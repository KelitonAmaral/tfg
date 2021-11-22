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
   
    type = forms.ChoiceField(label ='User type *', choices=TYPES_USERS, help_text='* Required fields')
    name = forms.CharField(label='Name *', max_length=100)
    email = forms.EmailField(label='Email', max_length=100)
    cpf = forms.CharField(label='CPF *',max_length=14,help_text='ATENTION: just numbers')
    phone = forms.CharField(label='Cellphone *',max_length=14, help_text='ATENTION: just numbers') 
    birth_date = forms.DateField(label='Date of birth *', help_text='dd/mm/aaaa')       
    gender = forms.ChoiceField(label='Gender *', choices=TYPE_GENDER)    
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
    name = forms.ChoiceField(label='User name', choices=TYPES_USERS, required=False)
    type = forms.CharField(label='User type', required=False)