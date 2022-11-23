import sqlite3 as sql


def register(name, surname, email, password):
    connection = sql.connet('registration.db')
    cursor = sql.Cursor()
    cursor.execute("INSERT INTO users VALUES (?,?,?,?)", [name, surname, email, password])
    connection.commit()
    connection.close()

