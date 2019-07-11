from django import forms
from .models import Register,Enquiry,News


class regform(forms.ModelForm):
    class Meta:
        model=Register
        fields = "__all__"


class logform(forms.Form):
      name = forms.CharField(required=False)
      password = forms.CharField(max_length=20)  
      # comment = forms.CharField(widget=forms.Textarea) 

class Enquiryform(forms.ModelForm):
    class Meta:
        model=Enquiry
        fields = "__all__"

class Newsletter(forms.ModelForm):
    Email=forms.CharField(required=True,max_length=50)

    class Meta:
        model = News
        widgets = {'Email': forms.EmailInput(), }
        fields = ['Email',]