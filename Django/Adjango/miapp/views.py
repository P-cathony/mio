from django.shortcuts import render, HttpResponse, redirect
from miapp.models  import Article
from django.db.models import Q  # operador or en la BD
from miapp.forms import FormArticle # importando la clase FormArticle
from django.contrib import messages 



# Create your views here.




# creando la vista index en django
def index(request): 
    # todo lo que se puede hacer en una vista.
    # html = """                        
    #     <h1>
    #         Inicio
    #     </h1>

    # """

# ----------------------------------------------------

    # html = """
    #     <p>
    #         años hasta el 2050: 
    #     </p>
    #     <ul>
    # """

    # year = 2021
    # while year <=2050:
    #     if year % 2 == 0:
    #         html += f"<li> {str(year)} </li>"
    #     year += 1
    # html += "</ul>"




    # variables vista
    nombre = "william A"
    lenguajes = ['JavaScript','Python','Php','C++']
    year = 2021
    hasta = range(year, 2051)





    # return HttpResponse(layout+html)
    return render(request, 'index.html', {
        'title': 'Inicio',
        'mi_variable': 'hablo desde mi_variable', # pasando variables de la vista al template
        'nombre': nombre,
        'lenguajes': lenguajes,
        'years': hasta

    }) # de esta forna mostramos los templates en una vista.
                                         # tambien se debe agregar a la lista de apps, la app sobre la que se trabaja.
# ----------------------------------------------------






# creando la vista hola mundo en django
def hola_mundo(request): # request: parametro que permite recibir datos de peticiones que se hagan a esta URL, se debe colocar en todas las funciones de views.py.
    # return HttpResponse(layout+"Hola mundo desde django") # para mostrar este metodo se tiene que llamar en urls.py
    return render(request, 'hola_mundo.html')



# creando la vista pagina en django
def pagina(request, redir=0):

                            # se redirecciona con el nombre de la url.
    if redir == 1:         #|
        return redirect('hola_mundo') # redireccionando a otras paginas.
        

    return render(request, 'pagina.html')


 
   # creando la vista contacto en django
def contacto(request, nombre="", apellidos=""):
    
    if nombre and apellidos:
        pass
        # return redirect('inicio')  
    

    return render( request, 'contacto.html') # 



#  Crear articulo
def crear_articulo(request, titulo, contenido, publico):

    try:
        
        articulo = Article(
            title=titulo,
            content=contenido,
            public=publico
        )

        articulo.save()
        return HttpResponse(f'Articulo created: {articulo.id} <strong>{articulo.title}, {articulo.content} ')

    except:
        response = 'Error no se pudo crear, verfica la ruta, o los valores de la url: crear-articulo/titulo/contenido/False or True. '
    return HttpResponse(response)





#  Crear articulo
def save_articulo(request):

    try:

        if request.method=='POST':
            titulo=request.POST['title']
            contenido=request.POST['content']
            publico=request.POST['public']
        
        articulo = Article(
            title=titulo,
            content=contenido,
            public=publico
        )

        articulo.save()
        # return HttpResponse(f'Articulo created: {articulo.id} <strong>{articulo.title}, {articulo.content} ')
        return redirect('listar_articulos')
    except:
        response = 'Error no se envian los datos revisa las urls o los metodos GET and POST  '
    return HttpResponse(response)



   
        
#  Crear articulo
def create_article(request):

    try:
        
        return render(request, 'create_article.html')

    except:
        response = 'Error  '
    return HttpResponse(response)
        


    

#  Crear create_full_articulo
def create_full_article(request):

    try:

        if request.method == 'POST':
            full_form = FormArticle(request.POST)
        
            if full_form.is_valid() :
                data_form = full_form.cleaned_data

                title = data_form.get('title')
                content = data_form['content']
                public = data_form.get('public')
                


                articulo = Article(
                    title=title,
                    content=content,
                    public=public
                    
                )

                articulo.save()

                #  crear mensaje flash que solo se muestra una vez.
                messages.success(request, f'Articulo {articulo.id} - {articulo.title } creado exitosamente')

                return redirect('listar_articulos')
                # return HttpResponse(title + ' - ' + content + ' - ' + str(public))

        else:
            full_form = FormArticle()


        return render(request, 'create_full_article.html', {
            'formulario' : full_form 
        }) 
        

    except:
        response = 'Error  '
    return HttpResponse(response)







#  Actualizar Articulo
def editar_articulo(request, id):

    try:
        articulo = Article.objects.get(pk = id)
        articulo.title = 'kin-kong'
        articulo.content = 'Pelicula de accion'
        articulo.public = True
        
        articulo.save()
        
        
        response = f'Articulo {articulo.id} editado : <stron> {articulo.title}  {articulo.content}</strong>'
        
    except:
        response = 'Articulo no encontraado'

    return HttpResponse(response)








#  eliminar Articulo
def eliminar_articulo(request, id):

    try:
        articulo = Article.objects.get(pk = id)
        
        
        # articulo.save()
        
        
        response = f'Articulo {articulo.id} eliminado : <stron> {articulo.title}  {articulo.content}</strong>'

        articulo.delete()

        return redirect('listar_articulos')
        
    except:
        response = 'Articulo no eliminado'

    return HttpResponse(response)







#  Mostrar articulo
def Articulo(request, titulo):

    try:
        articulo = Article.objects.get(title=titulo)
        response = f'Articulo: <br/> {articulo.id} - {articulo.title}'
        
    except:
        response = 'Articulo no encontraado'

    return HttpResponse(response)






# listar articulos

def listar_articulos(request):

    try:
        articulos = Article.objects.filter(public=True).order_by('-id')  #  se puede reemplazar y usar el metodo: order_by('id')[:3] mostrando solo 3 elementos.
       
        # articulos = Article.objects.filter(title__contains="articulo") #filter=== title__contains="",title__exact="", title__iexact="" 
        # filter(id__gt =12 --> mas grande que 11, id__gte =12 --> mayores e iguales, id__lt =12 --> menores, id__lte =12 --> menores e iguales )

        # articulos = Article.objects.filter(
        #                                 # title__contains="articulo",
        #                                 ).exclude(
        #                                     public=True
        #                                 ) #  exclude, me excluye algo de la lista.


        # articulos = Article.objects.raw("SELECT * FROM miapp_article WHERE public=1 ") # ejecutar SQL puro.

        # articulos = Article.objects.filter(
        #     Q(title__contains = "2") | Q(title__contains="3") # que contenga en su titulo el numero 2 o el 3.
        #     )



        return render(request, 'listarArticulos.html', {
            
            'articulos': articulos
        })

    except:

        response = 'no se pudo mostrar el contenido' 

    return HttpResponse(response)
