
import datetime # trabajar con fechas en mysql y python
import hashlib # cifrar password
import usuarios.conexion as conexion

# trayendo el metodo de conectar de la clase conexion 
connect = conexion.conectar()
database = connect[0]
cursor = connect[1]



class Usuario:
    # constructor
    def __init__(self, nombre, apellidos, email, password):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.password = password

    def registrar(self):
            fecha = datetime.datetime.now() # crear fecha actual.
            
            # cifrar password
            cifrado = hashlib.sha256()
            cifrado.update(self.password.encode('utf8'))

            # sentencia sql
            sql = "INSERT INTO usuarios VALUES(null, %s,%s,%s,%s,%s)"
            usuario = (self.nombre, self.apellidos, self.email, cifrado.hexdigest(), fecha)

            try:
                # registrar usuario en la bd
                cursor.execute(sql, usuario)
                # guardamos los cambios en la bd
                database.commit()
                # devolvemos una lista con el numero de filas afectadas y el propio objeto de la clase
                result = [cursor.rowcount, self]
            except:
                result = [0, self]
            
            return result

    def identificar(self):
        
        # consultar si existe el usuario
        sql = "SELECT * FROM usuarios WHERE email = %s AND password = %s "

        # cifrar password
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))

        # datos para la consulta 
        usuario = (self.email, cifrado.hexdigest())

        # enviar datos a la bbdd
        cursor.execute(sql, usuario)
        result = cursor.fetchone()

        return result