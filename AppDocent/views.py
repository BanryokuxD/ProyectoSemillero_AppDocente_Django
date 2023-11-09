from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Curso
from .forms import CursoForm, ActividadDocenteForm


def singin(request):
    if request.method == 'GET':
        return render(request, 'singin.html', {
            'form': AuthenticationForm()
        })
    else:
        user = authenticate(request, username=request.POST['username'],
                            password=request.POST['password'])
        if user is None:
            return render(request, 'singin.html', {
                'form': AuthenticationForm(),
                'error': 'Usuario o contraseña incorrectos'
            })
        else:
            login(request, user) 
            return redirect('registrar_actividades')

        
@login_required
def singout(request):
    logout(request)
    return redirect('singin')



def seleccionar_metodos(request):
    if request.method == 'POST':
        selected_methods = request.POST.getlist('selected_methods')
        if 'consultar' in selected_methods:
            return HttpResponseRedirect(reverse('registrar_curso', args=['consultar']))
        elif 'modificar' in selected_methods:
            return HttpResponseRedirect(reverse('registrar_curso', args=['modificar']))
        elif 'cargar' in selected_methods:
            return HttpResponseRedirect(reverse('registrar_curso', args=['cargar']))
    
    return render(request, 'seleccionar_metodos.html')

def registrar_curso(request, selected_method=None):
    cursos = Curso.objects.all()

    if selected_method == 'consultar':
        # Lógica para consultar planes de trabajo
        pass
    elif selected_method == 'modificar':
        # Lógica para modificar planes de trabajo
        pass
    elif selected_method == 'cargar':
        # Lógica para cargar cursos
        pass
    
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            cursos = Curso.objects.all()
    
    else:
        form = CursoForm()
    
    return render(request, 'registrar_curso.html', {'form': form, 'cursos': cursos})


def registrar_actividades(request):
    form_actividades = ActividadDocenteForm()
    if request.method == 'POST':
        form_type = request.POST.get('form_type')
        if form_type == 'form_datos_docente':
            return redirect('registrar_actividades')
        elif form_type == 'form_actividades':
            form_actividades = ActividadDocenteForm(request.POST)
            if form_actividades.is_valid():
                form_actividades.save()
                return redirect('registrar_actividades')

    context = {
        'form_actividades': form_actividades,
    }

    return render(request, 'registrar_actividades.html', context)

