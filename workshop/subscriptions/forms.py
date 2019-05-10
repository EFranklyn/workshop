from django import forms
from django.core.exceptions import ValidationError

from workshop.subscriptions.validators import validate_cpf


class SubscriptionForm(forms.Form):
    name = forms.CharField(label='Nome',
                           widget=forms.TextInput(attrs={'class':'contact_input',
                                                         'placeholder': 'Nome'}))

    cpf = forms.CharField(label='CPF', validators=[validate_cpf],
                           widget=forms.TextInput(attrs={'class':'contact_input',
                                                         'placeholder': 'CPF'}))

    email = forms.EmailField(label='Email',required = False,
                           widget=forms.EmailInput(attrs={'class':'contact_input',
                                                         'placeholder': 'Email'}))

    phone = forms.CharField(label='Phone',required = False,
                           widget=forms.TextInput(attrs={'class':'contact_input',
                                                         'placeholder': 'Telefone'}))

    def clean_name(self):

        name = self.cleaned_data['name']
        words = []

        for w in name.split():
            words.append(w.capitalize())

        capitalized_name = ' '.join(words)
        return capitalized_name


    def clean(self):

        if not self.cleaned_data.get('email') and not self.cleaned_data.get('phone'):
            raise ValidationError('Informe seu email ou Telefone')

        return self.cleaned_data