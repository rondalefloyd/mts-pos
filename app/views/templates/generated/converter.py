import os
import sys
import subprocess

sys.path.append(os.path.abspath(''))  # required to change the default path

def convert_ui_to_py(ui_file, output_dir):
    # Generate the output .py file path
    py_file = os.path.join(output_dir, os.path.splitext(os.path.basename(ui_file))[0] + '_ui.py')
    
    # Run the pyuic5 command to convert .ui to .py
    subprocess.run(['pyuic5', '-o', py_file, ui_file], check=True)
    
    # Modify the imports in the generated .py file
    with open(py_file, 'r') as file:
        content = file.read()
    
    content = content.replace(
        'from PyQt5 import QtCore, QtGui, QtWidgets',
        "import os, sys\nsys.path.append(os.path.abspath(''))  # required to change the default path\nfrom app.utils.pyqt5 import QtWidgets, QtCore, QtGui"
    )
    
    with open(py_file, 'w') as file:
        file.write(content)

def main():
    # Directory containing .ui files
    ui_directory = 'C:/Users/mimoy/Documents/GitHub/mts-pos/app/views/templates/generated'
    # Directory to save converted .py files
    output_directory = 'C:/Users/mimoy/Documents/GitHub/mts-pos/app/views/templates'
    
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Convert each .ui file in the directory
    for ui_file in os.listdir(ui_directory):
        if ui_file.endswith('.ui'):
            convert_ui_to_py(os.path.join(ui_directory, ui_file), output_directory)
            print(f'Converted {ui_file} to .py file')

if __name__ == '__main__':
    main()
    print('test')
