from django.contrib.auth.models import User #djangonun kendi modelini kullanacağız onu import ederiz.
from django.contrib.auth.forms import UserCreationForm

class Kullanici(UserCreationForm):
    class Meta:
        model = User
        fields=["username","email","password1","password2"]

    def __init__(self,*args,**kwargs):
        super(Kullanici,self).__init__(*args,**kwargs)
        self.fields["username"].widget.attrs.update
        ({'class':'form-control'})
        self.fields["email"].widget.attrs.update
        ({'class':'form-control'})
        self.fields["password1"].widget.attrs.update
        ({'class':'form-control'})
        self.fields["password2"].widget.attrs.update
        ({'class':'form-control'})