from tkinter import * 

# crear la ventana raiz
ventana = Tk()




# cambiar tamaño en la ventana
ventana.geometry("700x500")
ventana.title("formularios en tkinter | toni")



encabezado = Label(ventana, text="Formularios")
encabezado.config(
    padx=5,
    pady=5,
    fg="white",
    bg="green",
    font=("Consolas, 20")
)
encabezado.grid(row=0, column=0, columnspan=5, sticky=W)


# boton check

web = IntVar()
movil = IntVar()


def mostrarProfesion():

    texto = ""


    if web.get():
        texto += "Desarrollo web "
    

    if movil.get():
        if web.get():
            texto += "y Desarrollo movil"
        else:
            texto += "Desarrollo movil"




    mostrar.config(
        text=texto, 
        fg="white", 
        bg="green"
        )




Label(ventana, text="¿A que te dedicas?" ).grid(row= 1, column= 0)


Checkbutton(
    ventana, 
    text= "Desarrollo web",
    variable= web,
    onvalue= 1, # cuando esta marcado.
    offvalue= 0, # cuando no esta marcado.
    command= mostrarProfesion
    ).grid(row= 2, column= 0)


Checkbutton(
    ventana, 
    text="Desarrollo movil",
    variable= movil,
    onvalue= 1, # cuando esta marcado.
    offvalue= 0, # cuando no esta marcado.
    command= mostrarProfesion
    ).grid(row= 3, column= 0)


mostrar = Label(ventana)
mostrar.grid(row=4, column=0)



# Radio buttons

def marcar():
    marcado.config(text= opcion.get())
    



opcion = StringVar()
# mantener Radiobutton vacio
opcion.set(None)

Label(ventana, text="¿Cual es tu género?").grid(row=5)

Radiobutton(
    ventana, 
    text="Masculino",
    value= "Masculino",
    variable= opcion,
    command= marcar
    ).grid(row=6)


Radiobutton(
    ventana, 
    text="Femenino",
    value= "femenino",
    variable= opcion,
    command= marcar
    ).grid(row=7)


# resultado de radio button
marcado = Label(ventana)
marcado.grid(row=8)


# Option Menu
def seleccionar():
    seleccionado.config(text= opcion.get())
    


opcion=StringVar()
opcion.set("Opcion 1")


Label(ventana, text="Selecciona una opcion").grid(row= 5, column= 1)


# lista desplegable
select = OptionMenu(ventana, opcion, "Opcion 1", "Opcion 2", "Opcion 3")
select.grid(row=6, column=1)


# boton
Button(ventana, text="Ver", command= seleccionar ).grid(row=7, column=1)


seleccionado = Label(ventana)
seleccionado.grid(row=8, column=1)




# arrancar la ventana y mostrar la ventana
ventana.mainloop()