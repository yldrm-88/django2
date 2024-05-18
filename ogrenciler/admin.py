from django.contrib import admin

# Register your models here.

#öğrenciler kısmının admin panelinde gözükmesi için import etmemiz lazım
from .models import*

admin.site.register(Ogrenciler)