from django.shortcuts import render, loader, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Trabajadores, Contactos, Cargas, ListaCargas, ListaContactos
from .forms import FormEmpleado, FormEditarEmpleado, FormCarga, FormContacto, FormLogin, FormListaCargas, FormListaContactos
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html')

def iniciar_sesion(request):
    #Entrega el formulario para que el html lo cargue
    form = FormLogin()
    return render(request, 'iniciar_sesion.html', {'form': form})
    
def listar_empleados(request):
    trabajadores = Trabajadores.objects.all()
    return render(request, 'listar_empleados.html', {'trabajadores': trabajadores})

def agregar_empleado(request):
    #si el usuario envio el formulario con POST se guarda el formulario
    if request.method == 'POST':
        form = FormEmpleado(request.POST)
        if not form.is_valid():
            return render(request, 'agregar_empleado.html', {'form': form})
        form.save()
        messages.success(request, 'Trabajador ingresado exitosamente.')
        return redirect('/listar-empleados/')
        
    #si no, se carga el formulario como render
    else:
        #Entrega el formulario para que el html lo cargue
        form = FormEmpleado()
        return render(request, 'agregar_empleado.html', {'form': form})

def editar_empleado(request, rut_trabajador):
    if request.method == 'POST':
        empleado = get_object_or_404(Trabajadores, rut_trabajador=rut_trabajador)
        formulario = FormEditarEmpleado(request.POST, instance=empleado)
        if formulario.is_valid():
            formulario.save()
            return redirect('listar_empleados') 
    else:
        empleado = get_object_or_404(Trabajadores, rut_trabajador=rut_trabajador)
        formulario = FormEditarEmpleado(instance=empleado)

    return render(request, 'editar_empleado.html', {'formulario': formulario})


def remover_empleado(request, rut_trabajador):
   empleado = get_object_or_404(Trabajadores, rut_trabajador=rut_trabajador)
   empleado.delete()
   return redirect('listar_empleados')

def listar_contactos(request):
    contactos = Contactos.objects.all()
    return render(request, 'listar_contactos.html', {'contactos': contactos})

def agregar_contacto(request):
    #si el usuario envio el formulario con POST se guarda el formulario
    if request.method == 'POST':
        form = FormContacto(request.POST)
        if not form.is_valid():
            return render(request, 'agregar_contacto.html', {'form': form})
        form.save()
        return redirect('/listar-contactos/')
        
    #si no, se carga el formulario como render
    else:
        #Entrega el formulario para que el html lo cargue
        form = FormContacto()
        return render(request, 'agregar_contacto.html', {'form': form})
    
def editar_contacto(request, rut_contacto):
    if request.method == 'POST':
        contacto = get_object_or_404(Contactos, rut_contacto=rut_contacto)
        form = FormContacto(request.POST, instance=contacto)
        if form.is_valid():
            form.save()
            return redirect('/listar-contactos/') 
    else:
        contacto = get_object_or_404(Contactos, rut_contacto=rut_contacto)
        form = FormContacto(instance=contacto)

    return render(request, 'agregar_contacto.html', {'form': form})
    
def remover_contacto(request, rut_contacto):
   carga = get_object_or_404(Contactos, rut_contacto=rut_contacto)
   carga.delete()
   return redirect('/listar-contactos/')

def listar_cargas(request):
    cargas = Cargas.objects.all()
    return render(request, 'listar_cargas.html', {'cargas': cargas})

def agregar_carga(request):
    #si el usuario envio el formulario con POST se guarda el formulario
    if request.method == 'POST':
        form = FormCarga(request.POST)
        if not form.is_valid():
            return render(request, 'agregar_carga.html', {'form': form})
        form.save()
        return redirect('/listar-cargas/')
        
    #si no, se carga el formulario como render
    else:
        #Entrega el formulario para que el html lo cargue
        form = FormCarga()
        return render(request, 'agregar_carga.html', {'form': form})
    
def editar_carga(request, rut_carga):
    if request.method == 'POST':
        carga = get_object_or_404(Cargas, rut_carga=rut_carga)
        form = FormCarga(request.POST, instance=carga)
        if form.is_valid():
            form.save()
            return redirect('/listar-cargas/') 
    else:
        carga = get_object_or_404(Cargas, rut_carga=rut_carga)
        form = FormCarga(instance=carga)

    return render(request, 'agregar_carga.html', {'form': form})
    
def remover_carga(request, rut_carga):
   carga = get_object_or_404(Cargas, rut_carga=rut_carga)
   carga.delete()
   return redirect('/listar-cargas/')

def buscar_empleado(request):
    query = request.GET.get('q')
    if query:
        empleados = Trabajadores.objects.filter(nombre__icontains=query)
    else:
        empleados = Trabajadores.objects.all()
    return render(request, 'resultados_busqueda.html', {'empleados': empleados})

def crear_lista_carga(request):
    #si el usuario envio el formulario con POST se guarda el formulario
    if request.method == 'POST':
        form = FormListaCargas(request.POST)
        if not form.is_valid():
            return render(request, 'agregar_lista_carga.html', {'form': form})
        form.save()
        return redirect('/gestionar-rh/')
        
    #si no, se carga el formulario como render
    else:
        #Entrega el formulario para que el html lo cargue
        form = FormListaCargas()
        return render(request, 'agregar_lista_carga.html', {'form': form})

    
def editar_lista_carga(request, id_lista_cargas):
    if request.method == 'POST':
        listaCarga = get_object_or_404(ListaCargas, id_lista_cargas=id_lista_cargas)
        form = FormListaCargas(request.POST, instance=listaCarga)
        if form.is_valid():
            form.save()
            return redirect('gestionar_rh') 
    else:
        listaCarga = get_object_or_404(ListaCargas, id_lista_cargas=id_lista_cargas)
        form = FormListaCargas(instance=listaCarga)

    return render(request, 'agregar_lista_carga.html', {'form': form})

def remover_lista_carga(request, id_lista_cargas):
   listaCarga = get_object_or_404(ListaCargas, id_lista_cargas=id_lista_cargas)
   listaCarga.delete()
   return redirect('gestionar_rh')

def crear_lista_contacto(request):
    #si el usuario envio el formulario con POST se guarda el formulario
    if request.method == 'POST':
        form = FormListaContactos(request.POST)
        if not form.is_valid():
            return render(request, 'agregar_lista_contacto.html', {'form': form})
        form.save()
        return redirect('/gestionar-rh/')
        
    #si no, se carga el formulario como render
    else:
        #Entrega el formulario para que el html lo cargue
        form = FormListaContactos()
        return render(request, 'agregar_lista_contacto.html', {'form': form})

    
def editar_lista_contacto(request, id_lista_contactos):
    if request.method == 'POST':
        listaContacto = get_object_or_404(ListaContactos, id_lista_contactos=id_lista_contactos)
        form = FormListaContactos(request.POST, instance=listaContacto)
        if form.is_valid():
            form.save()
            return redirect('gestionar_rh') 
    else:
        listaContacto = get_object_or_404(ListaContactos, id_lista_contactos=id_lista_contactos)
        form = FormListaContactos(instance=listaContacto)

    return render(request, 'editar_lista_contacto.html', {'form': form})

def remover_lista_contacto(request, id_lista_contactos):
   listaContacto = get_object_or_404(ListaContactos, id_lista_contactos=id_lista_contactos)
   listaContacto.delete()
   return redirect('gestionar_rh')
    
def listar_recursos_humanos(request):
    trabajadores = Trabajadores.objects.all()
    listaCargas = ListaCargas.objects.all()
    listaContactos = ListaContactos.objects.all()
    return render(request, 'gestionar_rh.html', {'trabajadores': trabajadores, 'listaCargas': listaCargas, 'listaContactos': listaContactos})





