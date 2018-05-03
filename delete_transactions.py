import mysql.connector

querystring = """
    DELETE FROM Encounter
"""

try:
    connection = mysql.connector.connect(host='localhost',
        port=3307,
        database='raw_shr',
        user='root',
        password='password')
    if connection.is_connected():
        print('Connected to MySQL database')
    
    cursor = connection.cursor()
    cursor.execute(querystring)
    connection.commit()

except Error as e:
    print(e)

finally:
    connection.close()
    print('Connection closed.')