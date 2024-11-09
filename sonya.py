import sqlite3

def init_db():
        conn = sqlite3.connect('magazin.db')
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS magazin (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                fio TEXT UNIQUE NOT NULL,
                status TEXT NOT NULL
            )
        ''')
        conn.commit()
        conn.close()


def InsertUser(fio, status):
        conn = sqlite3.connect('magazin.db')
        cursor = conn.cursor()
        cursor.execute ('''INSERT INTO magazin (fio, status) 
                        VALUES (?,?)''',(fio, status))

        conn.commit()
        conn.close()

def update_user(id, fio, status):
    conn = sqlite3.connect('magazin.db')
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE magazin SET fio = ?, status = ?
        WHERE id = ?
    ''', (fio, status, id))
    conn.commit()
    conn.close() 
        
def delete_user(id):
    conn = sqlite3.connect('magazin.db')
    cursor = conn.cursor() 
    cursor.execute('DELETE FROM magazin WHERE id = ?', (id,))
    conn.commit()
    conn.close()

def get_user_by_id(id):
    conn = sqlite3.connect('magazin.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM magazin WHERE id = ?', (id,))
    user = cursor.fetchone()  
    conn.close()
    return user

if __name__ == '__main__':
    init_db()
    choice = input("Выберите функцию (update, delete, insert, get_user): ")

    if choice == "update":
            id = int(input("Введите id для обновления: "))
            fio = input("Введите ФИО: ")
            status = input("Введите должность: ")
            update_user(id, fio, status)

    elif choice == "delete":
        id = int(input("Введите id для удаления: "))
        delete_user(id)

    elif choice == "insert":
        fio = input("Введите ФИО: ")
        status = input("Введите должность: ")
        InsertUser(fio, status)

    elif choice == "get_user":
        id = int(input("Введите id для просмотра: "))
        user_data = get_user_by_id(id)  
        if user_data:
            print("Данные пользователя:")
            print(f"ID: {user_data[0]}")
            print(f"ФИО: {user_data[1]}")
            print(f"должность: {user_data[2]}")
        else:
            print(f"Пользователь с id {id} не найден.")

    else:
        print("Неверная функция.")