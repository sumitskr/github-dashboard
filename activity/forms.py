from django import forms

class Git_user_form(forms.Form):
    username = forms.CharField(label='User Name', max_length=20)
    password = forms.PasswordInput()
    git_token = forms.CharField(label="Git Token",min_length=40,max_length=40)
