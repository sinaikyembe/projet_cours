from django.contrib import admin
from .models import Enseignant,Cours,Promotion

# Register your models here.
admin.site.register(Enseignant)
admin.site.register(Cours)
admin.site.register(Promotion)

