import os
import pathlib
import shutil
from settings import WORKING_DIR


class FileManager:

    def __int__(self):
        pass

    def ls(self):
        """Выводит содержимое директории"""
        curr_path = str(pathlib.Path.cwd())
        files_list = os.listdir(curr_path)
        for i in range(len(files_list)):
            if pathlib.Path(files_list[i]).is_dir():
                files_list[i] = f"*dir* {files_list[i]}"
            elif pathlib.Path(files_list[i]).is_file():
                files_list[i] = f"*file* {files_list[i]}"
        r = "\n".join(files_list)
        print(f"Содержимое {curr_path}:\n{r}")

    def cd(self, dir_name: str):
        curr_path = str(pathlib.Path.cwd())
        if WORKING_DIR in curr_path:
            try:
                os.chdir(os.path.join(curr_path, dir_name))
            except FileNotFoundError or NotADirectoryError:
                print(f"Директории {dir_name} не существует или \
                      файл {dir_name} не является директорией")
        elif WORKING_DIR in curr_path and WORKING_DIR != curr_path and dir_name == "..":
            curr_path = str(pathlib.Path.cwd().parent)
            os.chdir(curr_path)
        else:
            print("Вы пытаетесь выйти за пределы рабочей директории. \
                  А ну-ка брысь отсюда!")

    def pwd(self):
        print(str(pathlib.Path.cwd()))

    # TODO: доделать перемещение и копирование файлов и папок
    def mv(self):
        pass

    def cp(self, dir_name: str, path: str):
        """Копирование файлов из одной папки в другую"""
        pass

    def mkdir(self, dir_name: str):
        '''Создание директории'''
        new_dir = pathlib.Path.joinpath(WORKING_DIR, dir_name)
        try:
            new_dir.mkdir(mode=0o666, parents=True)
        except FileExistsError:
            print(f"Директория {dir_name} уже существует!")

    def rmdir(self, dir_name: str):
        '''Удаление папки по имени'''
        try:
            dir2del = os.path.join(WORKING_DIR, dir_name)
            shutil.rmtree(dir2del, ignore_errors=False, onerror=None)
        except FileNotFoundError:
            print(f"Директории {dir_name} не существует")
        except NotADirectoryError:
            print(f"Файл {dir_name} не является директорией")

    def touch(self, file_name: str):
        '''Создание пустого файла в текущей директории'''
        path2file = pathlib.Path.cwd() / file_name
        try:
            path2file.touch(mode=0o666, exist_ok=False)
        except FileExistsError or IsADirectoryError:
            print(f'Файл с именем {file_name} уже существует!')

    def rename(self, old_name: str, new_name: str):
        """Переименование файлов и папок"""
        path_old = pathlib.Path(old_name)
        path_new = pathlib.Path(new_name)
        if path_old.exists() and not path_new.exists():   # проверяем, что новое имя не занято
            path_old.rename(str(path_new))
        else:
            print("Что-то пошло не так. Не могу переименовать {old_name} в {new_name}")

    def rm(self, file_name: str):
        """Удаление файлов по имени"""
        path2file = pathlib.Path(file_name).absolute()
        if path2file.is_file():
            path2file.unlink()
        else:
            print(f"Файла {file_name} не существует или является директорией")

    def write(self, file_name: str, *data: str):
        """Запись текста в файл"""
        data2write = " ".join(data)
        path2file = pathlib.Path(file_name)
        if path2file.is_file():
            path2file.write_text(data2write)
        else:
            print(f"Файла {file_name} не существует или является директорией")

    def cat(self, file_name: str):
        path2file = pathlib.Path(file_name)
        if path2file.is_file():
            print(path2file.read_text())
        else:
            print(f"Файла {file_name} не существует или является директорией")

    def router(self, command: str):
        """Ассоциация между командами и методами FileManager"""

        commands_dict = {
            "cd": "Перемещение между папками",
            "ls": "Вывод содержимого текущей папки на экран",
            "mkdir": "Создание папки",
            "rmdir": "Удаление папки",
            "create": "Создание файла",
            "rename": "Переименование файла/папки",
            "read": "Чтение файла",
            "remove": "Удаление файла",
            "copy": "Копирование файла/папки",
            "move": "Перемещение файла/папки",
            "write": "Запись в файл",
            "cwd": "Показать текущую директорию"
        }

        commands = [
            self.cd,
            self.ls,
            self.mkdir,
            self.rmdir,
            self.touch,
            self.rename,
            self.cat,
            self.rm,
            self.cp,
            self.mv,
            self.write,
            self.pwd
        ]
        item_dict = dict(zip(commands_dict.keys(), commands))
        return item_dict.get(command, None)




