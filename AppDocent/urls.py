from django.urls import path
from . import views
from django.views.generic import RedirectView
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('logout/', views.singout, name='logout'),
    path('singin/', views.singin, name='singin'),
    path('seleccionar_metodos/', views.seleccionar_metodos, name='seleccionar_metodos'),
    path('registrar_curso/cargar/', views.registrar_curso, name='registrar_curso_cargar'),
    path('registrar_actividades/', views.registrar_actividades, name='registrar_actividades'),
    path('', RedirectView.as_view(url='/singin/', permanent=True)),
    # Agrega más rutas y vistas según sea necesario
]

## urlpatterns[2] = path('trabajos/', login_required(views.trabajo, login_url='singin'), name='trabajos')
