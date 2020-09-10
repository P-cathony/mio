# importando forms para trabajar con formularios
from django import forms

# importando validators para las validaciones de los formularios 
from django.core import validators


class FormArticle(forms.Form):
    



    #  campo titulo
    title = forms.CharField(
        label="Titulo",
        max_length=20,
        required=True,
        validators=[
            validators.MinLengthValidator(4, 'El titulo es muy corto'),
            validators.RegexValidator('^[A-Za-z0-9ñ ]*$', 'Escribe bien el titulo !!', 'invalid_title' )
        ]
     
    )
    title.widget.attrs.update({
        'placeholder':'Ingresa titulo',
        'class':'titulo_form_article'
    })




    #  campo contenido
    content = forms.CharField(
        label="Contenido",
        widget= forms.Textarea,
        validators=[
            validators.MaxLengthValidator(20, 'Texto muy grande'),
           
        ]
    )
    content.widget.attrs.update({
        'placeholder':'Ingresa Contenido',
         'class':'content_form_article'
    })
    
    

    
    
    # campo select.
    public_options = [
        (1,'Si'),
        (0,'No')
    ]

    public = forms.TypedChoiceField(
        label="¿Publicado?",
        choices = public_options
    )


