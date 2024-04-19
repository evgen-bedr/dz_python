import mysql.connector

import const


def get_connection():
    connection = None
    try:
        connection = mysql.connector.connect(**const.dbconfig)
        print('Соединение с БД прошло успешно')
    except mysql.connector.Error as e:
        print(f'Ошибка соединения: \'{e}\'\nРабота программы завершена')
    return connection


def execute_query(connection, query):
    result = None
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        result = cursor.fetchall()
    except mysql.connector.Error as e:
        print(f'Ошибка: \'{e}\' в запросе: {query}')
    finally:
        cursor.close()
    return result
