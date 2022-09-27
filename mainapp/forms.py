from dataclasses import fields
from tkinter import Widget
from django import forms
from .models import student_extra, teacher_extra, admin_extra, question, answers
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm


class teacherFORM(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password', 'email']


class studentFORM(forms.ModelForm):
    required_css_class = "forms"
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={"class": "form-control", "placeholder": "enter Title", 'style': "width: 300px"}))
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={"class": "form-control", "placeholder": "enter Title", 'style': "width: 300px"}))
    username = forms.CharField(widget=forms.TextInput(
        attrs={"class": "form-control", "placeholder": "enter Title", 'style': "width: 300px"}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={"class": "form-control", "placeholder": "enter Title", 'style': "width: 300px"}))
    email = forms.CharField(widget=forms.EmailInput(
        attrs={"class": "form-control", "placeholder": "enter Title", 'style': "width: 300px"}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password', 'email']


class adminFORM(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password', 'email']


class teacherextraForm(forms.ModelForm):
    class Meta:
        model = teacher_extra
        fields = ['profile_pic']


class studentextraForm(forms.ModelForm):
    class Meta:
        model = student_extra
        fields = ['profile_pic']


class adminextraForm(forms.ModelForm):
    class Meta:
        model = admin_extra
        fields = ['profile_pic']


class quationForm(forms.ModelForm):
    required_css_class = "forms"
    Title = forms.CharField(widget=forms.TextInput(
        attrs={"class": "form-control", "placeholder": "enter Title", 'style': "width: 300px"}))
    discription = forms.CharField(widget=forms.Textarea(
        attrs={"class": "form-control", "placeholder": "enter Title", 'style': "height: 100px;width: 600px"}))

    image_q = forms.ImageField(required=False,
                               widget=forms.FileInput(
                                   attrs={"class": "form-control", 'style': "width: 300px"
                                          }
                               ))

    class Meta:
        model = question
        fields = ['Title', 'discription', 'image_q', 'cat_name']


class answerForm(forms.ModelForm):
    answer = forms.CharField(widget=forms.Textarea(
        attrs={"class": "form-control", "placeholder": "enter Title", 'style': "height: 100px;width: 600px"}))

    image_a = forms.ImageField(required=False,
                               widget=forms.FileInput(
                                   attrs={"class": "form-control", 'style': "width: 300px"
                                          }
                               ))

    class Meta:
        model = answers
        fields = ['answer', 'image_a']


class profileForm(forms.ModelForm):
    required_css_class = "forms"
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={"class": "form-control", "placeholder": "enter Title", 'style': "width: 300px"}))
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={"class": "form-control", "placeholder": "enter Title", 'style': "width: 300px"}))
    username = forms.CharField(widget=forms.TextInput(
        attrs={"class": "form-control", "placeholder": "enter Title", 'style': "width: 300px"}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username']


class sprofileform(forms.ModelForm):
    profile_pic = forms.ImageField(required=False,
                                   widget=forms.FileInput(
                                       attrs={"class": "form-control", 'style': "width: 300px"
                                              }
                                   ))

    class Meta:
        model = student_extra
        fields = ['profile_pic']
