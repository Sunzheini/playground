"""
1. create a folder: `D:\Study\Projects\Github\AegisAI\shared-lib`
2. `poetry init` -> creates a pyproject.toml
3. inside create a folder `shared_lib` with __init__.py inside
4. change toml to:
    [project]
    name = "shared-lib"
    version = "0.1.0"
    description = "Shared code for microservices"
    authors = [
        {name = "Sunzheini",email = "daniel_zorov@abv.bg"}
    ]
    readme = "README.md"
    requires-python = ">=3.11"
    dependencies = [
    ]

    [tool.setuptools]
    packages = ["shared_lib"]

    [build-system]
    requires = ["poetry-core>=2.0.0,<3.0.0"]
    build-backend = "poetry.core.masonry.api"
5. moved shared files there and change the imports in all the files inside shared-lib, e.g.:
inside the file shared-lib/needs/ResolveNeedsManager.py ->

# from needs.INeedRedisManager import INeedRedisManagerInterface
# from redis_management.redis_manager import RedisManager
from .INeedRedisManager import INeedRedisManagerInterface
from ..redis_management.redis_manager import RedisManager

6. in services/api-gateway-service/pyproject.toml add:
`"shared-lib @ file:///D:/Study/Projects/Github/AegisAI/shared-lib"`
at the end of the `dependencies` list
7. in services/api-gateway-service/ run:
`poetry lock` and `poetry install --no-root`,
you should see `  - Installing shared-lib (0.1.0 D:/Study/Projects/Github/AegisAI/shared-lib)`
8. change from
`contracts.job_schemas import IngestionJobRequest` to
`shared_lib.contracts.job_schemas import IngestionJobRequest`
"""

"""
Updating the shared-lib package:
1. version = "0.1.1" in shared-lib/pyproject.toml: increase the version so that next line will work!

2. in services/api-gateway-service/ run:
`poetry cache clear . --all` to clear the cache
`poetry update shared-lib`
"""