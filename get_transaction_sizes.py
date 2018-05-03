import mysql.connector

querystring = """
    SELECT (LENGTH(encounter_id) + IFNULL(LENGTH(patient_id), 0) + IFNULL(LENGTH(contents), 0)) as size
    FROM Encounter
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
    rows = cursor.fetchall()

    transaction_sizes = [int(txn[0]) for txn in rows]

    with open('transaction_sizes_abe.txt', 'w') as txn_sizes_file:
        txn_sizes_file.writelines(["{}\n".format(txn_size) for txn_size in transaction_sizes])

except Error as e:
    print(e)

finally:
    connection.close()
    print('Connection closed.')