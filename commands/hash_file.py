import hashlib
import os.path
import sys

args = sys.argv


def hash_file(args):
    if os.path.exists(args[2]):
        with open(args[2]) as file:
            data = file.read()
            hash_object = hashlib.md5(data.encode()).hexdigest()
            print(hash_object)
            return hash_object
