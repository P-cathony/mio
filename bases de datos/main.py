import mysql.connector 

# Conexión
database = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="master_python"

)

# print(database)

# interactuar con la base de datos crear consultas a traves del metodo execute().
cursor = database.cursor()

"""
# crear base de datos
cursor.execute("CREATE DATABASE IF NOT EXISTS master_python")

# Observar bases de datos
cursor.execute("SHOW DATABASES")

for bd in cursor:
    print(bd)
"""

# crear tablas
cursor.execute("""
CREATE TABLE IF NOT EXISTS vehiculos(
    id int(10) auto_increment not null,
    marca varchar(40) not null,
    modelo varchar(40) not null,
    precio float(10,2) not null,
    CONSTRAINT pk_vehiculo PRIMARY KEY(id)
)


""")

# Observar tablas
cursor.execute("SHOW TABLES")

for tb in cursor:
    print(tb)

# insertar datos en las tablas
# cursor.execute("INSERT INTO vehiculos VALUES(null,'Chevrolet','2020',50000)")


# insertar varios datos ala vez
autos = [
    ('renault','clio',15000),
    ('renault','sandero',18000),
    ('mazda','6',20000),
    ('chevrolet','spark gt',15000)
    
]

# cursor.executemany("INSERT INTO vehiculos VALUES(null,%s,%s,%s)",autos)

# guardar cambios en la base de datos
database.commit()

# mostrar datos de una tabla
cursor.execute("SELECT * FROM vehiculos")

# sacar los datos de cursor para trabajar en python.
result = cursor.fetchall() # tambien se puede utilizar fetchone() sacamos el primer dato de la tabla.

print("****todos los coches****")
for coche in result:
    print(coche)
    # print(coche[1], coche[3]) #interactuamos con las tablas como si fueran tublas.


# eliminar datos de una tabla
# cursor.execute("DELETE FROM vehiculos WHERE id = 5")

# eliminar varios datos de una tabla
# cursor.execute("DELETE FROM vehiculos WHERE marca = 'mazda'")

# guardar cambios en la base de datos
database.commit()

print()
# mostrar en terminal objetos borrados
print(cursor.rowcount, "Eliminados!!")


# actualizar datos de una tabla
cursor.execute("UPDATE vehiculos SET modelo='ferrari' where marca='chevrolet' ")
# guardar cambios en la base de datos
database.commit()


print()
print("****todos los coches****")
for coche in result:
    # print(coche)
    print(coche[0], coche[1], coche[2], coche[3]) #interactuamos con las tablas como si fueran tublas.
