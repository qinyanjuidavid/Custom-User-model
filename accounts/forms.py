from django.forms import ModelForm
from django import forms
from accounts.models import User
from django.contrib.auth.forms import ReadOnlyPasswordHashField

class usercreationform(ModelForm):
    class Meta:
        model=User
        fields=('first_name','last_name','email',)
    password1=forms.CharField(label='Password',widget=forms.PasswordInput)
    password2=forms.CharField(label='Password Confirmation',widget=forms.PasswordInput)
    def clean_password2(self):
        password1=forms.cleaned_data["password1"]
        password2=forms.cleaned_data["password2"]
        if passord1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match!")
        return password2
    def save(self, commit=True):
        user= super(usercreationform, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user




class userchangeform(ModelForm):
    password=ReadOnlyPasswordHashField()
    class Meta:
        model=User
        fields=('email','first_name','last_name','password','admin','active')

    def clean_password(self):
        return self.initial["password"]
