import os
import tempfile


class File:
    def __init__(self, path):
        self.path = path
        self._full_path = os.path.join(tempfile.gettempdir(), path)

    def write(self, str_to_write):
        pass


if __name__ == "__main__":
    obj = File('/tmp/file.txt')
    print("path = ", obj._full_path)
