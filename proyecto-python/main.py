

# PAGINA PRINCIPAL

"""
- abrir asistente 
- login o registro
- si elegimos registro, creara un usuario en bbdd
- si elegimos login, identificamos al usuario y nos preguntará
- crear nota, mostrar notas, borrarlas. 

"""

from usuarios import acciones

print("""
Acciones disponibles:
    - registro
    - login


""")

# intanciando un objeto del tipo Acciones.
hazEL = acciones.Acciones()

accion = input("¿Que quieres hacer?: ")

# llamamos el metodo registro y login de la clase Acciones.
if accion == "registro":
    hazEL.registro()
    

elif accion == "login":
    hazEL.login()
    
