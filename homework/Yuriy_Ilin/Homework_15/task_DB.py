import mysql.connector as mysql
from mysql.connector import Error


def add_connection():
    '''Создаем соединение'''
    try:
        db = mysql.connect(
            user = 'st-onl',
            passwd = 'AVNS_tegPDkI5BlB2lW5eASC',
            host = 'db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
            port = 25060,
            database = 'st-onl'
        )
        if db.is_connected():
            return db
    except Error as e:
        print(f"Ошибка подключения к БД: {e}")
        return None


def insert_student(db, name, second_name, group_id=None):
    '''Создание студента. Изначально, если группа не известна/не создана, можно не указывать group_id'''
    if not db or not db.is_connected():
        print("Нет соединения с БД")
        return None
    try:
        with db.cursor() as cursor:
            query = """
                INSERT INTO students (name, second_name, group_id)
                VALUES (%s, %s, %s)
            """
            cursor.execute(query, (name, second_name, group_id))
            db.commit()
            object_id = cursor.lastrowid
            return object_id
    except Error as e:
        print(f"Ошибка при выполнении запроса на добавление студента: {e}")


def insert_book(db, title, taken_by_student_id):
    '''Создание книги'''
    if not db or not db.is_connected():
        print("Нет соединения с БД")
        return None
    try:
        with db.cursor() as cursor:
            query = """
                INSERT INTO books (title, taken_by_student_id)
                VALUES (%s, %s)
            """
            cursor.execute(query, (title, taken_by_student_id))
            db.commit()
            object_id = cursor.lastrowid
            return object_id
    except Error as e:
        print(f"Ошибка при выполнении запроса на добавление книги: {e}")


def insert_group(db, title, start_date, end_date):
    '''Создание группы'''
    if not db or not db.is_connected():
        print("Нет соединения с БД")
        return None
    try:
        with db.cursor() as cursor:
            query = """
                INSERT INTO `groups` (title, start_date, end_date)
                VALUES (%s, %s, %s)
            """
            cursor.execute(query, (title, start_date, end_date))
            db.commit()
            object_id = cursor.lastrowid
            return object_id
    except Error as e:
        print(f"Ошибка при выполнении запроса на создание группы: {e}")


def insert_subject(db, title):
    '''Создание учебного предмета'''
    if not db or not db.is_connected():
        print("Нет соединения с БД")
        return None
    try:
        with db.cursor() as cursor:
            query = """
                INSERT INTO subjects (title)
                VALUES (%s)
            """
            cursor.execute(query, (title,))
            db.commit()
            object_id = cursor.lastrowid
            return object_id
    except Error as e:
        print(f"Ошибка при выполнении запроса на создание учебного предмета: {e}")


def insert_lesson(db, title, subject_id):
    '''Создание занятия'''
    if not db or not db.is_connected():
        print("Нет соединения с БД")
        return None
    try:
        with db.cursor() as cursor:
            query = """
                INSERT INTO lessons (title, subject_id)
                VALUES (%s, %s)
            """
            cursor.execute(query, (title, subject_id))
            db.commit()
            object_id = cursor.lastrowid
            return object_id
    except Error as e:
        print(f"Ошибка при выполнении запроса на создание занятия: {e}")


def insert_mark(db, value, lesson_id, student_id):
    '''Добавление оценок'''
    if not db or not db.is_connected():
        print("Нет соединения с БД")
        return None
    try:
        with db.cursor() as cursor:
            query = """
                INSERT INTO marks (value, lesson_id, student_id)
                VALUES (%s, %s, %s)
            """
            cursor.execute(query, (value, lesson_id, student_id))
            db.commit()
            object_id = cursor.lastrowid
            return object_id
    except Error as e:
        print(f"Ошибка при выполнении запроса на добавление оценки: {e}")


def update_student_group(db, group_id, student_id):
    '''Добавление группы студенту'''
    if not db or not db.is_connected():
        print("Нет соединения с БД")
        return None
    try:
        with db.cursor() as cursor:
            query = """
                UPDATE students SET group_id = %s WHERE id = %s
            """
            cursor.execute(query, (group_id, student_id))
            db.commit()
    except Error as e:
        print(f"Ошибка при выполнении запроса на обновление группы студента: {e}")


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


def get_info_student(db, student_id, student_id2):
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
                LEFT JOIN `groups` g ON s.group_id  = g.id
                LEFT JOIN marks m ON m.student_id  = s.id
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

# Создаем студента и сразу получаем его id
student_id = insert_student(db, 'Пабло', 'Искалбар')

# Создаем книг и получение их id!!!
book_1 = insert_book(db, 'Гадкий утенок', student_id)
book_2 = insert_book(db, '365 дней', student_id)

# Создаем группу и сразу получаем ее id !!!
group_id = insert_group(db, 'Острые QAзырьки', 'Jan 2025', 'Dec 2025')

# Добавляем студента в группу !!!
update_student_group(db, group_id, student_id)

# Создаем учебные предметы!!!
subject_1 = insert_subject(db, 'Математика и алгоритмы')
subject_2 = insert_subject(db, 'Литература SQL')

# Создаем занятие
lesson_1 = insert_lesson(db, 'Занятие по математике', subject_1)
lesson_2 = insert_lesson(db, 'Занятие по высшей математике', subject_1)
lesson_3 = insert_lesson(db, 'Занятие по SQL', subject_2)
lesson_4 = insert_lesson(db, 'Занятие по БД', subject_2)

# Добавляем оценки
mark_lesson_1 = insert_mark(db, 5, lesson_1, student_id)
mark_lesson_2 = insert_mark(db, 4, lesson_2, student_id)
mark_lesson_3 = insert_mark(db, 5, lesson_3, student_id)
mark_lesson_4 = insert_mark(db, 3, lesson_4, student_id)

# Все оценки студента (Получение только столбцов ФИО, оценки и предмета)
print(get_marks_student(db, student_id))

# Все оценки студента (Получение только столбцов ФИО, оценки и предмета)
print(get_books_student(db, student_id))

# Вся информация по студенту
print(get_info_student(db, student_id, student_id))

db.close()










