from django.contrib.auth.models import User 

def getContext(request):
    kullanicilar=User.objects.all()
    context={
        "kullanicilar":kullanicilar,
    }
    return context