from django import forms
from django.contrib.auth.models import User
from applications.users.models import Profile

class LoginForm(forms.Form):
    """
    """
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


class SignupForm(forms.Form):
    """
    """
    username = forms.CharField(
        label='',
        min_length='4',
        max_length='50',
        widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control'})
    )
    password = forms.CharField(
        label='',
        max_length='70', 
        widget=forms.PasswordInput(render_value=True, attrs={'placeholder': 'Password', 'class': 'form-control'})
    )
    password_confirmation = forms.CharField(
        label='',
        max_length='70', 
        widget=forms.PasswordInput(render_value=True, attrs={'placeholder': 'Password confirmation', 'class': 'form-control'})
    )
    first_name = forms.CharField(
        label='',
        min_length='2' ,
        max_length='50',
        widget=forms.TextInput(attrs={'placeholder': 'First name', 'class': 'form-control'})
    )
    last_name = forms.CharField(
        label='',
        min_length='2', 
        max_length='50',
        widget=forms.TextInput(attrs={'placeholder': 'Last name', 'class': 'form-control'})
    )
    email = forms.CharField(
        label='',
        min_length='6', 
        max_length='70', 
        widget=forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'form-control'})
    )

    def clean_username(self):
        """
        """
        username = self.cleaned_data['username']
        username_taken = User.objects.filter(username=username).exists()
        if username_taken:
            raise forms.ValidationError('Username is already in use')
        return username

    def clean(self):
        """ verificamos la confirmacion del password
        """
        data = super().clean()
        password = data['password']
        password_confirmation = data['password_confirmation']

        if password != password_confirmation:
            raise forms.ValidationError('Password do not match')

        return data

    def save(self):
        """ creamos usuario y perfil
        """
        data = self.cleaned_data
        data.pop('password_confirmation')
        user = User.objects.create_user(**data)
        profile = Profile(user=user)
        profile.save()
