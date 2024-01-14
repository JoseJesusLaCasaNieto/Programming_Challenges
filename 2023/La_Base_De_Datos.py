# /*
#  * Realiza una conexión desde el lenguaje que hayas seleccionado a la siguiente
#   * base de datos MySQL:
#  * - Host: mysql-5707.dinaserver.com
#  * - Port: 3306
#  * - User: mouredev_read
#  * - Password: mouredev_pass
#  * - Database: moure_test
#  *
#  * Una vez realices la conexión, lanza la siguiente consulta e imprime el resultado:
#  * - SELECT * FROM `challenges`
#  *
#  * Se pueden usar librerías para realizar la lógica de conexión a la base de datos.
#  */

import mysql.connector

def connect_and_query():
    connection_config = {
        'host': 'mysql-5707.dinaserver.com',
        'port': 3306,
        'user': 'mouredev_read',
        'password': 'mouredev_pass',
        'database': 'moure_test'
    }

    try:
        connection = mysql.connector.connect(**connection_config)

        if connection.is_connected():
            print("Connection established")

            cursor = connection.cursor()

            query = "SELECT * FROM `challenges`"
            cursor.execute(query)

            results = cursor.fetchall()

            for result in results:
                print(result)

    except mysql.connector.Error as e:
        print(f"Connection error: {e}")
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()
            print("Connection closed")

connect_and_query()




