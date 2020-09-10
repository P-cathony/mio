from tkinter import * 

# crear la ventana raiz
ventana = Tk()


# cambiar tamaño en la ventana
ventana.geometry("500x300")
ventana.config(bg="blue") # cambiar el color del fondo de ventana.

# Ingresar texto en la ventana 
texto = Label(ventana, text="Bienvenido a mi programa")

# configurar texto de la ventana, adminte colores hexadecimales.
texto.config(
    fg="white", # color fuente
    bg="black", # background
    padx=40, # margen horizontal
    pady=20, # margen vertical
    font=("Arial", 30) # tipo de fuente y tamaño.
    )

# Empaquetar texto 
texto.pack(fill=X)

# Ingresar texto en la ventana 
texto = Label(ventana, text="Este es otro texto del programa")
# configuracion del texto de vcentana
texto.config( 
    # justify="right", # justificar fuente
    # width=400, # cambia ancho de cuadro 
    height=3, # cambia altura de cuadro 
    bg="orange", # cambiar color de cuadro.
    font=("Arial", 18), # tipo de fuente y tamaño.
    padx=10, # margen horizontal
    pady=20, # margen vertical
    cursor="pirate" # cambiar forma del cursor. "arrow" "circle" "clock" "cross" "dotbox" "exchange" "fleur" "heart" "heart" "man" "mouse" "pirate" "plus" "shuttle" "sizing" "spider" "spraycan" "star" "target" "tcross" "trek" "watch"
    )

# Empaquetar texto 
texto.pack(side=TOP, fill=X ) #
# fill=X, expand=YES 



# parametro de palabra clave, sirven para evitar orden en parametros.
# def prueba(nombre, apellidos, pais):
#     return "hola {} {} veo que eres de {}".format(nombre,apellidos,pais)


# Ingresar texto en la ventana 
texto = Label(ventana, text= "basico")
# configuracion del texto de vcentana
texto.config( 
    # justify="left", # justificar fuente
    # width=20, # cambia ancho de cuadro 
    height=3, # cambia altura de cuadro 
    bg="green", # cambiar color de cuadro tambien colores hexadecimales.
    font=("Arial", 18), # tipo de fuente y tamaño.
    padx=10, # margen horizontal
    pady=20, # margen vertical
    cursor="pirate" # cambiar forma del cursor. "arrow" "circle" "clock" "cross" "dotbox" "exchange" "fleur" "heart" "heart" "man" "mouse" "pirate" "plus" "shuttle" "sizing" "spider" "spraycan" "star" "target" "tcross" "trek" "watch"
    )

# Empaquetar texto 
texto.pack(side=LEFT, fill=X, expand=YES ) # el movimiento del texto dentro del pack pero 
                     # los estilos como tal dentro del config.
                     # observar la imagen que hay en imagenes.



# Ingresar texto en la ventana 
texto = Label(ventana, text= "otro texto")
# configuracion del texto de vcentana
texto.config( 
    # justify="left", # justificar fuente
    # width=20, # cambia ancho de cuadro 
    height=3, # cambia altura de cuadro 
    bg="yellow", # cambiar color de cuadro tambien colores hexadecimales.
    font=("Arial", 18), # tipo de fuente y tamaño.
    padx=10, # margen horizontal
    pady=20, # margen vertical
    cursor="pirate" # cambiar forma del cursor. "arrow" "circle" "clock" "cross" "dotbox" "exchange" "fleur" "heart" "heart" "man" "mouse" "pirate" "plus" "shuttle" "sizing" "spider" "spraycan" "star" "target" "tcross" "trek" "watch"
    )

# Empaquetar texto 
texto.pack(side=LEFT, fill=X, expand=YES ) # el movimiento del texto dentro del pack pero 
                     # los estilos como tal dentro del config.
                     # observar la imagen que hay en imagenes.





# Ingresar texto en la ventana 
texto = Label(ventana, text= "otro texto 3")
# configuracion del texto de vcentana
texto.config( 
    # justify="left", # justificar fuente
    # width=20, # cambia ancho de cuadro 
    height=3, # cambia altura de cuadro 
    bg="violet", # cambiar color de cuadro tambien colores hexadecimales.
    font=("Arial", 18), # tipo de fuente y tamaño.
    padx=10, # margen horizontal
    pady=20, # margen vertical
    cursor="pirate" # cambiar forma del cursor. "arrow" "circle" "clock" "cross" "dotbox" "exchange" "fleur" "heart" "heart" "man" "mouse" "pirate" "plus" "shuttle" "sizing" "spider" "spraycan" "star" "target" "tcross" "trek" "watch"
    )

# Empaquetar texto 
texto.pack(side=LEFT, fill=X, expand=YES ) # el movimiento del texto dentro del pack pero 
                     # los estilos como tal dentro del config.
                     # observar la imagen que hay en imagenes.





# arrancar la ventana y mostrar la ventana
ventana.mainloop()