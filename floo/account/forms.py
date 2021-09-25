from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import widgets
from .models import CustomUser
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model

SEX_CHOICES=(('M','남'),('W','여'))
AGE_CHOICES=(('5','10대 이하'),('10','10대'),('20','20대'),('30','30대'),('40','40대'),('50','50대 이상'))

class RegisterForm(UserCreationForm):
    username = forms.CharField(widget = forms.TextInput(attrs={
         "class":"input",
         "type":"username",
         "placeholder":"id",
     }),label="ID", error_messages={'unique' : '입력하신 아이디를 사용하는 유저가 이미 존재합니다',
                                            'max_length' : '아이디는 최대 150글자까지 작성할 수 있습니다'})

    password1 = forms.CharField(widget = forms.TextInput(attrs={
         "class":"input",
         "type":"password",
         "placeholder":"password",
     }),label="password")

    password2 = forms.CharField(widget = forms.TextInput(attrs={
         "class":"input",
         "type":"password",
         "placeholder":"confirm password",
     }),label="password")


    nickname = forms.CharField(widget = forms.TextInput(attrs={
         "class":"input",
         "type":"nickname",
         "placeholder":"닉네임",
     }),label="enter nickname", error_messages={'unique' : '입력하신 닉네임을 사용하는 유저가 이미 존재합니다'},
     required=True)

    sex=forms.ChoiceField(widget=forms.Select(choices='SEX_CHOICES'),label="성별",initial='남')
    
    age=forms.ChoiceField(widget=forms.Select(choices='AGE_CHOICES'),label="나이")

    error_messages = {
        'password_mismatch': '입력하신 두 비밀번호가 같지 않습니다',
    }

    class Meta:
        model = CustomUser
        fields = ['username','password1','password2','sex','age']