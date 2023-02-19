import os
import pathlib


class WorkingDirectory:

    def __init__(self, sep : str):
        self.sep = sep
        self.storage = ['storage: ']

    def current_path(self):
        '''Текущая иерархия директорий'''
        abs_path = pathlib.Path(__file__).parent.absolute()
        print('abs path:' + str(abs_path))
        return str(abs_path) + self.sep + self.sep.join(self.storage)

    def parent_path(self):
        '''Возвращает родительскую директорию (наддиректорию)'''
        abs_path = pathlib.Path(__file__).parent.absolute()
        print(self.storage[1:])
        return str(abs_path) + self.sep + self.sep.join(self.storage[:1])

    def path2file(self, file_name: str):
        """Возвращает путь к указанному файлу"""
        locale_storage = self.storage[:]
        locale_storage.append(file_name)
        abs_path = pathlib.Path(__file__).parent.absolute()
        return str(abs_path) + self.sep + self.sep.join(locale_storage)

    def add_path(self, path: str):
        """Отвечает за перемещение в иерархии директорий,
        а также ограничивает выход за пределы рабочей папки"""
        if ".." in path and len(self.storage) >= 1:
            self.storage.pop(-1)
        elif ".." in path and len(self.storage) == 1:
            print("Нельзя выходить за пределы рабочей директории!")
        else:
            self.storage.append(path)



class FileManager:

    def __int__(self):
        self.sep = os.sep
        self.storage = WorkingDirectory(self.sep)

    def change_dir(self):
        pass

    def make_dir(self, dir_name: str):
        "Создаем директорию, указывая имя"
        current_path = self.storage.path2file(dir_name)
        try:
            os.mkdir(current_path)
        except FileExistsError:
            print(f"Директория {dir_name} уже существует!")

test = WorkingDirectory(os.sep)
test.current_path()

