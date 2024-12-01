# mts-pos

# REQUIREMENTS
1. To update the requirement list:
```pip freeze > requirements.txt```

2. To install the requirements from the list:
```pip install -r requirements.txt```

3. To make executable file, make sure to change the execution policy in order to activate 'venv'
```Get-ExecutionPolicy```
4. Run Windows Powershell as Admin
```Set-ExecutionPolicy RemoteSigned```

# STANDARDS
1. Keep the object name of the widgets in camel casing.
2. Always use horizontal/vertical layout when creating a button box.
3. Naming conventions:
* ```variables and functions should start in lowercase and in the form of camel case```
* ```class should start in uppercase and in the form of camel case```
* ```Always use the name 'password' for naming variables that are named 'password'```
4. Do not perform nested if statements (if statements inside for loops are allowed).
5. Try/except conventions:
* ```Always add print statements when doing error handling to track errors easier.```
* ```Only use try/except statements where the errors would likely occur```
6. Variable conventions:
* ```Only declare variable when the value will be used multiple times inside the scope```
* ```Always declare variables with initial values when writing a checker (i.e. null, [], "", 0)```
7. 'windowEvent' values:
* ```NO_EVENT (nothing will happen/breaks loops)```
* ```START_<CONTROLLER_NAME> (run the window)```
8. Nesting conventions:
* ```Do not write nested if statements more than 1```
9. Create a script for the executable file that displays all the logs
10. Apply threading in functions that uses functions with loopings
11. Code structure ordering:
* ```Imports```
* ```Class Definition```
* ```Initialization Method (__init__)```
* ```Public Methods (event handlers)```
* ```Private Methods (helper functions)```
* ```Overridden Methods (like closeEvent)```

# DIRECTORY STRUCTURE
```
├── app/
│   ├── controllers/ <-- contains crud functions
│   ├── models/ <-- contains ORM classes and database schema definitions
│   ├── utils/ <-- contains app config
│   └── views/
│       ├── assets/ <-- contains images
│       ├── components/ <-- contains specific function for the ui
│       └── templates/ <-- contains auto-generated ui files
├── tests/
└── venv/ <-- contains libraries
├── .env
├── .env.template
├── .gitignore
├── LICENSE
├── README.md
├── requirements.txt
└── setup.py
```

# NEW INSTRUCTIONS
install 'Qt for Python' extension for easy compilation of ui files

to setup device as the db server, run setup.py

python -m venv venv -> to create virtual env
pip freeze > requirements.txt -> to collect all installed requirements/libraries
pip install -r requirements.txt -> to install all collected requirements/libraries

if new libraries were installed, always run 'pip freeze > requirements.txt' after to avoid conflicts for other venv


pyqt5
peewee
Cython
ipython
dotenv
pandas
pywin32
python-docx

Python 3.12.6

all should be trust