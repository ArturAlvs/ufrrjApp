from django.contrib import admin

# Register your models here.


from .models import Anunciante, Produto, Horario

admin.site.register(Anunciante)
admin.site.register(Produto)
admin.site.register(Horario)