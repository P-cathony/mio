from tkinter import * 

# crear la ventana raiz
ventana = Tk()

# cambiar tamaño en la ventana
ventana.geometry("700x500")
ventana.title(" recoger datos de formularios en tkinter | toni")

# configuracion de la ventana
ventana.config(
    bd=50 
    )




# metodo para recoger valor de dato
def getdato():
    resultado.set(dato.get())

    # si en resultado hay un valor lo resalta verde.
    if len(resultado.get()) >= 1:
        texto_recibido.config(
        bg = "green",
        fg = "white"
        )

# asignar a la variable lo que esta en el campo del formulario.
dato = StringVar()
resultado = StringVar()

# textvariable es lo que estamos recogiendo en la variable dato y resultado desde el formulario
Label(ventana, text="Ingresa texto").grid(row=1, column=0, sticky=NW)
campo = Entry(ventana, textvariable=dato)
campo.grid(row=2, column=0)





Label(ventana, text="dato recibido").grid(row=4, column=0, sticky=NW)
# donde recibimos el resultado 
texto_recibido = Label(ventana, textvariable=resultado)
texto_recibido.grid(row=5, column=0, sticky=NW)










# boton

Label(ventana).grid(row=6, column=0) # espacios 
# Label(ventana).grid(row=6, column=0) # espacios 
boton = Button(ventana, text="Enviar", command=getdato)
boton.grid(row=7, column=0, sticky=NW)

# configuracion del boton
boton.config(
    padx=5,
    pady=5, 
    bg="green", 
    fg="white"
    )#








# arrancar la ventana y mostrar la ventana
ventana.mainloop()