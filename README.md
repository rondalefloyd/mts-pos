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
