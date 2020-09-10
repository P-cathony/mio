from tkinter import * 
from tkinter import messagebox as messagebox

# crear la ventana raiz
ventana = Tk()




# cambiar tamaño en la ventana
ventana.geometry("700x500")
ventana.title("Alertas en tkinter | toni")




# Alerta normal         cada alerta tiene su boton
def sacarAlerta():
    messagebox.showinfo("Alerta", "hola todo va bien") # "showwarning"  "showerror"  "askquiestion--- preguntar si quiere salir"

# boton
Label(ventana).grid(row=2, column=1) # espacios 
boton = Button(ventana, text="Mostrar alerta", command=sacarAlerta)
boton.grid(row=3, column=1, sticky=W)

# configuracion del boton
boton.config(
    padx=5,
    pady=5, 
    bg="green", 
    fg="white"
    )#




# Alerta normal askquestion
def salir(nombre):
    resultado = messagebox.askquestion("Salir", "¿Seguro quieres salir?") # "showwarning"  "showerror"  "askquiestion--- preguntar si quiere salir"
    
    if resultado == "yes":
        messagebox.showinfo("hasta luego", "Que este muy bien señor@ {}".format(nombre)) 
        ventana.destroy()


# boton
Label(ventana).grid(row=4, column=1) # espacios 
boton = Button(ventana, text="   salir   ", command= lambda : salir("toni"))
boton.grid(row=5, column=1, sticky=W)

# configuracion del boton
boton.config(
    padx=10,
    pady=10, 
    bg="red", 
    fg="white"
    )#






# arrancar la ventana y mostrar la ventana
ventana.mainloop()