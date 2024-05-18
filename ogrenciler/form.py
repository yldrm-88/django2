from django.forms import ModelForm
from .models import Ogrenciler

class OgrenciForm(ModelForm): #Model formdan miras alır.
    class Meta:      #Bu bir subclass yani alt classdır.Burada kolon içerisindeki model isimlerini almamıza yardımcı olur.
        model=Ogrenciler
        fields=["adSoyad","hakkinda","resim"]
    def __init__(self,*args,**kwargs):  #args tuple yani istediğin kadar parametre yollayabilirsin demek.
        super(OgrenciForm,self).__init__(*args,**kwargs)
        self.fields["adSoyad"].widget.attrs.update({"class":"form-control"})
        self.fields["hakkinda"].widget.attrs.update({"class":"form-control"})
        self.fields["resim"].widget.attrs.update({"class":"form-control"})