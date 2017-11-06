from django import forms

class SignupForms(forms.Form):
    email = forms.CharField(label="<b>Email</b>", placeholder="Enter Email")
    pws = forms.PasswordInput(label="<b>Password</b>", placeholder="Enter Password")
    psw-repeat = forms.PasswordInput(label="<b>Repeat Password</b>", placeholder="Repeat Password")
    Uname = forms.CharField(label="<b>Username</b>", placeholder="Enter Username")
    #pic = forms.ImageField()
