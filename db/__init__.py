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
            INSERT INTO books (name, author, description, genre) VALUES ('{name}', '{author}', '{description}', '{genre}')
        """)
        self.connection.commit()


