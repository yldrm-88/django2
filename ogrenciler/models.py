from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Ogrenciler(models.Model):
    adSoyad=models.CharField(max_length=100,verbose_name="Ad Soyad")
    hakkinda=models.TextField(max_length=100,verbose_name="Hakkında")
    resim=models.FileField(upload_to="ogrenci_resmi",null=True,blank=True,verbose_name="Resim")
    olusturan=models.ForeignKey(User,on_delete=models.CASCADE,null=True) #herhangi bir öğrenciyi silince onunla ilgili her şeyi siler.
    #modelde değişiklik yaptığında makemigration yapman lazım ardından migrate yapacaksın
    def __str__(self):
        return self.adSoyad