from django import forms
from reserva.models import Reserva

from datetime import date

class ReservaForm(forms.ModelForm):

    def clean_data_apenas(self):
        data = self.cleaned_data['data_apenas']
        hoje = date.today()

        if data < hoje:
            raise forms.ValidationError('Não é possível realizar uma reserva para o passado!')

        quantidade_de_reservas = Reserva.objects.filter(data_apenas=data).count()

        if quantidade_de_reservas >= 4:
            raise forms.ValidationError('O limite máximo de reservas para esse dia já foi atingido.')
        
        return data

    class Meta:
        model = Reserva
        fields = [
            'nome', 'email', 'nome_pet', 'data_apenas', 'turno',
            'tamanho', 'observacoes', 'petshop', 'categoria'
        ]
        widgets = {
            'data_apenas': forms.DateInput(attrs={'type': 'date'})
        }