from django import forms
from .models import Curso, ActividadDocente, Nivel, ProyectoCurricular, TipoActividad

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = '__all__'


class ActividadDocenteForm(forms.ModelForm):
    class Meta:
        model = ActividadDocente
        fields = '__all__'
    nivel = forms.ModelChoiceField(queryset=Nivel.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    proyecto_curricular = forms.ModelChoiceField(queryset=ProyectoCurricular.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))