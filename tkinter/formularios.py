
from tkinter import * 

# crear la ventana raiz
ventana = Tk()




# cambiar tamaño en la ventana
ventana.geometry("700x500")
ventana.title("formularios en tkinter | toni")




# texto encabezado
encabezado = Label(ventana, text="Formularios tkinter")
# configuracion del encabezado.
encabezado.config(

    fg = "white",
    bg = "darkgray",
    font = ("Open sans", 18),
    padx = 10, # espacio entre letra y margen X
    pady = 10  # espacio entre letra y margen Y

)
encabezado.grid(row=0, column=0, columnspan=6, sticky=E) # grid y pack no son compatibles por lo que saca 
                                          # error se debe de tener pack o grid.
                                          # sticky quiere decir pega y funciona con las misma cordenadas 
                                          # de la imagen de posiciones.
                                          # al metodo grid se le debe de pasar el numero de fila y columna
                                          # en la que queremos posicionar el texto.






# label para el campo (nombre)
label = Label(ventana, text="Nombre")
label.grid(row=1, column=0, padx=5 , sticky=W, pady=5)

# campo de texto (nombre)
campo_texto = Entry(ventana)  # Entry se puede cargar dentro de Frame o cualquier cosa.
# empaquetando en un grid
campo_texto.grid(row=1, column=1, sticky=W, padx=5, pady=5)




# label para el campo (Apellidos)
label = Label(ventana, text="Apellidos")
label.grid(row=2, column=0, padx=5 , sticky=W, pady=5)

# campo de texto (Apellidos)
campo_texto = Entry(ventana)  # Entry se puede cargar dentro de Frame o cualquier cosa.
# empaquetando en un grid
campo_texto.grid(row=2, column=1, sticky=W, padx=5, pady=5)
# configuracion campo texto
campo_texto.config(justify="left", state="normal") # que el texto salga por la derecha o izquierda y que este o no habilitado.




# label para el campo (Descripcion)
label = Label(ventana, text="Descripcion")
label.grid(row=3, column=0, padx=5 , sticky=NW, pady=5)

# campo de texto Grande (Descripcion)
campo_grande = Text(ventana)  # El campo text crea un campo de gran dimension.
# empaquetando en un grid
campo_grande.grid(row=3, column=1, sticky=W, padx=5, pady=5)
# configuracion campo texto Grande
campo_grande.config(
    width=30, 
    height=5, 
    font=("Arial", 12), 
    padx=5, 
    pady=5, 
    ) # 



# boton
Label(ventana).grid(row=4, column=1) # espacios 
boton = Button(ventana, text="Enviar")
boton.grid(row=5, column=1, sticky=W)

# configuracion del boton
boton.config(
    padx=5,
    pady=5, 
    bg="green", 
    fg="white"
    )#






# arrancar la ventana y mostrar la ventana
ventana.mainloop()