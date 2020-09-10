from django.contrib import admin

# importar el modelo de models.py
from .models import Article, Category

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

# registrar los modelos.
admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)


# configurar titulo panel admin
titulo = "Master en Django"
admin.site.site_header = titulo
admin.site.site_title = titulo
admin.site.index_title = "Bienvenido sñr Toni"