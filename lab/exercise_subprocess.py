import subprocess


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


if __name__ == "__main__":
    cmd_path = r"C:\Appl\Projects\C#\Studio5000SDKController\build\bin\Debug"
    exe_path = r"C:\Appl\Projects\C#\Studio5000SDKController\build\bin\Debug\Studio5000Controller.exe"
    project_path = r"C:\Appl\Projects\Rockwell\OPC_UA_Server.ACD"
    open_cmd_and_send_command(cmd_path, exe_path, project_path)
