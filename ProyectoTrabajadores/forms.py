from django import forms
from .models import Trabajadores, Cargas, Contactos, Usuarios, ListaCargas, ListaContactos

class FormEmpleado(forms.ModelForm):
    CARGO_CHOICES = [('Vendedor', 'VENDEDOR'), ('Caja', 'CAJA'), ('Bodeguero/a', 'BODEGUERO/A')]
    DEPARTAMENTO_CHOICES= [('Ventas', 'VENTAS'), ('Bodega', 'BODEGA'), ('Administración', 'ADMINISTRACIÓN')]
    departamento = forms.ChoiceField(choices=DEPARTAMENTO_CHOICES, widget=forms.Select(attrs={'class': 'form-select'}))
    cargo = forms.ChoiceField(choices=CARGO_CHOICES, widget=forms.Select(attrs={'class': 'form-select'}))

    class Meta:
        model = Trabajadores
        exclude = ['contactos', 'cargas']

        #cambia el titulo con el que se muetra el input
        labels = {'rut_trabajador' : 'Rut del trabajador',
                  'nombre' : 'Nombre',
                  'apellido' : 'Apellido',
                  'telefono' : 'Teléfono',
                  'direccion' : 'Dirección',
                  'email' : 'Correo Electrónico'}
        
        #En attrs uno puede pasar los atributos del input como diccionario
        widgets = {'rut_trabajador' : forms.TextInput(attrs={'class' : 'form-control'}),
                   'nombre' : forms.TextInput(attrs={'class' : 'form-control'}),
                   'apellido' : forms.TextInput(attrs={'class' : 'form-control'}),
                   'telefono' : forms.NumberInput(attrs={'class' : 'form-control'}),
                   'direccion' : forms.TextInput(attrs={'class' : 'form-control'}),
                   'email' : forms.TextInput(attrs={'class' : 'form-control'})}

class FormEditarEmpleado(forms.ModelForm):
    CARGO_CHOICES = [('Vendedor', 'VENDEDOR'), ('Caja', 'CAJA'), ('Bodeguero/a', 'BODEGUERO/A')]
    DEPARTAMENTO_CHOICES = [('Ventas', 'VENTAS'), ('Bodega', 'BODEGA'), ('Administración', 'ADMINISTRACIÓN')]
    
    departamento = forms.ChoiceField(choices=DEPARTAMENTO_CHOICES, widget=forms.Select(attrs={'class': 'form-select'}))
    cargo = forms.ChoiceField(choices=CARGO_CHOICES, widget=forms.Select(attrs={'class': 'form-select'}))

    class Meta:
        model = Trabajadores
        exclude = ['rut_trabajador', 'contactos', 'cargas']

        labels = {
                'nombre' : 'Nombre',
                'apellido' : 'Apellido',
                'telefono' : 'Teléfono',
                'direccion' : 'Dirección',
                'email' : 'Correo Electrónico'}

        widgets = {
                    'nombre' : forms.TextInput(attrs={'class' : 'form-control'}),
                    'apellido' : forms.TextInput(attrs={'class' : 'form-control'}),
                    'telefono' : forms.NumberInput(attrs={'class' : 'form-control'}),
                    'direccion' : forms.TextInput(attrs={'class' : 'form-control'}),
                    'email' : forms.TextInput(attrs={'class' : 'form-control'})
                    }

class FormCarga(forms.ModelForm):
    GENERO_CHOICES = [('Hombre', 'Hombre'), ('Mujer', 'Mujer')]
    genero = forms.ChoiceField(choices=GENERO_CHOICES, widget=forms.Select(attrs={'class': 'form-select'}))

    class Meta:

        model = Cargas
        fields = '__all__' 
        #cambia el titulo con el que se muetra el input
        labels = {'rut_carga' : 'Rut de la carga',
                  'nombre' : 'Nombre',
                  'apellido' : 'Apellido',}
        
        #En attrs uno puede pasar los atributos del input como diccionario
        widgets = {'rut_carga' : forms.TextInput(attrs={'class' : 'form-control'}),
                   'nombre' : forms.TextInput(attrs={'class' : 'form-control'}),
                   'apellido' : forms.TextInput(attrs={'class' : 'form-control'})}

class FormContacto(forms.ModelForm): 
    class Meta:

        model = Contactos
        fields = '__all__' 

        #cambia el titulo con el que se muetra el input
        labels = {'rut_contacto' : 'Rut del contacto de emergencia',
                  'nombre' : 'Nombre',
                  'apellido' : 'apellido',
                  'telefono' : 'Teléfono'}
        
        #En attrs uno puede pasar los atributos del input como diccionario
        widgets = {'rut_contacto' : forms.TextInput(attrs={'class' : 'form-control'}),
                   'nombre' : forms.TextInput(attrs={'class' : 'form-control'}),
                   'apellido' : forms.TextInput(attrs={'class' : 'form-control'}),
                   'telefono': forms.NumberInput(attrs={'class': 'form-control'})}

class FormLogin(forms.ModelForm):
    class Meta:

        model = Usuarios
        #Elige que campos del modelo se cargaran como formulario 
        exclude = ['permisos']

        #cambia el titulo con el que se muetra el input
        labels = {'username' : 'Ingresar su nombre de usuario',
                  'password' : 'Contraseña'}
        
        #En attrs uno puede pasar los atributos del input como diccionario
        widgets = {'username' : forms.TextInput(attrs={'class' : 'form-control'}),
                   'password' : forms.PasswordInput(attrs={'class' : 'form-control'})}
        

class FormListaCargas(forms.ModelForm):
    PARENTECO_CHOICES = [('Hijo', 'hijo'), ('Padre', 'padre'), ('Madre', 'madre'), ('Conyuge', 'conyuge'), ('Nieto', 'nieto')]
    parentesco = forms.ChoiceField(choices=PARENTECO_CHOICES, label = 'Parenteco con el trabajador', widget=forms.Select(attrs={'class': 'form-select'}))


    class Meta:
        model = ListaCargas
        fields = '__all__' 

        #cambia el titulo con el que se muetra el input
        labels = {'rut_trabajador' : 'Trabajador',
                  'rut_carga' : 'Carga',
                  'parentesco' : 'Parentesco con el trabajador'
                  }
        
        #En attrs uno puede pasar los atributos del input como diccionario
        widgets = {'rut_trabajador' : forms.Select(attrs={'class' : 'form-control'}),
                   'rut_carga' : forms.Select(attrs={'class' : 'form-control'})}
        
class FormListaContactos(forms.ModelForm):
    RELACION_CHOICES = [('Hijo', 'hijo'), ('Padre', 'padre'), ('Madre', 'madre'), ('Pareja', 'pareja'), ('Nieto', 'nieto')]
    relacion = forms.ChoiceField(choices=RELACION_CHOICES, label = 'Relación con el trabajador', widget=forms.Select(attrs={'class': 'form-select'}))
   
    class Meta:

        model = ListaContactos

        fields = '__all__' 

        #cambia el titulo con el que se muetra el input
        labels = {'rut_trabajador' : 'Trabajador',
                  'rut_contacto' : 'Contacto de emergencia',
                  'relacion' : 'Relación con el trabajador'
                  }
        
        #En attrs uno puede pasar los atributos del input como diccionario
        widgets = {'rut_trabajador' : forms.Select(attrs={'class' : 'form-control'}),
                   'rut_contacto' : forms.Select(attrs={'class' : 'form-control'})}
        



