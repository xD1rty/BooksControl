# Импорт всех нужных библиотек
import sqlite3

# Класс для взаимодействия и работы с базой данных SQLite
class Database:
    def __init__(self, name): # Инициализация класса Database
        self.connection = sqlite3.connect(name) # Создание соединения
        self.cursor = self.connection.cursor() # Создание курсора для выполнения SQL команд

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                author TEXT NOT NULL,
                description TEXT NOT NULL,
                genre TEXT NOT NULL
            )
        ''') # Создание таблицы базы данных (NOT EXISTS - метод, создающий таблицу если ее нет)
    
    def create_book(self, name, author, description, genre): # Функция создания книги в БД
        self.cursor.execute(f"""
            INSERT INTO books (name, author, description, genre) VALUES ('{name}', '{author}', '{description}', '{genre.lower().strip()}')
        """) # Созданеи книги в БД
        self.connection.commit() # Запись изменений

    def get_all_genres(self): # Получение всех имеющихся жанров
        genres = []
        self.cursor.execute('SELECT genre FROM books') # Команда для получения жанров
        _genres = self.cursor.fetchall() # Получение жанров
        for _g in _genres: # Цикл для избежания повторений
            if _g.lower() not in genres:
                genres.append(_g.lower())
        return genres # Возвращение жанров

    def get_all_books(self): # Получение всех книг
        books = []
        self.cursor.execute('SELECT id, name, author, genre FROM books') # Запрос на получение айди, имени, автора и жанра книги
        _books = self.cursor.fetchall() # Получение
        for _book in _books: # Перебор книг для beauty-вывода
            books.append(f"{_book[0]} | {_book[1]} | {_book[2]} | {_book[3]}")
        return books # Возвращение книг

    def get_book_by_id(self, id: int): # Получение книги по номеру (ID)
        self.cursor.execute(f'SELECT name, author, genre, description FROM books WHERE id={id}') # Запрос на получение данных
        name, author, genre, description = self.cursor.fetchone() # Получение одного элемента
        return f"""
Название: {name}
Автор: {author}
Жанр: {genre}
Описание: {description}""" # Возвращение готовой строчки

    def delete_book_by_id(self, id: int): # Удаление книги по ID
        self.cursor.execute(f"DELETE FROM books WHERE id={id}") # Запрос на удаление данных
        self.connection.commit() # Запись изменений

    def search_book_by_description(self, words): # Поиск книги по описанию
        books = []
        self.cursor.execute(f"SELECT * FROM books WHERE description LIKE '{words}'") # Запрос на получения данных
        _books = self.cursor.fetchall() # Получение данных
        for _book in books:
            books.append(f"""
Название: {_book[1]}
Автор: {_book[2]}
Жанр: {_book[4]}
Описание: {_book[3]}""")
        return books # Возвращение книг 

    def search_book_by_author(self, words): # Поиск книги по автору
        books = []
        self.cursor.execute(f"SELECT * FROM books WHERE author LIKE '{words}'") # Запрос на получение данных
        _books = self.cursor.fetchall() # Получение данных
        for _book in books: # Перебор книги для beauty-вывода
            books.append(f"""
Название: {_book[1]}
Автор: {_book[2]}
Жанр: {_book[4]}
Описание: {_book[3]}""")
        return books # Возвращение книг

