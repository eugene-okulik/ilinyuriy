import mysql.connector as mysql
from mysql.connector import Error


# Список допустимых таблиц для ввода
allowed_tables = {"students", "books", "groups", "subjects", "lessons", "marks"}


def add_connection():
    '''Создаем соединение'''
    try:
        db = mysql.connect(
            user='st-onl',
            passwd='AVNS_tegPDkI5BlB2lW5eASC',
            host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
            port=25060,
            database='st-onl'
        )
        if db.is_connected():
            return db
    except Error as e:
        print(f"Ошибка подключения к БД: {e}")
        return None


def insert_row_db(db, table: str, columns: list | tuple, values: list | tuple):
    """
    Универсальная вставка строки в таблицу.

    :param db: соединение с БД
    :param table: имя таблицы
    :param columns: list или tuple строк — имена столбцов
    :param values: list или tuple — значения для вставки
    :return: ID добавленной строки
    """
    if not db or not db.is_connected():
        print("Нет соединения с БД")
        return None

    if table not in allowed_tables:
        raise ValueError("Недопустимая таблица!")

    if not isinstance(columns, (list, tuple)) or not isinstance(values, (list, tuple)):
        raise ValueError("columns и values должны быть 'list' или 'tuple'!")

    if len(columns) != len(values):
        raise ValueError("Количество значений columns и values должно совпадать!")

    if not columns or not values:
        raise ValueError("Столбцы и значения не могут быть пустыми!")

    try:
        with db.cursor() as cursor:
            columns_str = ', '.join(f"`{col}`" for col in columns)
            placeholders = ', '.join(['%s'] * len(values))
            query = f"INSERT INTO `{table}` ({columns_str}) VALUES ({placeholders})"
            cursor.execute(query, values)
            db.commit()
            return cursor.lastrowid
    except Error as e:
        print(f"Ошибка {e}")
        return None


def insert_many_rows_db(db, table: str, columns: list | tuple, values: list):
    """
    Универсальная вставка нескольких строк в таблицу.

    :param db: соединение с БД
    :param table: имя таблицы
    :param columns: list или tuple строк — имена столбцов
    :param values: list - список добавляемых данных list[tuple | list]
    :return: кол-во добавленных строк
    """
    if not db or not db.is_connected():
        print("Нет соединения с БД")
        return None

    if table not in allowed_tables:
        raise ValueError("Недопустимая таблица!")

    if not isinstance(columns, (list, tuple)):
        raise ValueError("columns должен быть 'list' или 'tuple'!")

    if not isinstance(values, list) or not all(isinstance(row, (list, tuple)) for row in values):
        raise ValueError("values должен быть списком кортежей или списков!")

    if not columns or not values:
        raise ValueError("Столбцы и значения не могут быть пустыми!")

    for row in values:
        if len(row) != len(columns):
            raise ValueError("Каждое значение должно соответствовать количеству столбцов!")

    try:
        with db.cursor() as cursor:
            columns_str = ', '.join(f"`{col}`" for col in columns)
            placeholders = ', '.join(['%s'] * len(columns))
            query = f"INSERT INTO `{table}` ({columns_str}) VALUES ({placeholders})"
            cursor.executemany(query, values)
            db.commit()
            return cursor.rowcount
    except Error as e:
        print(f"Ошибка при множественной вставке: {e}")
        return None


def update_rows_db(db, table: str, column_value: dict, where_value: dict):
    """
    Универсальный способ обновить запись в таблице.

    :param db: соединение с БД
    :param table: имя таблицы
    :param column_value: dict — столбец: новое значение поля
    :param where_value: dict — столбец: значение поля, по которому происходит изменение данных
    :return: кол-во измененных строк
    """
    if not db or not db.is_connected():
        print("Нет соединения с БД")
        return None

    if table not in allowed_tables:
        raise ValueError("Недопустимая таблица!")

    if not isinstance(column_value, dict) or not isinstance(where_value, dict):
        raise ValueError("column_value и where_value должны быть 'dict'!")

    for key, value in column_value.items():
        if not key or value is None:
            raise ValueError(f"Недопустимая пара ключ/значение: '{key}': {value}")

    for key, value in where_value.items():
        if not key or value is None:
            raise ValueError(f"Недопустимая пара ключ/значение: '{key}': {value}")

    try:
        with db.cursor() as cursor:
            set_clause = ', '.join(f"`{col}` = %s" for col in column_value)
            where_clause = ' AND '.join(f"`{col}` = %s" for col in where_value)
            query = f"UPDATE {table} SET {set_clause} WHERE {where_clause}"
            values = tuple(column_value.values()) + tuple(where_value.values())
            cursor.execute(query, values)
            db.commit()
            return cursor.rowcount
    except Error as e:
        print(f"Ошибка {e}")
        return None


def get_marks_student(db, student_id):
    '''Получение всех оценок студента'''
    if not db or not db.is_connected():
        print("Нет соединения с БД")
        return None
    try:
        with db.cursor(dictionary=True) as cursor:
            query = """
                SELECT DISTINCT s.name, s.second_name, m.value, l.title
                FROM students s LEFT JOIN marks m ON m.student_id = s.id
                LEFT JOIN lessons l ON l.id = m.lesson_id
                WHERE s.id = %s;
            """
            cursor.execute(query, (student_id,))
            return cursor.fetchall()
    except Error as e:
        print(f"Ошибка при выполнении запроса на получение оценок студента: {e}")


def get_books_student(db, student_id):
    '''Получение всех оценок студента'''
    if not db or not db.is_connected():
        print("Нет соединения с БД")
        return None
    try:
        with db.cursor(dictionary=True) as cursor:
            query = """
                SELECT s.name, s.second_name, b.title
                FROM students s JOIN books b ON s.id = b.taken_by_student_id
                WHERE s.id = %s
            """
            cursor.execute(query, (student_id,))
            return cursor.fetchall()
    except Error as e:
        print(f"Ошибка при выполнении запроса на получение книг студента: {e}")


def get_info_student(db, student_id):
    '''Получение всех оценок студента'''
    if not db or not db.is_connected():
        print("Нет соединения с БД")
        return None
    try:
        with db.cursor(dictionary=True) as cursor:
            query = """
                SELECT
                    s.id AS 'Id student', s.name, s.second_name,
                    g.id AS 'Id group', g.title AS 'title group', g.start_date, g.end_date,
                    l.title AS 'title lesson',
                    sub.title AS 'title subject',
                    m.value,
                    (SELECT GROUP_CONCAT(title SEPARATOR ', ') FROM books WHERE taken_by_student_id = %s) AS books
                FROM students s
                LEFT JOIN `groups` g ON s.group_id = g.id
                LEFT JOIN marks m ON m.student_id = s.id
                LEFT JOIN lessons l ON m.lesson_id = l.id
                LEFT JOIN subjects sub ON l.subject_id = sub.id
                WHERE s.id = %s;
            """
            cursor.execute(query, (student_id, student_id))
            return cursor.fetchall()
    except Error as e:
        print(f"Ошибка при выполнении запроса на информации по студенту: {e}")


# Создаем соединение
db = add_connection()

# Создаем и получаем id студента
student_id = insert_row_db(db, 'students', ['name', 'second_name'], ('Марк', 'Авралий'))

# Создаем книги для студента
count_books = insert_many_rows_db(
    db, 'books',
    ['title', 'taken_by_student_id'], [('Книга о быте', student_id), ('Вавилон & Python', student_id)]
)

# Создаем группу и получаем ее id
group_id = insert_row_db(
    db, 'groups', ['title', 'start_date', 'end_date'], ('Project AQA', 'Jan 2025', 'Dec 2025')
)

# Добавляем (изменяем) группу студента
update_rows_db(db, 'students', {'group_id': group_id}, {'id': student_id})

# Создание учебных предметов
subjects_1 = insert_row_db(db, 'subjects', ['title'], ('MegaSub 1',))
subjects_2 = insert_row_db(db, 'subjects', ['title'], ('UltraSub 1',))

# Создание занятий
lesson_1 = insert_row_db(db, 'lessons', ['title', 'subject_id'], ('Занятие v1.0', subjects_1))
lesson_2 = insert_row_db(db, 'lessons', ['title', 'subject_id'], ('Занятие v2.0', subjects_1))
lesson_3 = insert_row_db(db, 'lessons', ['title', 'subject_id'], ('Занятие v3.0', subjects_2))
lesson_4 = insert_row_db(db, 'lessons', ['title', 'subject_id'], ('Занятие v4.0', subjects_2))

# Создание оценок
count_marks = insert_many_rows_db(
    db, 'marks',
    ['value', 'lesson_id', 'student_id'],
    [(5, lesson_1, student_id),
     (5, lesson_2, student_id),
     (3, lesson_3, student_id),
     (1, lesson_4, student_id)]
)

# Все оценки студента (Получение только столбцов ФИО, оценки и предмета)
print(get_marks_student(db, student_id))

# Все книги студента
print(get_books_student(db, student_id))

# Вся информация по студенту
print(get_info_student(db, student_id))

db.close()
