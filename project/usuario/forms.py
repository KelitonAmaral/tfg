from django import forms
from .models import Usuario
from curso.models import Curso

class UsuarioRegisterForm(forms.ModelForm):
    TIPOS_USUARIOS = (
        ('ALUNO', 'Aluno'),
    )
   
   
    tipo = forms.ChoiceField(label='Tipo *',choices=TIPOS_USUARIOS, help_text='Este processo cadastra somente alunos' )
    nome = forms.CharField(label='Nome completo', help_text='* Campos obrigatórios')
    email = forms.EmailField(label= 'Email *', max_length=100, help_text='Use o email institucional')
    curso = forms.ModelChoiceField(label='Curso *',queryset=Curso.objects.all())
    cpf = forms.CharField(label='CPF *' , max_length = 14 , help_text='ATENÇÃO: Somente os NÚMEROS', required = True)
    matricula = forms.CharField(label='Matrícula *', max_length=10, help_text="ATENÇÃO: Consulte o <a href='http://www.ufn.edu.br/agenda' target= '_blank'>AGENDA</a> para descobrir", required = True)    
    fone = forms.CharField(label='Celular para contato *', max_length=14, help_text="ATENÇÃO: Somente os NÚMEROS", required = True)    
    password = forms.CharField(label= "Senha *", widget=forms.PasswordInput)
        
    class Meta:
        model = Usuario
        fields = ['nome','tipo','curso', 'email', 'cpf', 'matricula', 'fone','password']


class BuscaAlunoForm(forms.Form):
    nome_usuario = forms.CharField(label='Nome do usuário', required=False)
    curso = forms.ModelChoiceField(label='Curso', queryset=Curso.objects.all(), required=False)