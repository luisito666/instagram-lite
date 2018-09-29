from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label='',
                               required=True,
                               max_length='30',
                               widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control'})
    )
    password = forms.CharField(label='',
                               required=True,
                               widget=forms.PasswordInput(render_value=True, attrs={'placeholder': 'Password', 'class': 'form-control'})
    )
    