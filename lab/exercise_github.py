"""
Step 1 — Create the PAT on GitHub
Go to github.com → click your profile picture (top right) → Settings
Scroll down to Developer settings (bottom of left sidebar)
Click Personal access tokens → Tokens (classic)
Click "Generate new token (classic)"
Give it a name, e.g. ccc-ci-token
Set expiration (e.g. 90 days or No expiration)
Under Select scopes, check repo (this gives full read access to private repos)
Click "Generate token"
Copy the token immediately — you won't see it again

Step 2 — Add the secret to ccc-app-backend-main
Go to your ccc-app-backend-main repo on GitHub
Click Settings tab
Left sidebar → Secrets and variables → Actions
Click "New repository secret"
Fill in:
Name: PAT
Secret: paste the token from Step 1
Click "Add secret"
"""