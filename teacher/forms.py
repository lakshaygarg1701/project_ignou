from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class FacultySignUp(UserCreationForm):
	first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
	last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
	email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
	mobile= forms.CharField(max_length=10)

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'mobile', 'password1', 'password2')