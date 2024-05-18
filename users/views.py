from django.shortcuts import render,redirect
from .form import*
from django.contrib.auth import authenticate,login as lgn ,logout #login için import edilmesi gerekenler
from django.contrib import messages
# Create your views here.

def register(request):
    form=Kullanici()
    context={
        "form":form
    }
    if request.method=="POST":
        form=Kullanici(request.POST)
        if form.is_valid():
            
           # user=form.save(commit=False)
           # user.username=user.username.lower()
          #  user.save()
          form.save()
          return redirect("index")
        else:
           return render(request,"register.html",context)
    return render(request,"register.html",context)



def login(request):
   if request.method=="POST":
      userName=request.POST["userName"]
      userPass=request.POST["userPass"]
      user=authenticate(request,username=userName,password=userPass)#değerlerin eşit olup olmadığına bakacaktır.
      if user is not None:
         lgn(request,user)
         messages.success(request,"Giriş Başarılı")
         return redirect("index")
      else:
         messages.error(request,"Hatalı Giriş")
         return render(request,"login.html")
        
   return render(request,"login.html") #giriş başarılı olunca bizi login sayfasına gönderecektir.


def userLogout(request):
    logout(request)
    return redirect("index")