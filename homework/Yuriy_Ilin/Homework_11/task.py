class Book:
    material = 'бумага'
    text = True

    def __init__(self, title, author, count_pages, isbn, reserve=False):
        self.title = title
        self.author = author
        self.count_pages = count_pages
        self.isbn = isbn
        self.reserve = reserve

    def get_info(self):
        lst = [
            f"Название: {self.title}",
            f"Автор: {self.author}",
            f"страниц: {self.count_pages}",
            f"материал: {self.material}"
        ]
        if self.reserve:
            lst.append("зарезервирована")
        return ", ".join(lst)


book_1 = Book("Преступление и наказание", "Фёдор Достоевский", 200, 123224, True)
book_2 = Book("Мастер и Маргарита", "Михаил Булгаков", 300, 187722, False)
book_3 = Book("Война и мир", "Лев Толстой", 1200, 174532, False)
book_4 = Book("Капитанская дочка", "Александр Пушкин", 150, 489652, False)
book_5 = Book("Властелин колец", "Джон Р.Р. Толкин", 1470, 999845, False)

print(book_1.get_info())
print(book_2.get_info())
print(book_3.get_info())
print(book_4.get_info())
print(book_5.get_info())


class SchoolBook(Book):
    def __init__(self, title, author, count_pages, isbn, subject, number_group, reserve=False, tasks=False):
        super().__init__(title, author, count_pages, isbn, reserve)
        self.subject = subject
        self.number_group = number_group
        self.tasks = tasks

    def get_info(self):
        lst = [
            f"Название: {self.title}",
            f"Автор: {self.author}",
            f"страниц: {self.count_pages}",
            f"предмет: {self.subject}",
            f"класс: {self.number_group}"
        ]
        if self.reserve:
            lst.append("зарезервирована")
        return ", ".join(lst)


school_book1 = SchoolBook(
    "Алгебра",
    "Доставучий",
    200,
    127894,
    "Математика",
    9,
    reserve=True,
    tasks=True
)

school_book2 = SchoolBook(
    "Могучий и сложный",
    "Пупкин",
    300,
    859654,
    "Русский язык",
    7
)

print(school_book1.get_info())
print(school_book2.get_info())
