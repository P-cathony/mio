
import mysql.connector

def conectar():
    
    # Conexion base de datos
    database = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "",
        database = "master_python",
        port = 3306

    )

    # Crear cursor para ejecutar cosultas a BBDD
    cursor = database.cursor(buffered=True)

    return [database, cursor]