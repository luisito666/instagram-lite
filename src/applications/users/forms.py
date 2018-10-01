from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label='',
                               required=True,
                               max_length='30',
                               min_length='4',
                               widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control'})
    )
    password = forms.CharField(label='',
                               required=True,
                               max_length='40',
                               min_length='4',
                               widget=forms.PasswordInput(render_value=True, attrs={'placeholder': 'Password', 'class': 'form-control'})
    )

class ProfileForm(forms.Form):
    """
    """
    website = forms.URLField(max_length='200', required=True)
    biography = forms.CharField(max_length='500', required=False)
    phone_number = forms.CharField(max_length='20', required=False)
    picture = forms.ImageField()
    