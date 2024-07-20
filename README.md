# mts-pos

# REQUIREMENTS
1. Create a virtual environment:
* ```python -m venv venv```
2. Activate the virtual environment:
* ```venv\Scripts\activate```
3. Install the following libraries:
* ```pip install pyinstaller```
* ```pip install pandas```
* ```pip install pyqt5```
* ```pip install pywin32```
* ```pip install py-machineid```
* ```pip install python-dotenv```
* ```pip install sqlalchemy```
* ```pip install sqlalchemy-libsql```
* ```pip install libsql-experimental```

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
```my_pos_app/
├── LICENSE
├── README.md
├── requirements.txt
├── setup.py
├── my_pos_app/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   ├── database/
│   │   ├── __init__.py
│   │   ├── db_manager.py
│   │   └── models.py
│   ├── ui/
│   │   ├── __init__.py
│   │   ├── main_window.ui
│   │   └── dialogs/
│   │       ├── __init__.py
│   │       ├── settings_dialog.ui
│   │       └── about_dialog.ui
│   ├── views/
│   │   ├── __init__.py
│   │   ├── main_window.py
│   │   └── dialogs/
│   │       ├── __init__.py
│   │       ├── settings_dialog.py
│   │       └── about_dialog.py
│   ├── controllers/
│   │   ├── __init__.py
│   │   ├── main_controller.py
│   │   └── dialogs/
│   │       ├── __init__.py
│   │       ├── settings_controller.py
│   │       └── about_controller.py
│   ├── assets/
│   │   ├── images/
│   │   └── styles/
│   └── utils/
│       ├── __init__.py
│       ├── helpers.py
│       └── validators.py
└── tests/
    ├── __init__.py
    ├── test_main.py
    ├── test_db_manager.py
    └── test_helpers.py```
