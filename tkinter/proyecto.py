from tkinter import * 
from tkinter import ttk # importar modulo tablas


# crear la ventana raiz
ventana = Tk()

# cambiar tamaño en la ventana
# ventana.geometry("500x500")
ventana.minsize(500, 500) # hacemos que la ventana sea dinamica y crezca con la informacion.
ventana.title("proyecto en tkinter | toni")
ventana.resizable(0,0)




# PANTALLAS
# montar pantalla
def home():
    
    home_label.config(
        fg="white",
        bg="black",
        font=("Arial", 30 ),
        padx=210,
        pady=20
    )
    home_label.grid(row=0, column=0)

    # llamando el metodo products_box() para listar porcuctos
    products_box.grid(row=2)

    # listar productos
    # for product in products:
    #     if len(product) == 3:
    #         product.append("added")
    #         Label(products_box, text=product[0]).grid()
    #         Label(products_box, text=product[1]).grid()
    #         Label(products_box, text=product[2]).grid()
    #         Label(products_box, text="-----------------").grid()
            

    for product in products:
        if len(product) == 3:
            
            product.append("added")
            products_box.insert('',0,text=product[0], values= (product[1]))

    
    # Ocultar pantallas
    add_label.grid_remove()
    info_label.grid_remove()
    data_label.grid_remove()
    add_frame.grid_remove()

    return True

    


def add():
    # Encabezado
    add_label.config(
        fg="white",
        bg="black",
        font=("Arial", 30 ),
        padx=110,
        pady=20
    )
    add_label.grid(row=0, column=0, columnspan=10)

    # campos formulario 
    # Mostrar Frame
    add_frame.grid(row=1)

    # nombre producto
    add_name_label.grid(row=1, column=0, padx=5, pady=5, sticky=E)
    add_name_Entry.grid(row=1, column=1, padx=5, pady=5, sticky=W)
   
    # precio producto
    add_price_label.grid(row=2, column=0, padx=5, pady=5, sticky=E)
    add_price_Entry.grid(row=2, column=1, padx=5, pady=5, sticky=W)
   
    # Descripcion producto
    add_description_label.grid(row=3, column=0, padx=5, pady=5, sticky=NW)
    add_description_Entry.grid(row=3, column=1, padx=5, pady=5, sticky=W)
    add_description_Entry.config(
        width=40,
        height=5,
        font=("Consolas", 12),
        padx=5,
        pady=5
    )

    

    add_separator.grid(row=4)

    # configuracion boton 
    boton.grid(row=5, column=1, sticky=E)
    boton.config(
        padx=15,
        pady=5,
        bg="green",
        fg="white"
    )

    # Ocultar pantallas
    home_label.grid_remove()
    products_box.grid_remove()
    info_label.grid_remove()
    data_label.grid_remove()
    
    
   
   
    return True

  




def info():
    
    info_label.config(
        fg="white",
        bg="black",
        font=("Arial", 30 ),
        padx=150,
        pady=20
        
    )
    info_label.grid(row=0, column=0)
    data_label.grid(row=1, column=0)
    desc_box.grid(row=3, column=0)

    for p in products:
        if len(p) == 3:
            p.append("added")
            Label(desc_box, text=p[2]).grid()
        
    

    
   

  # Ocultar pantallas
    add_label.grid_remove()
    home_label.grid_remove()
    add_frame.grid_remove()
    products_box.grid_remove()

    
    return True



# Agregar productos
def add_product():
    products.append([
        name_data.get(),
        price_data.get(),
        add_description_Entry.get("1.0", "end-1c")

    ])
    print(products)
    
  
    
        
        
        
    
    # llamamos el metodo home() para volver a la pantalla home.
    home()


    # vaceando campos.
    name_data.set("")
    price_data.set("")
    add_description_Entry.delete("1.0", END)



#  campos de pantallas (inicio)
home_label = Label(ventana, text="inicio")
# products_box = Frame(ventana, width=250)




# Definiendo tabla para mostrar datos.
# Label(products_box).grid(row=0)

# creamos la  tabla
Label(ventana).grid(row=1)
products_box = ttk.Treeview(height=12, columns=3)
products_box.grid(row=1, column=0, columnspan=2)

# creamos las columnas
products_box.heading("#0", text="Producto", anchor=W)
products_box.heading("#1", text="Precio", anchor=W)




#  campos de pantallas (añadir)
add_label = Label(ventana, text="Añadir Producto")

#  campos de pantallas (informacion)
info_label = Label(ventana, text="informacion")
data_label = Label(ventana, text="Creado por toni - 2020")
desc_box = Frame(ventana, width=250)










# variables importantes
products = []
name_data = StringVar()
price_data = StringVar()







# campos de formulario (Nombre producto)
# Definiendo frame
add_frame = Frame(ventana)


add_name_label = Label(add_frame, text="Nombre ")
add_name_Entry = Entry(add_frame, textvariable=name_data)


#  campos de formulario (Precio producto)
add_price_label = Label(add_frame, text="Precio ")
add_price_Entry = Entry(add_frame, textvariable=price_data)


#  campos de formulario (Precio producto)
add_description_label = Label(add_frame, text="Descripcion")
add_description_Entry = Text(add_frame)

add_separator = Label(add_frame)

# Button
boton = Button(add_frame, text="Guardar", command=add_product)




# cargar pantalla de inicio
home()




# MENU SUPERIOR
menu_superior = Menu(ventana) # Instancia de la clase menú

# Menu barra ventana
menu_superior.add_command(label="Inicio", command=home)
menu_superior.add_command(label="Añadir", command=add)
menu_superior.add_command(label="Informacion", command=info)
menu_superior.add_command(label="salir", command=ventana.quit)




# cargar menú
ventana.config(menu=menu_superior)













# arrancar la ventana y mostrar la ventana
ventana.mainloop()