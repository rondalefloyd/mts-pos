import sys, os
import PyInstaller.__main__

sys.path.append(os.path.abspath('')) # required to change the default path

# PyInstaller options
opts = [
    '--distpath', 'dist',
    '--workpath', 'build',
    '--onefile',
    # '--noconsole',
    # '--icon', 'icon_path',
    '--name', 'ms-superstore-pos',
    '--add-data', '.env;.',
    '--add-data', 'tests/database/sales.db;tests/database',
    '--add-data', 'tests/database/system.db;tests/database',
    'app/main.py'
]

# Run PyInstaller
PyInstaller.__main__.run(opts)
