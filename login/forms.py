from django import forms
from .models import Book
from  django.contrib.auth import(
		authenticate,
		get_user_model,
		login,
		logout,
		)
user = get_user_model()
class LoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)

	def clean(self,*args,**kwargs):
		username = self.cleaned_data.get("username")
		password = self.cleaned_data.get("password")
		
		if username and password:
			user = authenticate(username=username,password=password)
			if not user:
				raise forms.ValidationError("This user doesnot exists.")

			if not user.check_password(password):
				raise forms.ValidationError("Incorrect password.")

			if not user.is_active:
				raise forms.ValidationError("this user no longer active.")
		return super(LoginForm,self).clean(*args,**kwargs)


class SignupForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model = user
		fields = [
			'first_name',
			'last_name',
			'username',
			'password',	
		]



class PostBook(forms.ModelForm):
	class Meta:
		model=Book
		fields=['title','author','summary']





