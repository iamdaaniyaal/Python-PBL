from django import forms

class First(forms.Form):
	answer	 = forms.CharField(max_length=500,widget=forms.TextInput(attrs={'size':50}),required=True,label='')	