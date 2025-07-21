import pathlib
"""
The pathlib module (introduced in Python 3.4) provides an object-oriented way to 
handle filesystem paths, replacing older os.path functions with a more intuitive API.
"""

# Create a Path object
current_dir = pathlib.Path(".")  # Relative path
home_dir = pathlib.Path.home()   # User's home directory
abs_path = pathlib.Path("/tmp/data")  # Absolute path

# Join paths using `/`
config_path = home_dir / ".config" / "my_app" / "settings.json"
print(config_path)  # Output: /home/user/.config/my_app/settings.json (Linux/macOS)


path = pathlib.Path("data/logs/app.log")
print("Exists?", path.exists())
print("Is file?", path.is_file())
print("Filename:", path.name)       # Output: app.log
print("Stem:", path.stem)           # Output: app
print("Extension:", path.suffix)    # Output: .log
print("Parent dir:", path.parent)   # Output: data/logs