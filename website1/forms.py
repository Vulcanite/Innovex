from django import forms

from django.contrib.auth.forms import UserCreationForm
from website1.models import Account
from django.contrib.auth import authenticate

class RegistrationForm(UserCreationForm):
	email = forms.EmailField(max_length=60, help_text="Required. Add a valid email address")
	org_name = forms.CharField(max_length=100)

	class Meta:
		model = Account
		fields = ("full_name","email","organisation_name", "password1", "password2")


class AccountAuthentication(forms.ModelForm):
	password = forms.CharField(label='Password', widget=forms.PasswordInput)

	class Meta:
		model = Account
		fields = ('email', 'password')

	def clean(self):
		if self.is_valid():
			email = self.cleaned_data['email']
			password = self.cleaned_data['password']
			if not authenticate(email=email, password=password):
				raise forms.ValidationError("Invalid Login")