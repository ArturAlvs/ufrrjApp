from django.contrib import admin

# Register your models here.

from .models import Refeicao, Horarios

admin.site.register(Refeicao)
admin.site.register(Horarios)