-- Создание студента (изначально без группы)
INSERT INTO students (name, second_name) VALUES ('Yuriy', 'Doronin');

-- Создание книг
INSERT INTO books (title, taken_by_student_id)
VALUES 
	('Happy Python', 20855),
	('Automation for QA', 20855),
	(N'Идиот', 20855);
	
-- Создание группы
INSERT INTO "groups" (title, start_date, end_date) VALUES ('AQA School', 'Jan 2025', 'Dec 2025');

-- Добавление студента в группу
UPDATE students SET group_id = 5464 WHERE id = 20855;

-- Создание учебных предметов
INSERT INTO subjects (title)
VALUES 
	('Python Programming'),
	('Git & Repositories'),
	('SQL for everyone');

-- Создание занятий
INSERT INTO lessons (title, subject_id)
VALUES 
	('Base Python', 11591),
	('Advanced Python', 11591),
	('Git for begginers', 11592),
	('GITarist', 11592),
	('SQL Base+', 11593),
	('Bid Data', 11593);

-- Добавление оценкок
INSERT INTO marks (value, lesson_id, student_id)
VALUES 
	(5, 11630, 20855),
	(4, 11631, 20855),
	(4, 11632, 20855),
	(5, 11633, 20855),
	(5, 11634, 20855),
	(3, 11635, 20855);

-- Все оценки студента (Получение только столбцов ФИО, оценки и предмета)
SELECT DISTINCT s.name, s.second_name, m.value, l.title 
FROM students s LEFT JOIN marks m ON m.student_id = s.id
LEFT JOIN lessons l ON l.id = m.lesson_id
WHERE s.id = 20855;

-- Книги, находящиеся у студента
SELECT s.name, s.second_name, b.title 
FROM students s JOIN books b ON s.id = b.taken_by_student_id
WHERE s.id = 20855;

-- Все о студенте (повозился с дубликатами из-за книг, пока не узнал, что есть такая штука как GROUP_CONCAT)
SELECT DISTINCT
	s.id AS 'Id student', s.name, s.second_name,
	g.id AS 'Id group', g.title AS 'title group', g.start_date, g.end_date,
	l.title AS 'title lesson',
	sub.title AS 'title subject',
	m.value,
	(SELECT GROUP_CONCAT(title SEPARATOR ', ') FROM books WHERE taken_by_student_id = 20855) AS books
FROM students s
LEFT JOIN "groups" g ON s.group_id  = g.id
LEFT JOIN marks m ON m.student_id  = s.id
LEFT JOIN lessons l ON m.lesson_id = l.id
LEFT JOIN subjects sub ON l.subject_id = sub.id
WHERE s.id = 20855;
