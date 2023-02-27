from file_manager import FileManager
from settings import WORKING_DIR
import os


def main():
    # Экземпляр обработчика файлов
    file_processing = FileManager()
    try:
        os.mkdir(WORKING_DIR)
    except FileExistsError:
        pass
    os.chdir(WORKING_DIR)
    print(
        "Создана рабочая директория:" + str(WORKING_DIR) +
        "\nВы можете изменить рабочую директорию "
    )

    while True:

        command = input("\nВведите команду -> ").split(" ")

        # Остановка работы программы
        if command[0] == "exit":
            break

        # Получаем результат существования команды
        result = file_processing.router(command[0])
        # Если есть такая команда
        if result:
            try:
                result(*command[1:])
            except TypeError:
                print(f"Команда {command[0]} была вызвана с некорректными аргументами")

        else:
            commands_str = "\n".join(
                [
                    f"{key} - {value}"
                    for (key, value) in FileManager.get_commands().items()
                ]
            )
            print(f"Команда {command[0]} не найдена! Список команд:\n{commands_str}")

    print("Произведен выход из программы.")


if __name__ == "__main__":
    main()
