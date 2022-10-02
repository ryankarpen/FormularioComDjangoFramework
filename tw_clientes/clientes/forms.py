from django import forms

from .models import Cliente


class ClienteForm(forms.ModelForm):  # o ModelForm irá obter todas as validações que informamos no nosso model
    class Meta:
        model = Cliente
        fields = ['nome', 'sexo', 'data_nascimento', 'email', 'profissao']
