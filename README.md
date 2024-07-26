# mts-pos

# REQUIREMENTS
1. Execute this command:
* ```pip install -r requirements.txt```

# STANDARDS
1. Keep the object name of the widgets in camel casing.
2. Always use horizontal/vertical layout when creating a button box.
3. Naming conventions:
* ```variables and functions should start in lowercase and in the form of camel case```
* ```class should start in uppercase and in the form of camel case```
* ```Always use the name 'accessCode' for naming variables that are named 'password'```
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