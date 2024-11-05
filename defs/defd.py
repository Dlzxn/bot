import sqlite3
#проверка бд есть ли юзер
def ref_prov(id_use):
    sqlite_connection = sqlite3.connect('bd/bd')
    cursor = sqlite_connection.cursor()
    print("Подключен к SQLite")
    sqlite_select_query = """SELECT * from users"""
    cursor.execute(sqlite_select_query)
    records = cursor.fetchall()
    for row in records:
        if row[0]==id_use:
            cursor.close()
            return True
    cursor.close()
    return False
def db_table_val(user_id: int, user_name: str, user_surname: str, username: str):
    conn = sqlite3.connect('bd/bd', check_same_thread=False)
    cursor = conn.cursor() #курсор для бд
    cursor.execute('INSERT INTO users (user_id, user_name, user_surname, username) VALUES (?, ?, ?, ?)', (user_id, user_name, user_surname, username))
    conn.commit()