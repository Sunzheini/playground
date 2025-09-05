"""
create a .gitignore file to exclude unnecessary files from being tracked by git:
.idea/
__pycache__/
.venv/
venv/
*.sqlite3
*.db
Thumbs.db
.env
"""


"""
If Pycharm is still tracking a file you added to .gitignore, you may need to manually remove it from the git index using the following command:
git rm --cached <file_path>
example: git rm --cached .env
"""