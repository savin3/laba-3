from django import forms
from .models import Profile, Post, Comment

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'bio']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Расскажите о себе...'}),
        }

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'rows': 6,
                'placeholder': 'Напишите что-нибудь...',
                'style': 'width: 100%; font-size: 16px;'
            }),
        }
        labels = {
            'content': ''
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'rows': 2,
                'placeholder': 'Напишите комментарий...',
                'style': 'width: 100%; font-size: 14px;'
            }),
        }
        labels = {
            'content': ''
        }