from tkinter import * 
from PIL import Image,ImageTk

# crear la ventana raiz
ventana = Tk()


# cambiar tamaño en la ventana
ventana.geometry("700x500")
# ventana.config(bg="white") # cambiar el color del fondo de ventana.



# cargar una imagen en ventana
# para las imagenes instalar pillow qu se hace con pip install --upgrade pillow
# importar Image, ImageTk para trabajar con imagenes.
imagen = Image.open('./imagenes/DN.jpg')
render = ImageTk.PhotoImage(imagen)

# tenemos que pasar por un label la imagen renderizada.
imagen = Label(ventana, image=render)
imagen.pack()



# arrancar la ventana y mostrar la ventana
ventana.mainloop()