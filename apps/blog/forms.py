from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text', 'email']
        widgets = {
            'text': forms.Textarea(attrs={
                'class': 'form-control w-100',
                'placeholder': 'Comment: '
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email: '
            })
        }