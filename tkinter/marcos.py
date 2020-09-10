from tkinter import * 

# crear la ventana raiz
ventana = Tk()
ventana.title("Marcos | python")
# cambiar tamaño en la ventana
ventana.geometry("700x600")




# creando marco padre
marco_padre = Frame(ventana, width=250, height=250)

# configurando marco
# marco_padre.config(
    # bg="lightblue",
    # bd=5,
    # relief = "raised" # en el relief se pueden usar las sgtes opciones: "flat" "groove" "raised" "ridge" "solid" "sunken"
    # )

# Empaquetar marco siempre se debe de hacer igual que con texto
marco_padre.pack(side=BOTTOM, anchor=S, fill=X, expand=YES)





# creando marco
marco = Frame(marco_padre, width=250, height=250)

# configurando marco
marco.config(
    bg="red",
    bd=5,
    relief = "raised" # en el relief se pueden usar las sgtes opciones: "flat" "groove" "raised" "ridge" "solid" "sunken"
    )

# Empaquetar marco siempre se debe de hacer igual que con texto
marco.pack(side=LEFT, anchor=SW)

# evitar que se contraiga el marco 
marco.pack_propagate(False)

# meter texto dentro de un Frame (cuadro)
texto = Label(marco, text="Primer marco")


# configurar texto dentro del marco 
texto.config(
    bg = "red",
    fg = "white",
    font = ("Arial", 20),
    # height = 4,
    # width = 10,
    # bd = 3,
    # relief = SOLID,

)
texto.pack(anchor = CENTER, fill= Y, expand=YES)   # recibe side=LEFT, anchor=CENTER





# creando marco
marco = Frame(marco_padre, width=250, height=250)

# configurando marco
marco.config(
    bg="green",
    bd=5,
    relief = "raised" # en el relief se pueden usar las sgtes opciones: "flat" "groove" "raised" "ridge" "solid" "sunken"
    )

# Empaquetar marco siempre se debe de hacer igual que con texto
marco.pack(side=RIGHT, anchor=SE)








# creando marco padre
marco_padre = Frame(ventana, width=250, height=250)

# configurando marco padre
# marco_padre.config(
    # bg="lightblue",
    # bd=5,
    # relief = "raised" # en el relief se pueden usar las sgtes opciones: "flat" "groove" "raised" "ridge" "solid" "sunken"
    # )

# Empaquetar marco siempre se debe de hacer igual que con texto
marco_padre.pack(side=TOP, anchor=N, fill=X, expand=YES)






# creando marco
marco = Frame(marco_padre, width=250, height=250)

# configurando marco
marco.config(
    bg="blue",
    bd=5,
    relief = "raised" # en el relief se pueden usar las sgtes opciones: "flat" "groove" "raised" "ridge" "solid" "sunken"
    )

# Empaquetar marco siempre se debe de hacer igual que con texto
marco.pack(side=LEFT)






# creando marco
marco = Frame(marco_padre, width=250, height=250)

# configurando marco
marco.config(
    bg="orange",
    bd=5,
    relief = "raised" # en el relief se pueden usar las sgtes opciones: "flat" "groove" "raised" "ridge" "solid" "sunken"
    )

# Empaquetar marco siempre se debe de hacer igual que con texto
marco.pack(side=RIGHT)




# arrancar la ventana y mostrar la ventana
ventana.mainloop()

