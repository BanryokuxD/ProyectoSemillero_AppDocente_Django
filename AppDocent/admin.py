from django.contrib import admin
from .models import TipoActividad, CentroCostos, Nivel, ProyectoCurricular, User, Profesor, Vinculacion, Dedicacion


admin.site.register(TipoActividad)
admin.site.register(CentroCostos)

admin.site.register(Nivel)
admin.site.register(ProyectoCurricular)


admin.site.register(Profesor)
admin.site.register(User)


admin.site.register(Vinculacion)
admin.site.register(Dedicacion)