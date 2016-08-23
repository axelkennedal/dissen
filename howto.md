# How to work on this project
Some handy dandy tips, *make sure you read all of it before getting started*.

## Environment
1. Clone this repo to your computer / pull to make sure you have the latest version.
2. Run `source dissenEnv/bin/activate` in your terminal to enter the virtual Python environment setup for the project.
3. To start a development server, run `python manage.py runserver` in a new terminal window, stop it with ctr-c.

## Feature Branches & Git
Create a new branch when you start working on a new feature and add your name to it (e.g. "contact model -axelkennedal"). **Don't commit directly to master** unless it's for stuff like readme.md etc.

### Creation & Merge
1. Create a new local branch and start working on it (make commits): `git checkout -b [new-branch-name] master`
2. After working on the new branch, use this to push to remote: `git push -u origin [new-branch-name]`
3. After this, create a pull request in GitHub, then merge when everything is ok.

Before a branch being merged **the code must have been reviewed and approved** by someone else. Just @ that person in the pull request (or write to them on Slack or whatever).

### Deletion
1. When done working on a branch (and everything has been merged with master), first do: `git checkout master`
2. Then remove the local branch: `git branch -d [new-branch-name]`
3. Lastly, remove the remote copy of the branch `git push origin --delete [new-branch-name]`

### Fixing mistakes
To cancel the current commit: `git reset --soft HEAD~`

## Github
Use issues and milestones!

## Changing/creating models
1. Change/create the code of the model(s)
2. Run `python manage.py makemigrations` to create migrations for the changes
3. Run `python manage.py migrate` to apply the changes to the database
4. Make one single git commit for both the changes in the model (python code) and the changes in the database (migrations).
