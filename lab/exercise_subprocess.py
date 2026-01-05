import subprocess
import sys


# 1. Using subprocess to open a command prompt and run an executable with arguments
def open_cmd_and_send_command(cmd, exe, project):
    try:
        # Open command prompt
        cmd_process = subprocess.Popen(['cmd', '/K', exe, project], cwd=cmd)
        cmd_process.wait()

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Close the command prompt process
        if cmd_process:
            cmd_process.terminate()


# 2.
def run_tests(request: dict = None):
    """Run tests programmatically"""
    try:
        test_pattern = request.get("test_pattern") if request else None

        cmd = [sys.executable, "-m", "pytest", "-v", "--tb=short"]
        if test_pattern:
            cmd.extend(["-k", test_pattern])
        else:
            cmd.append("tests/")

        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            cwd=".",
            check=True  # Will raise CalledProcessError for non-zero exit codes
        )

        return {
            "success": result.returncode == 0,
            "stdout": result.stdout,
            "stderr": result.stderr,
            "returncode": result.returncode,
        }

    # Handle when pytest fails (non-zero exit code)
    except subprocess.CalledProcessError as e:
        return {
            "success": False,
            "error": f"Tests failed with exit code {e.returncode}",
            "stdout": e.stdout if hasattr(e, 'stdout') else "",
            "stderr": e.stderr if hasattr(e, 'stderr') else "",
            "returncode": e.returncode,
        }
    except Exception as e:
        return {"success": False, "error": str(e), "stdout": "", "stderr": ""}


if __name__ == "__main__":
    # cmd_path = r"C:\Appl\Projects\C#\Studio5000SDKController\build\bin\Debug"
    # exe_path = r"C:\Appl\Projects\C#\Studio5000SDKController\build\bin\Debug\Studio5000Controller.exe"
    # project_path = r"C:\Appl\Projects\Rockwell\OPC_UA_Server.ACD"
    # open_cmd_and_send_command(cmd_path, exe_path, project_path)

    test_result = run_tests({"test_pattern": "addition"})
