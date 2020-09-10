
import notas.nota as modelo



class Acciones:

    def crear(self, usuario):
        print("ok {} !! vamos a crear una nueva nota..... ".format(usuario[1]))
        titulo = input("\nIntroduce el titulo de tu nota: ")
        descripcion = input("\nMete el contenido de tu nota: ")
    
        # Instanciando el modelo que se encuentra en el fichero nota.py
        nota = modelo.Nota(usuario[0], titulo, descripcion)
        guardar = nota.guardar() # llamando metodo guardar de la class Nota.

        if guardar[0] >=1:
            print("\nperfecto has guardado la nota: {}".format(nota.titulo))
        
        else:
            print("\n No se ha guardado la nota, lo siento señor@ {} ".format(usuario[1]))


    def mostrar(self, usuario):
        print("\nVale {} !! Aquí tiene tus notas: \n".format(usuario[1]))

        # crear objeto para sacar listado
        nota = modelo.Nota(usuario[0])
        notas = nota.listar()

        for nota in notas:
            print("\n**************************************")
            print(nota[2])
            print(nota[3])
            print(nota[4])
            print("\n**************************************")

    def borrar (self,usuario):
        print("\n Ok {} vamos a borrar notas ".format(usuario[1]))

        titulo = input("Introduce el titulo de la nota a borrar: ")

        nota = modelo.Nota(usuario[0], titulo)
        eliminar = nota.eliminar()

        if eliminar[0] >= 1:
            print("Hemos borrado la nota: {} ".format(nota.titulo))
        else:
            print("No se ha borrado la nota, prueba de nuevo......")

