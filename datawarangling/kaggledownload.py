import os
import sys

path = os.path.join(os.path.expanduser('~'), '.kaggle')

try:
    os.makedirs(path)
except FileExistsError:
    pass

"""To Safeguard the file keep its permission 600
with open(os.path.join(path, 'kaggle.json'), 'r') as fp:
    os.chmod(fp.name, 0o600)
"""

from kaggle import cli

"""--force is to force download the file even if its already downloded."""
sys.argv = 'kaggle competitions download -c titanic --force'.split()
"""calling kaggle cli to get the files using credentials from ~/.kaggle/kaggle.json"""
cli.main()
