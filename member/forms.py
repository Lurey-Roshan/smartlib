from django import forms

from member.models import User

class LoginForm(forms.ModelForm):
	class Meta:
		model=User
		field=('Username','Password')

class RegisterForm(forms.ModelForm):
	class Meta:
		model=User
		field=('Username','email','Password1', 'Password2')