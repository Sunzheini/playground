import importlib
import multiprocessing
from multiprocessing import Queue
from pathlib import Path
from typing import Any, Dict

import yaml

# Windows safe start method
if multiprocessing.get_start_method(allow_none=True) is None:
    try:
        multiprocessing.set_start_method("spawn")
    except RuntimeError:
        # already set by parent process
        pass


def _import_from_fqn(fqn: str):
    """Import an attribute from a fully qualified name like 'package.module.attr'."""
    module_name, attr_name = fqn.rsplit('.', 1)
    module = importlib.import_module(module_name)
    return getattr(module, attr_name)


def load_yaml(path: str | Path) -> Dict[str, Any]:
    with open(path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)


def build_queue(defn: Dict[str, Any]) -> Queue:
    # For now we only support multiprocessing.Queue with optional maxsize
    maxsize = int(defn.get('maxsize', 0) or 0)
    return Queue(maxsize=maxsize)


def run_job(config_path: str | Path, job_name: str | None = None) -> None:
    """
    Minimal runner that understands the custom_pipeline.yaml format authored in this repo.
    It will:
      - create queues
      - locate the job entrypoint and simply call it if present (function_5)
        so the code path remains canonical
    """
    cfg = load_yaml(config_path)

    # Materialize queues for potential future use. We pass nothing yet because function_5
    # internally constructs its own Queue and processes, but this keeps the door open for
    # future wiring where function_5 could accept an external queue.
    queue_objs = {}
    for q in cfg.get('queues', []) if cfg else []:
        queue_objs[q['name']] = build_queue(q)

    # Select job
    jobs = cfg.get('jobs', []) if cfg else []
    if not jobs:
        raise RuntimeError("No jobs defined in YAML.")

    job = None
    if job_name:
        for j in jobs:
            if j.get('name') == job_name:
                job = j
                break
        if job is None:
            raise RuntimeError(f"Job '{job_name}' not found in YAML.")
    else:
        job = jobs[0]

    entry = job.get('entrypoint') or {}
    module = entry.get('module')
    function = entry.get('function')
    if not module or not function:
        raise RuntimeError("Job entrypoint must provide module and function.")

    # Import and invoke the function. For this project the job is function_5.
    fn = _import_from_fqn(f"{module}.{function}")

    # Call entrypoint. If in the future we want to pass a queue, adjust function_5 signature.
    fn()


if __name__ == "__main__":
    # Default to the colocated custom_pipeline.yaml and job 'run_function_5'
    this_dir = Path(__file__).parent
    default_yaml = this_dir / 'custom_pipeline.yaml'
    run_job(str(default_yaml), job_name='run_function_5')
