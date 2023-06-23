from django import forms
class LoginUsuario(forms.Form):
    usuario = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Ingrese su username','class':'form-control'}),max_length=50,required=True,label='Nombre de usuario')
    clave = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Ingrese su contraseña','class':'form-control'}), max_length=20,label='Password',required=True,error_messages={'required':'La contraseña es obligatoria'})