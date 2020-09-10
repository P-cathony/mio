"""Adjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

# importar los settings para cargar las informacion de MEDIA
from django.conf import settings

# importando las vistas de miapp.
# from miapp import views # forma común.
import miapp.views # otra forma de llamar las vistas.



urlpatterns = [  
    # vista de administrador django.
    path('admin/', admin.site.urls), # user: admin  pass: djangoadmin.
    
    # una vista puede ser llamada de diferentes rutas.
    path('', miapp.views.index, name="index"),
    path('inicio/', miapp.views.index, name="inicio"),

    # view hola_mundo
    path('hola-mundo/', miapp.views.hola_mundo, name="hola_mundo"),

    # view pagina
    path('pagina-pruebas/', miapp.views.pagina, name="pagina-pruebas"),
    path('pagina-pruebas/<int:redir>', miapp.views.pagina, name="pagina-pruebas"),
    
    # view contacto
    path('contacto/', miapp.views.contacto, name="contacto"), # vista normal 
    path('contacto/<str:nombre>', miapp.views.contacto, name="contacto"), # recoger parametros por la url. luego se le pasa a la vista.
    path('contacto/<str:nombre>/<str:apellidos>', miapp.views.contacto, name="contacto"), # recoger parametros por la url. luego se le pasa a la vista.

    # view crear_articulo
    path('crear-articulo/<str:titulo>/<str:contenido>/<str:publico>', miapp.views.crear_articulo, name="crear_articulo"), 

    # view articulo
    path('articulo/<str:titulo>', miapp.views.Articulo, name="articulo"), 

    # view editar_articulo
    path('editar-articulo/<int:id>', miapp.views.editar_articulo, name="editar_articulo"), 

    # vista eliminar_articulo
    path('eliminar-articulo/<int:id>', miapp.views.eliminar_articulo, name="eliminar_articulo"), 

    # view listar_articulos
    path('articulos/', miapp.views.listar_articulos, name="listar_articulos"), 

    
    # view save_articulo
    path('save-article/', miapp.views.save_articulo, name="save_articulo"),

    
    # view create_article
    path('create-article/', miapp.views.create_article, name="create_article"),
    


    # view create_article
    path('create-full/', miapp.views.create_full_article, name="create_full_article"),
    
]


# Configuracion para cargar imagenes
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

















