from django import forms

from member.models import User

'''class LoginForm(forms.ModelForm):
	class Meta:
		model=User
		field=['username','password']

class RegisterForm(forms.ModelForm):
	class Meta:
		model=User
		field=['username','email','password1', 'password2']

'''
class UserEditForm(forms.ModelForm):
	class Meta:
		model=User
		fields = ['is_student', 'is_administrator']