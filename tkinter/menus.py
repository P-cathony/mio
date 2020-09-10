from tkinter import * 

# crear la ventana raiz
ventana = Tk()


# cambiar tamaño en la ventana
ventana.geometry("700x500")
ventana.title("menú en tkinter | toni")




# menú
mi_menu = Menu(ventana)
ventana.config(menu=mi_menu)

# Submenu de Archivo
archivo = Menu(mi_menu, tearoff=0)
archivo.add_command(label="Archivo Nuevo")
archivo.add_command(label="Nueva Ventana")
archivo.add_separator()
archivo.add_command(label="Abrir Archivo")
archivo.add_command(label="Abrir Carpeta")
archivo.add_separator()
archivo.add_command(label="salir", command=ventana.quit)


# menu Archivo
mi_menu.add_cascade(label="Archivo", menu=archivo)
# menu Editar
mi_menu.add_command(label="Editar")
# menu Seleccion
mi_menu.add_command(label="Seleccion")










# arrancar la ventana y mostrar la ventana
ventana.mainloop()