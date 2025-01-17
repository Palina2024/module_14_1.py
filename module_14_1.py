import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')
# Заполняем БД 10 записями:
# for i in range(1, 11):
#     cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)', (f'user{i}', f'example{i}@gmail.com', i * 10, 1000))

# Обновляем balance у каждой 2ой записи начиная с 1ой на 500:
# cursor.execute('UPDATE Users SET balance = balance - 500 WHERE id IN (1, 3, 5, 7, 9)')

# Удаляем каждую 3ую запись в таблице начиная с 1ой:
# cursor.execute('DELETE FROM Users WHERE id IN (1, 4, 7, 10)')

# Сделаем выборку всех записей при помощи fetchall(), где возраст не равен 60:
cursor.execute('SELECT username, email, age, balance FROM Users WHERE age != 60')
users = cursor.fetchall()
for user in users:
    username, email, age, balance = user
    print(f'Имя: {username} | Почта: {email} | Возраст: {age} | Баланс: {balance}')

connection.commit()
connection.close()