# import sqlite3

# class DB_Controller:
#     conn: sqlite3.Connection
#     cursor: sqlite3.Cursor

#     def __init__(self, db_name) -> None:
#         self.db_name = db_name
    
#     def open(self):
#         self.conn = sqlite3.connect(self.db_name, check_same_thread=False)
#         self.cursor = self.conn.cursor()

#     def close(self):
#         self.cursor.close()
#         self.conn.close()
    
#     def init_table(self):
#         self.open()
#         self.cursor.execute(
#             '''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, 
#             first_name TEXT, last_name TEXT, date TEXT)''')
#         self.close()

#     def get_data(self):
#         self.open()
#         self.cursor.execute(
#             '''SELECT * FROM users'''
#             )
#         data = self.cursor.fetchall()
#         self.close()
#         return data
    
#     def add_data(self, obj):
#         self.open()
#         self.cursor.execute('''INSERT INTO users (first_name, last_name, date) VALUES (?, ?, ?)''', (obj['first_name'], obj['last_name'], obj['date']))
#         self.conn.commit()
#         self.close()
import sqlite3

class DB_Controller:
    conn: sqlite3.Connection
    cursor: sqlite3.Cursor
    db_name: str

    def __init__(self, db_name) -> None:
        self.db_name = db_name
    
    def open(self):
        self.conn = sqlite3.connect(self.db_name, check_same_thread=False)
        self.cursor = self.conn.cursor()

    def close(self):
        self.cursor.close()
        self.conn.close()

    def init_table(self):
        self.open()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS patient (id INTEGER PRIMARY KEY, 
                            age STRING(3), sex STRING(10), race STRING(8), weight STRING(3), name STRING(30), img TEXT)''')
        self.close()
    
    def add_data(self, info):
        self.open()
        self.cursor.execute('''INSERT INTO patient (age, sex, race, weight, name, img) 
                            VALUES (?, ?, ?, ?, ?, ?)''', info)
        self.conn.commit()
        self.close()

    def get_data(self):
        self.open()
        self.cursor.execute('''SELECT id, age, sex, race, name, weight, img FROM patient''')
        data = self.cursor.fetchall()
        return data
    
    def delete_record(record_id):
        try:
        # Подключение к базе данных
            conn = sqlite3.connect('your_database.db')
            cursor = conn.cursor()

        # SQL-запрос для удаления записи по id
            sql_query = "DELETE FROM your_table WHERE id = ?"

        # Выполнение запроса
            cursor.execute(sql_query, (record_id,))

        # Подтверждение изменений
            conn.commit()
            print(f"Запись с id {record_id} успешно удалена.")
        except sqlite3.Error as error:
            print(f"Ошибка при удалении записи: {error}")
        finally:
        # Закрытие соединения
            if conn:
                conn.close()
                
    class DatabaseController:
        # Пример метода для удаления данных
        def delete_data(self, row_id):
            query = "DELETE FROM table_name WHERE id = %s"
            self.cursor.execute(query, (row_id,))
            self.conn.commit()
            

# Пример использования
db = DB_Controller('main.db')
db.init_table()