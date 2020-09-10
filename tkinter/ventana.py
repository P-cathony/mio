# tkinter
# modulo para crear interfaces graficas de usuario

from tkinter import *
import os.path

class Programa:
    def __init__(self):
        self.title = "Mi primer ventana"
        self.icon = './imagenes/logo.ico'
        self.icon_alt = './tkinter/imagenes/logo.ico'
        self.size = "750x450"
        self.resizable = "False "

    def cargar(self):
        # crear la ventana raiz
        ventana = Tk()
        self.ventana = ventana


        # cambiar el titulo a la ventana 
        ventana.title(self.title)



        # comprobar si un archivo existe
        ruta_icono = os.path.abspath(self.icon)

        if not  os.path.isfile(ruta_icono):
            ruta_icono = os.path.abspath(self.icon_alt)



        # icono de la ventana 
        ventana.iconbitmap(ruta_icono)


        # mostrar texto en la ventana
        texto = Label(ventana, text=ruta_icono)
        texto.pack()



        # cambiar tamaño en la ventana
        ventana.geometry('750x450')


        # bloquear tamaño de la ventana 
        if self.resizable:
            ventana.resizable(1, 1) # parametro izquierdo = horizontal parametro derecho vertical
        else:
            ventana.resizable(0, 0) # parametro izquierdo = horizontal parametro derecho vertical
       


    # arrancar la ventana y mostrar la ventana siempre de ultimo
    def mostrar(self):
        self.ventana.mainloop()

        
    
    # agregar texto
    def addTexto(self, dato):
        texto = Label(self.ventana, text = dato)
        texto.pack()



# instanciar clase programa 
programa = Programa()
programa.cargar()
programa.addTexto("Hola desde addtexto")
programa.mostrar()


######   NOTA      

# cambiar la extension del archivo py por pyw 
# para ponerlo en modo ventana y eliminar pantalla negra
