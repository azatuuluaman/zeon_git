import os.path
import sys
from pathlib import Path

args = sys.argv

if not len(args) < 2:
    exit(0)

dir = ".zeon_fs3"

path = 'zeon_fs2/' + dir

if not Path(path).is_dir():
    os.makedirs('.zeon_fs3')
    exit(0)
