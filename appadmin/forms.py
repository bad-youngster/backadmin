from django import forms


class RegisterForm(forms.Form):
    firstname = forms.CharField()
    lastname = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField()
    verfiypassword = forms.CharField()


class LoginForm(forms.Form):
    username = forms.CharField(
        error_messages={'required': "dont not null"}
    )
    password = forms.CharField(
        min_length=5,
        error_messages={'required': "dont not null",
                        'min_length': "password length not less than 5"}
    )