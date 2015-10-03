import os

_SPECIAL_DIRS = ('.git', '.hg', '.svn')

def normalize_file_path(path):
    path = str(path)
    dirname = os.path.normpath(path)
    while dirname != '/':
        for special_dir in _SPECIAL_DIRS:
            if os.path.isdir(os.path.join(dirname, special_dir)):
                return os.path.normpath(os.path.relpath(path, dirname))
        dirname = os.path.dirname(dirname)
    return path