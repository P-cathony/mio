
import usuarios.conexion as conexion


# trayendo el metodo de conectar de la clase conexion 
connect = conexion.conectar()
database = connect[0]
cursor = connect[1]




class Nota:
    



    def __init__(self, usuario_id, titulo = " ", descripcion = " "):
        self.usuario_id = usuario_id
        self.titulo = titulo
        self.descripcion = descripcion
        

    def guardar(self):
        # sentencia sql
        sql = "INSERT INTO notas VALUES(null, %s, %s, %s, NOW())"
        nota = (self.usuario_id, self.titulo, self.descripcion)

        # registrar notas en la bd
        cursor.execute(sql, nota)
        database.commit()

        return [cursor.rowcount, self]


    def listar(self):
        # sentencia sql
        sql = f"SELECT * FROM notas WHERE usuario_id = { self.usuario_id }"
        
        # executar consulta
        cursor.execute(sql)
        result = cursor.fetchall()

        return result


    def eliminar(self):
        # sentencia sql
        sql = f"DELETE FROM notas WHERE usuario_id = { self.usuario_id } AND titulo LIKE '%{ self.titulo }%' "

        # executar consulta
        cursor.execute(sql)
        database.commit()

        return [cursor.rowcount, self]