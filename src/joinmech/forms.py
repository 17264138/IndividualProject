from django import forms
from .models import Join

#form using Django form technique
class EmailForm(forms.Form):
	name=forms.CharField(required=False)
	email=forms.EmailField()

#specifies which fields to show on homepage
class JoinForm(forms.ModelForm):
	class Meta:
		model = Join
		fields =["email",]