import sqlite3
#проверка бд есть ли юзер
def ref_prov(id_use):
    sqlite_connection = sqlite3.connect('bd/bd')
    cursor = sqlite_connection.cursor()
    sqlite_select_query = """SELECT * from users"""
    cursor.execute(sqlite_select_query)
    records = cursor.fetchall()
    for row in records:
        if row[0]==id_use:
            cursor.close()
            return True
    cursor.close()
    return False
#проверка есть ли юзер в бд



def db_table_val(user_id: int, user_name: str, user_surname: str, username: str):
    conn = sqlite3.connect('bd/bd', check_same_thread=False)
    cursor = conn.cursor() #курсор для бд
    cursor.execute('INSERT INTO users (user_id, user_name, user_surname, username) VALUES (?, ?, ?, ?)', (user_id, user_name, user_surname, username))
    conn.commit()
#запись нового юзера в бд


def from_bd(num: int, user_id: int):
    sqlite_connection = sqlite3.connect('bd/bd')
    cursor = sqlite_connection.cursor()
    sqlite_select_query = """SELECT * from users"""
    cursor.execute(sqlite_select_query)
    records = cursor.fetchall()
    for row in records:
        if row[0]==user_id:
            return row[num]
    cursor.close()
#забирает номер столбца бд кот нуден и пользователя возвращает значение заданнного столбца



def zamena_para(user_id: int, smena):
    sqlite_connection = sqlite3.connect('bd/bd')
    cursor = sqlite_connection.cursor()
    cursor.execute('UPDATE users SET para_id = ? WHERE user_id = ?', (smena, user_id))
    sqlite_connection.commit()
    sqlite_connection.close()
#подмена элемента