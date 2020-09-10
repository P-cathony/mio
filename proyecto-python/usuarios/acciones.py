# llamando el modelo de usuarios
import usuarios.usuarios as modelo
import notas.acciones  

class Acciones:

    def registro(self):
        print("\nOK!! vamos a registrarte en el sistema......")
        print()
        nombre = input("¿Cual es tu nombre?: ")
        apellidos = input("¿Cuales son tus apellidos?: ")
        email = input("Introduce tu email: ")
        password = input("Introduce tu contraseña: ")

        # crear objeto de tipo modelo
        usuario = modelo.Usuario(nombre,apellidos,email,password)
        
        # llamando el metodo registrar de usuario
        registro = usuario.registrar()

        if registro[0] >= 1:
            print("\nperfecto {} te has registrado con el email {}".format(registro[1].nombre, registro[1].email))
        else:
            print("\nNo te has registrado correctamente ")

            

    def login(self):
        print("\nValeee!! Identificate en el sistema ")
        
        try:

            email = input("Introduce tu email: ")
            password = input("Introduce tu contraseña: ")
            

            # validando el email y el password del modelo usuario 
            usuario = modelo.Usuario('', '', email, password)
            login = usuario.identificar() # llamando el metodo identificar de la class usuario.

            if email == login[3]:
                print("\nBienvenido señor@: {}, te has registrado en el sistema el {} ".format(login[1], login[5]))
                self.proximasAcciones(login)
                # repitela@uu.com   pass== 1234

        except Exception as e:
            # print(type(e))
            # print(type(e).__name__)
            print("Login incorrecto intentalo de nuevo ")


    def proximasAcciones(self, usuario):
        print("""

            Presiona alguna de las letras que esta encerrada().    

            Acciones disponibles:
            - crear nota - (C)
            - mostrar tus notas - (M)
            - Eliminar - (E)
            - Salir - (S)

        """)

        accion = input ("¿Que quieres hacer? ")
        hazEl = notas.acciones.Acciones()

        if accion == "c":
            hazEl.crear(usuario)
            self.proximasAcciones(usuario)

        elif accion == "m":
            hazEl.mostrar(usuario)
            self.proximasAcciones(usuario)
        
        elif accion == "e":
            hazEl.borrar(usuario)
            self.proximasAcciones(usuario)
        
        elif accion == "s":
            print("\nHasta luego señor usuario ")
            exit()
            