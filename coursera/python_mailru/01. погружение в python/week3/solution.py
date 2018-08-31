import os


class FileReader(str):

    def read(self):
        storage_path = os.path.join(self)
        try:
            with open(storage_path, 'r') as test_file:
                test_file.seek(0)
                temp_load = test_file.read()
            return str(temp_load)
        except OSError:
            return ''


reader = FileReader("example.txt")
print(reader.read())


# Инициализатор этого класса принимает аргумент - путь до файла на диске.
#
# У класса должен быть метод read, возвращающий содержимое файла в виде строки.
#
# Еще один момент - внутри метода read вы должны обрабатывать исключение IOError, возникающее, когда файла,
# с которым был инициализирован класс, на самом деле нет на жестком диске. В случае возникновения такой ошибки
# метод read должен возвращать пустую строку "".
