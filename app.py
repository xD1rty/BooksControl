"""
ДЛЯ ЗАПУСКА ТРЕБУЕТСЯ ПРОСТО ВВЕСТИ
python3 app.py 

И все заработает
"""


from db import Database

db = Database("test.db")

print("""
BooksControl - управляй книгами просто!!!

Управление:
1. Получить все книги
2. Получить полное описание книги по номеру
3. Удалить книгу
4. Найти книгу по автору
5. Найти книгу по описанию
6. Добавить новую книгу

""")

while True:
    _req = int(input("Введите ваш запрос >>> ")) 
    if _req == 1:
        for book in db.get_all_books():
            print(book)
            print("---")
    elif _req == 2:
        for book in db.get_all_books():
            print(book)
            print("---")
        id = int(input("Введите номер книги >>> "))
        print(db.get_book_by_id(id))
    elif _req == 3:
        for book in db.get_all_books():
            print(book)
            print("---")
        id = int(input("Введите номер книги >>> "))
        db.delete_book_by_id(id)
        print("Удалено.\n")
    elif _req == 4:
        words = input("Введите автора >>> ")
        for book in db.search_book_by_author(words):
            print(book)
            print("---")
    elif _req == 5:
        words = input("Введите описание >>> ")
        for book in db.search_book_by_description(words):
            print(book)
            print("---")
    elif _req == 6:
        name = input("Введите название книги >>> ")
        author = input("Введите автора книги >>> ")
        genre = input(f"Вот примеры жанров: {db.get_all_genres()}\nВведите жанр книги >>> ")
        description = input("Введите описание книги >>> ")
        db.create_book(name, author, description, genre)
        for book in db.get_all_books():
            print(book)
            print("---")
    else:
        print("Введите корректную команду!!")

