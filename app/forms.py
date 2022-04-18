"""
Definition of forms.
"""
from django.db import models
from .models import Comment
from .models import Blog

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Логин'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Пароль'}))

class customerFeedback(forms.Form):
    name = forms.CharField(label='Ваше имя', min_length=2, max_length=50)
    name.widget.attrs.update({'class': 'form-control', 'id' : 'myInput1'})
    city = forms.CharField(label='Ваш город', min_length=2, max_length=50)
    city.widget.attrs.update({'class': 'form-control', 'id' : 'myInput2'})
    gender = forms.ChoiceField(label='Ваш пол',
                               choices=[('1', 'Мужской'), ('2', 'Женский')],
                               widget=forms.RadioSelect, initial=1)
    product = forms.ChoiceField(label="Продукт, который больше всего понравился на сайте",
                                choices = [('1', ''),
                                           ('2', 'Зефирный котик'),
                                           ('3', 'Плюшевый плед'),
                                           ('4', 'Зефирный зайка'),
                                           ('5', 'Куколка'),
                                           ('6', 'Единорожка'),
                                           ('7', 'Ёжик'),
                                           ('8', 'Дракоша'),
                                           ('9', 'Мастер-класс')])
    product.widget.attrs.update({'class': 'form-control', 'id' : 'myInput3'})
    notice = forms.BooleanField(label='Получать новости сайта на e-mail', required=False)
    email = forms.EmailField(label='Ваш e-mail', min_length=5)
    email.widget.attrs.update({'class': 'form-control', 'id' : 'myInput4'})
    message = forms.CharField(label='Отзывы и предложения',required=False,
                              widget=forms.Textarea(attrs={'rows':10, 'cols':40, 'class': 'form-control', 'id' : 'myInput5'}))

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment # используемая модель
        fields = ('text',) # требуется заполнить только поле text
        labels = {'text': "Комментарий"} # метка к полю формы text

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'description', 'content', 'image',)
        labels = {'title': "Заголовок", 'description': "Краткое содержание", 'content': "Полное содержание", 'image': "Картинка"}






