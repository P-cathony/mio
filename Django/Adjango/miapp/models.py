from django.db import models

# Create your models here.

# tabla Articilo
class Article(models.Model):
    title = models.CharField(max_length=100, verbose_name="Titulo")
    content = models.TextField(verbose_name="Contenido")
    public = models.BooleanField(verbose_name="¿Publicado?")
    img = models.ImageField(default='null', verbose_name="Imagen", upload_to="articles")
    created = models.DateField(auto_now_add=True, verbose_name="Creado")
    updated = models.DateTimeField(auto_now=True, verbose_name="Actualizado")

    class Meta:
        verbose_name = "Articulo"
        verbose_name_plural = "Articulos"
        ordering = ['-id']

    def __str__ (self):
        if self.public:
            public = "(publicado)"
        else:
            public = "(privado)"

        return f"{self.title} {public}"
    

# Tabla category
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    created = models.DateField()
   

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"