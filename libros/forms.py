from django import forms
from .models import Libro, Autor, Clasificacion

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ('nombre', 'apellido', 'genero', 'libros')

def __init__ (self, *args, **kwargs):
        super(ClienteForm, self).__init__(*args, **kwargs)
        self.fields["libros"].widget = forms.widgets.CheckboxSelectMultiple()
        self.fields["libros"].help_text = "Ingrese Libros"
        self.fields["libros"].queryset = Libro.objects.all()

class ClasificacionForm(forms.ModelForm):
    class Meta:
        model = Clasificacion
        fields = ('libro', 'autor')

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ('nombre', 'editorial', 'precio', 'unidades')
