from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm

class userregistrationForm(forms.ModelForm):
    
    class Meta:
        model = CustomUser
        fields = ['user_name','is_employee', 'user_pic', 'user_pass', 'confirm_password']
        # labels = {'email':'Email'}
        widgets = {'user_name':forms.TextInput(attrs={'class':'form-control'}),
                   'user_pass':forms.PasswordInput(attrs={'class':'form-control'}),
                   'confirm_password':forms.PasswordInput(attrs={'class':'form-control'})}

    def clean(self, *args, **kwargs):
        user_name = self.cleaned_data.get('user_name')
        password1 = self.cleaned_data.get('user_pass')
        password2 = self.cleaned_data.get('confirm_password')

        if password1 != password2:
            raise forms.ValidationError("Password Don't Match")
        
        pas = CustomUser.objects.filter(user_name=user_name)
        if pas.exists():
            raise forms.ValidationError("Username Already In Use")
        
        return super(userregistrationForm, self).clean(*args, **kwargs)
    
    
class OrganisationForm(forms.ModelForm):
    class Meta:
        model = organisation
        fields = ['org_name', 'org_desc', 'org_logo', 'org_page']
        # widgets = {'org_name':forms.TextInput(attrs={'class':'form-control'}),
                #    'org_page':forms.TextInput(attrs={'class':'form-control'})}
        