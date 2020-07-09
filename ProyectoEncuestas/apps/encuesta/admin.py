from django.contrib import admin

# Register your models here.
from .models import Departamento
from .models import Estacompuesto
from .models import Municipio
from .models import Reclamo
from .models import Respuesta
from .models import Tipotrasporte
from .models import Usuario

admin.site.register(Departamento)
admin.site.register(Estacompuesto)
admin.site.register(Municipio)
admin.site.register(Reclamo)
admin.site.register(Respuesta)
admin.site.register(Tipotrasporte)
admin.site.register(Usuario)