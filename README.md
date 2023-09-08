# Introduction
KNotes is a flask web application that allows the user to create an account, write notes and delete notes.

## Installation
```bash
git clone https://github.com/kevinkoech357/KNotes

cd KNotes
```
## Setting up python virtual environment
```bash
python3 -m venv env

source env/bin/activate
```
### Installing dependencies
```bash
pip install -r requirements.txt
```
## Starting server
Option 1:
```bash
flask --app run run
```
Option 2:
```bash
gunicorn -w 4 run:app
```
## Checking live
Option 1:
Go to your browser and input=> ```http://127.0.0.1:5000```

Option 2:
Go to your browser and input=> ```http://127.0.0.1:8000```

## Bugs
* Deleting note doesn't work as expected. Will fix soon.
* Can't cancel flash messages.
