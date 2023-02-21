import os
import pathlib
import shutil


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

    def chdir(self, dir_name: str):
        '''Сменить директорию'''
        self.storage.add_path((dir_name))
        curr_path = self.storage.current_path()
        try:
            os.chdir(curr_path)
        except FileNotFoundError:
            self.storage.add_path(f"..{self.sep}")
            print(f"Директории {dir_name} не существует")
        except NotADirectoryError:
            self.storage.add_path(f"..{self.sep}")
            print(f"Файл {dir_name} не является директорией")

    def mkdir(self, dir_name: str):
        '''Создание директории'''
        current_path = self.storage.path2file(dir_name)
        try:
            os.mkdir(current_path)
        except FileExistsError:
            print(f"Директория {dir_name} уже существует!")

    def rmdir(self, dir_name: str):
        ''''Удаление папки по имени'''
        curr_path = self.storage.path2file(dir_name)
        try:
            os.rmdir(curr_path)
        except OSError:
            try:
                shutil.rmtree(curr_path, ignore_errors=False, onerror=None)
            except FileNotFoundError:
                print(f"Директории {dir_name} не существует")
            except NotADirectoryError:
                print(f"Файл {dir_name} не является директорией")
        except FileNotFoundError:
            print(f"Директории {dir_name} не существует")
        except NotADirectoryError:
            print(f"Файл {dir_name} не является директорией")

    def touch(self, file_name: str):
        '''Создание пустого файла'''
        curr_path = self.storage.path2file(file_name)
        try:
            open(curr_path, 'w').close()
        except FileExistsError or IsADirectoryError:
            print(f'Файл с именем {file_name} уже существует!')

    def rename(self, old_name: str, new_name: str):
        """Переименование файлов"""
        path_old = self.storage.path2file(old_name)
        path_new = self.storage.path2file(new_name)
        try:
            if not os.path.isfile(path_new): # проверяем, что новое имя не занято
                os.rename(path_old, path_new)
            else:
                raise IsADirectoryError
        except FileNotFoundError:
            print(f"Указанного файла {old_name} не существует")
        except IsADirectoryError or FileExistsError:
            print(f"Файл с названием {new_name} уже существует")

    def rm(self, file_name: str):
        """Удаление файлов по имени"""
        path = self.storage.path2file(file_name)
        if os.path.isfile(path):
            os.remove(path)
        else:
            print(f"Файла {file_name} не существует")

    def write(self, file_name: str, *data: str):
        """Запись текста в файл"""
        text = " ".join(data)
        path = self.storage.path2file(file_name)
        try:
            with open(path, "a") as file:
                file.write(text)
        except IsADirectoryError:
            print(f"Указанный файл: {file_name} является директорией")


test = WorkingDirectory(os.sep)
test.current_path()

