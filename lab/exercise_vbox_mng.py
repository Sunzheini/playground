import subprocess

path: str = 'C:\\Program Files\\Notepad++\\notepad++.exe'


def open_path(path_to_open: str) -> None:
    subprocess.Popen(path_to_open)


def main() -> None:
    try:
        open_path(path)
    except FileNotFoundError:
        print(f"File not found: {path}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == '__main__':
    main()
else:
    print("This script is not being run directly.")
    print("It is likely being imported as a module.")
