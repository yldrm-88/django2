from django.shortcuts import render,redirect
from .models import*
from .form import*
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    ogrenciler=Ogrenciler.objects.all()
    context={
        "ogrenciler":ogrenciler,
    }
    return render(request,"index.html",context)


def detay(request,id):
    ogrenci=Ogrenciler.objects.filter(id=id)
    context={
        "ogrenci":ogrenci
    }
    return render(request,"detay.html",context)


def create(request):
    form=OgrenciForm()
    context={
        "form":form
    }
    if request.method=="POST":
        form=OgrenciForm(request.POST,request.FILES)
        if form.is_valid():
            ogr=form.save(commit=False)
            ogr.olusturan=request.user
            ogr.save()
            return redirect("index")
        else:
            return(request,"create.html",context)
    return render(request,"create.html",context)

def filter(request,id):
    ogrenciler=Ogrenciler.objects.filter(olusturan=id)
    context={
        "ogrenciler":ogrenciler,
    }
    return render(request,"filter.html",context)