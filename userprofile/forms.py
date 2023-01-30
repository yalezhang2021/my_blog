from django import forms    #引入表单类
from django.contrib.auth.models import User     #引入User

#login form, 继承了 forms.Form class
class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
    

