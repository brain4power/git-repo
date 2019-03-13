import os
import tempfile


class File:
    def __init__(self, path):
        self.path = path
        try:
            with open(self.path, 'r', encoding='UTF-8'):
                pass
        except FileNotFoundError:
            with open(self.path, 'w', encoding='UTF-8'):
                pass

    def write(self, input_text):
        with open(self.path, 'w', encoding='UTF-8') as fd:
            fd.write(input_text)

    def read(self):
        with open(self.path, 'r', encoding='UTF-8') as fd:
            fd.seek(0)
            return fd.read()

    def __add__(self, obj1):
        storage_path = os.path.join(tempfile.gettempdir(), 'summary.txt')
        with open(storage_path, 'w') as new_obj_file:
            with open(self.path, 'r') as self_file:
                self_file.seek(0)
                with open(obj1.path, 'r') as obj1_file:
                    obj1_file.seek(0)
                    new_obj_file.write(self_file.read() + '\n' + obj1_file.read())
        return File(storage_path)

    def __str__(self):
        return self.path

    def __iter__(self):
        return open(self.path, 'r', encoding='UTF-8')


if __name__ == "__main__":
    first = File('first.txt')
    second = File('second.txt')
    #first.write('1111\n22222')
    second.write('2')
    new_obj = first + second
    #print(first.read() + second.read())
    #print(new_obj.read())
    for line in first:
        print('line=', line)
    # with open('first.txt', 'r') as te:
    #     print(te.readline())
    #     print('-------')
