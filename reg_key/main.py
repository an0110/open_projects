
#Python3 version of hugo24's snippet
import winreg


def read(path, root=HKEY_CURRENT_USER):
    path, name = os.path.split(path)
    with suppress(FileNotFoundError), OpenKey(root, path) as key:
        return QueryValueEx(key, name)[0]


