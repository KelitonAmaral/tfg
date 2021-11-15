from django import forms
from .models import User


class UserRegisterForm(forms.ModelForm):
    TYPES_USERS = (
        ('ATHLETE', 'Athlete' ),
        ('COACH', 'Coach'),
        ('GUEST', 'Guest' ),
    )
    
    TYPE_GENDER = (
        ('FEMALE', 'Female'),
        ('MALE', 'Male'),
    )
   
    type = forms.CharField(_('User type *'), max_length=13, choices=TYPES_USERS, default='GUEST', help_text='* Required fields')
    name = forms.CharField(_('Name *'), max_length=100)
    email = forms.EmailField(_('Email'), unique=True, max_length=100, db_index=True)
    cpf = forms.CharField(_('CPF *'),max_length=14,help_text='ATENTION: just numbers')
    phone = forms.CharField(_('Cellphone *'),max_length=14, help_text='ATENTION: just numbers') 
    birth_date = forms.DateField(_('Date of birth *'), help_text='dd/mm/aaaa')       
    gender = forms.CharField(_('Gender *'), max_length=10, choices=TYPE_GENDER)    
    password = forms.CharField(label= "Password *", widget=forms.PasswordInput)
        
    class Meta:
        model = User
        fields = ['name', 'type', 'email', 'cpf', 'phone', 'birth_date', 'gender', 'password']


class SearchUserForm(forms.Form):
    TYPES_USERS = (
        ('ATHLETE', 'Athlete' ),
        ('COACH', 'Coach'),
        ('GUEST', 'Guest' ),
    )
    name = forms.CharField(label='User name', choices=TYPES_USERS, required=False)
    type = forms.CharField(label='User type', required=False)