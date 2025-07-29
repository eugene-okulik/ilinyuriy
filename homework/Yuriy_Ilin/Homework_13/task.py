import datetime
from pathlib import Path

current_path = Path(__file__)
data_path = current_path.resolve().parents[2] / "eugene_okulik" / "hw_13" / "data.txt"
abs_path = data_path.resolve()  # Создание абсолютного пути для доп безопасности


def get_dates():
    try:
        # Проверка существует ли путь
        if not abs_path.exists():
            raise FileNotFoundError(f"Файл не найден в: {abs_path}")

        # Проверка файл ли лежит в абсолютном пути
        if not abs_path.is_file():
            raise IsADirectoryError("Это не файл")

        with open(abs_path) as file:
            line = file.readlines()

        date_1 = datetime.datetime.strptime(line[0][3:29], "%Y-%m-%d %H:%M:%S.%f")
        print(date_1 + datetime.timedelta(days=7))

        weekdays = {
            0: "Понедельник",
            1: "Вторник",
            2: "Среда",
            3: "Четверг",
            4: "Пятница",
            5: "Суббота",
            6: "Воскресенье",
        }
        date_2 = datetime.datetime.strptime(line[1][3:29], "%Y-%m-%d %H:%M:%S.%f")
        print(f"{date_2} - {weekdays[date_2.weekday()]}")

        date_3 = datetime.datetime.strptime(line[2][3:29], "%Y-%m-%d %H:%M:%S.%f")
        date_now = datetime.datetime.now()
        print(f"Дата {date_3} была {(date_now - date_3).days} назад")

    except FileNotFoundError:
        print(f"Файл не найден в: {abs_path}")

    except IsADirectoryError:
        print("Это не файл")

    except PermissionError as e:
        print("Недостаточно прав для чтения файла:", e)

    except Exception as e:
        print("Произошла непредвиденная ошибка:", e)


get_dates()
