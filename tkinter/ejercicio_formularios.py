from tkinter import * 
from tkinter import messagebox as messagebox
from PIL import Image,ImageTk


# crear la ventana raiz
ventana = Tk()




# cambiar tamaño en la ventana
ventana.geometry("400x115")
ventana.title("Ejercicio en tkinter | toni")
ventana.config(bg="black")




numero1 = StringVar()
numero2 = StringVar()
resultado = StringVar()



# convertir a float
def cFLoat(numero):
    try:
        result = float(numero)
    except:
        result = 0
        messagebox.showinfo("Error", "Introduce bien los datos")
        numero1.set("")
        numero2.set("")
    return result



# metodos de los botones
def sumar():
    try:
        resultado.set(cFLoat(numero1.get()) + cFLoat(numero2.get()) )
        mostrarResultado()
    except:
        messagebox.showinfo("Error", "Introduce bien los datos")
        numero1.set("")
        numero2.set("")


def restar():
    resultado.set(cFLoat(numero1.get()) - cFLoat(numero2.get()) )
    mostrarResultado()


def multiplicar():
    resultado.set(cFLoat(numero1.get()) * cFLoat(numero2.get()) )
    mostrarResultado()


def dividir():
    resultado.set(cFLoat(numero1.get()) / cFLoat(numero2.get()) )
    mostrarResultado()




# metodo mostrar resultado
def mostrarResultado():
    messagebox.showinfo("Resultado", "El resultado de la operacion es: {}".format(resultado.get()))
    numero1.set("")
    numero2.set("")



# Frame para meter el formulario
marco = Frame(ventana, width=300, height=200)
# configuracion del marco
marco.config(
    bd= 2,
    relief= SOLID,
    padx= 5,
    pady= 5

)
marco.pack(side=TOP, anchor=CENTER)
marco.pack_propagate(False)



# cargar una imagen en ventana
imagen = Image.open('./tkinter/imagenes/DN.jpg')
render = ImageTk.PhotoImage(imagen)

# tenemos que pasar por un label la imagen renderizada.
imagen = Label(marco, image=render)
imagen.pack()




# label para el campo (numero1)
label = Label(marco, text="primer numero")
label.grid(row=1, column=0, padx=5 , sticky=W, pady=5)

# campo de texto (numero1)
campo_texto = Entry(marco, textvariable=numero1, justify="center")  # Entry se puede cargar dentro de Frame o cualquier cosa.
# empaquetando en un grid
campo_texto.grid(row=1, column=1, sticky=W, padx=5, pady=5)




# label para el campo (numero2)
label = Label(marco, text="segundo numero")
label.grid(row=2, column=0, padx=5 , sticky=W, pady=5)

# campo de texto (numero2)
campo_texto = Entry(marco, textvariable=numero2, justify="center")  # Entry se puede cargar dentro de Frame o cualquier cosa.
# empaquetando en un grid
campo_texto.grid(row=2, column=1, sticky=W, padx=5, pady=5)




# # label para el campo (resultado)
# label = Label(marco, text="resultado")
# label.grid(row=3, column=0, padx=5 , sticky=W, pady=5)

# # campo de texto (resultado)
# campo_texto = Entry(marco, textvariable=resultado)  # Entry se puede cargar dentro de Frame o cualquier cosa.
# # empaquetando en un grid
# campo_texto.grid(row=3, column=1, sticky=W, padx=5, pady=5)





# boton (Sumar)
# Label(marco).grid(row=4) # espacios 

boton = Button(marco, text="Sumar", command=sumar)
boton.grid(row=5, column=0, sticky=W+E)

# configuracion del boton
boton.config(
    padx=5,
    pady=5, 
    bg="green", 
    fg="white"
    )#






# boton (Restar)
# Label(ventana).grid(row=4, column=1) # espacios 
boton = Button(marco, text="Restar", command=restar)
boton.grid(row=5, column=1, sticky=W+E)

# configuracion del boton
boton.config(
    padx=5,
    pady=5, 
    bg="green", 
    fg="white"
    )#





# boton (Multiplicar)
# Label(ventana).grid(row=4, column=1) # espacios 
boton = Button(marco, text="Multiplicar", command=multiplicar)
boton.grid(row=5, column=2, sticky=W+E)

# configuracion del boton
boton.config(
    padx=5,
    pady=5, 
    bg="green", 
    fg="white"
    )#





# boton (Dividir)
# Label(ventana).grid(row=4, column=1) # espacios 
boton = Button(marco, text="Dividir", command=dividir)
boton.grid(row=5, column=3, sticky=W+E)

# configuracion del boton
boton.config(
    padx=5,
    pady=5, 
    bg="green", 
    fg="white"
    )#





# arrancar la ventana y mostrar la ventana
ventana.mainloop()