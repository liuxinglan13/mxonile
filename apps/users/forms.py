# _*_ coding: utf-8 _8_
from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(required=True)  #验证非空
    password = forms.CharField(required=True, min_length=5)  #验证非空，字符串不小于5