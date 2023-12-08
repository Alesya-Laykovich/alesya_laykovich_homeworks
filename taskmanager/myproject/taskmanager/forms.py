from datetime import datetime

from django import forms
from .models import *
from django.forms import ModelForm
from django.db import models
from django.core.exceptions import ValidationError
import re
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-control',
                                                                                       'autocomplete': 'off'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя',
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email',
                             widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Пароль',
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Повторите пароль',
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# class TaskForm(forms.ModelForm):
#     class Meta:
#         model = TaskManager
#         fields = ['title', 'content', 'category', 'priority', 'completed']
#         widgets = {
#             'title': forms.TextInput(attrs={'class': 'form-control'}),
#             'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
#             'category': forms.Select(attrs={'class': 'form-select'}),
#             'priority': forms.Select(attrs={'class': 'form-select'}),
#             'completed': forms.Select(attrs={'class': 'form-select'})
#         }

    # def clean_title(self):
    #     title = self.cleaned_data['title']
    #     if re.match(r'\d', title):
    #         raise ValidationError('Заголовок не может начинаться с цифры')
    #     return title
        # for i in title:
        #     if i == ' ':
        #         continue
        #     if i.isdigit():
        #         raise ValidationError('Заголовок не может начинаться с цифры')
        #     elif not i.isalpha():
        #         raise ValidationError('Заголовок не может содержать спецсимволы')
        # return title

class TaskForm(forms.ModelForm):
    title = forms.CharField(max_length=155, label='Заголовок',
                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    content = forms.CharField(label='Описание', required=False,
                              widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))
    category = forms.ModelChoiceField(queryset=Category.objects.all(), label='Категория',
                                      empty_label='Выберите категорию',
                                      widget=forms.Select(attrs={'class': 'form-select'}))

    priority = forms.ModelChoiceField(queryset=Priority.objects.all(), label='Приоритет',
                                      empty_label='Выберите приоритет',
                                      widget=forms.Select(attrs={'class': 'form-select'}))
    favourite = forms.ModelChoiceField(queryset=Favourite.objects.all(), label='Избранное',
                                      widget=forms.Select(attrs={'class': 'form-select'}), required=False)
    completed_at = forms.DateField(label='Дата завершения', widget=forms.DateInput(format='%d.%m.%Y'), required=False)
    completed = forms.ModelChoiceField(queryset=Completed.objects.all(), label='Статус задачи',
                                      empty_label='Выберите статус',
                                      widget=forms.Select(attrs={'class': 'form-select'}), required=False)

    # completed_at = forms.DateField(label='Дата завершения', widget=forms.DateInput(format='%m/%d/%Y'))
    # def save(self):
    #     task = TaskManager.objects.create(
    #         title=self.cleaned_data['title'],
    #         content=self.cleaned_data['content'],
    #         category=self.cleaned_data['category'],
    #     )
    #     return task
    class Meta:
        model = TaskManager
        fields = ['title', 'content', 'category', 'priority', 'favourite', 'completed', 'completed_at']

    def clean_user(self):
        if not self.cleaned_data['user']:
            return User()
        return self.cleaned_data['user']

class FinishForm(forms.ModelForm):
    completed = forms.ModelChoiceField(queryset=Completed.objects.all(), label='Статус задачи',
                                      empty_label='Выберите статус',
                                      widget=forms.Select(attrs={'class': 'form-select'}))
    completed_at = forms.DateField(label='Дата завершения', widget=forms.DateInput(format='%d.%m.%Y'))
    # def save(self):
    #     task = TaskManager.objects.create(
    #         title=self.cleaned_data['title'],
    #         content=self.cleaned_data['content'],
    #         category=self.cleaned_data['category'],
    #     )
    #     return task
    class Meta:
        model = TaskManager
        fields = ['completed', 'completed_at']

# class CompletedAt(forms.ModelForm):
#     completed = forms.ModelChoiceField(queryset=Completed.objects.all(), label='Статус задачи',
#                                        empty_label='Выберите статус',
#                                        widget=forms.Select(attrs={'class': 'form-select'}))
#     completed_at = forms.DateField(label='Дата завершения', widget=forms.DateInput(format='%d-%m-%Y',
#                                                                                    attrs={'type': 'date'}),
#                                    required=False)
#
#     class Meta:
#         model = CompletedAt
#         fields = '__all__'