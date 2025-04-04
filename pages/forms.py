from django import forms
from django.contrib.auth.forms import AdminUserCreationForm, UserChangeForm, SetPasswordForm
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from pages.models import CustomUser, Songs, News, Gallery, Links


class CustomUserCreationForm(AdminUserCreationForm):

    class Meta:
        model = CustomUser
        fields = ("first_name", "last_name", "username", "email")

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ("username", "email")

class RegistrationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        )

class ChangePasswordForm(SetPasswordForm):
    class Meta:
        model = CustomUser
        fields = ['new_password1', 'new_password2']

    def __init__ (self, *args, **kwargs):
        super(ChangePasswordForm, self).__init__(*args, **kwargs)

        self.fields['new_password1'].widget.attrs['class'] = 'form-control'
        self.fields['new_password1'].widget.attrs['placeholder'] = 'Password'

        self.fields['new_password2'].widget.attrs['class'] = 'form-control'
        self.fields['new_password2'].widget.attrs['placeholder'] = 'Confirm Password'

class SongsForm(ModelForm):
    class Meta:
        model = Songs
        fields = ('title', 'description', 'is_set', 'file')

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Title'}),
            'description': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Description'}),
        }


class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = ('heading', 'content_text', 'image_file', 'article_created_at')

        widgets = {
            'heading': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Heading'}),
            'content_text': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Description'}),
        }

class GalleryForm(ModelForm):
    class Meta:
        model = Gallery
        fields = ('heading', 'content_text', 'image_file', 'article_created_at')

        widgets = {
            'heading': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Heading'}),
            'content_text': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Description'}),
        }

class LinkForm(ModelForm):
    class Meta:
        model = Links
        fields = ('link_name', 'description')

        widgets = {
            'link_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Link'}),
            'description': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Description'}),
        } 