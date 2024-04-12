from django import forms
from StoreApp.models import Cliente

#criando um formulário basedo num model
class CadastroForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'