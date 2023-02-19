from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label='Имя пользователя: ')
    password = forms.CharField(label='Пароль')

    class Meta:
        fields = ['username', 'password',]


class SignatureForm(forms.Form):
    signature = forms.CharField(label='Код')

    class Meta:
        fields = ['signature',]







