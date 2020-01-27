from django.contrib import admin

from .models import Medication, SideEffect

admin.site.register(Medication)
admin.site.register(SideEffect)
