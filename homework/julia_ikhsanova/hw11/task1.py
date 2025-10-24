class Book:
    page_material = "бумага"
    has_text = True

    def __init__(self, title: str, author: str, pages: int, isbn, is_reserved: bool):
        self.title = title
        self.author = author
        self.pages = pages
        self.isbn = isbn
        self.is_reserved = is_reserved

    def print_book(self):
        book = f"Название: {self.title}, Автор: {self.author}, Страниц: {self.pages}, Материал: {self.page_material}"
        if self.is_reserved:
            print(book + ", Зарезервирована")
        else:
            print(book)


# first_book = Book("Идиот", "Достоевский", 10, 100, True)
# first_book.print_book()
# second_book = Book("Идиот", "Достоевский", 11, 200, False)
# second_book.print_book()
# third_book = Book("Идиот", "Достоевский", 12, 300, True)
# third_book.print_book()
# fourth_book = Book("Идиот", "Достоевский", 13, 400, False)
# fourth_book.print_book()
# fifth_book = Book("Идиот", "Достоевский", 13, 500, True)
# fifth_book.print_book()


class SchoolTextbooks(Book):
    def __init__(self, title, author, pages, isbn, is_reserved, subject, school_grade, has_exercises: bool):
        super().__init__(title, author, pages, isbn, is_reserved)
        self.subject = subject
        self.school_grade = school_grade
        self.has_exercises = has_exercises

    def print_Textbook(self):
        Textbook = (
            f"Название: {self.title}, Автор: {self.author}, "
            f"Страниц: {self.pages}, Предмет: {self.subject}, "
            f"Класс {self.school_grade}"
        )
        if self.is_reserved:
            print(Textbook + ", Зарезервирована")
        else:
            print(Textbook)

fifth_Textbook = SchoolTextbooks("Алгебра", "Иванов", 100, 11, True, "Математика", 11, True)
fifth_Textbook.print_Textbook()
second_Textbook = SchoolTextbooks("Всеобщая история", "Сидоров", 200, 12, False, "История", 10, False)
second_Textbook.print_Textbook()

