from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'website', 'message']
        widget = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'website', 'type': 'url'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'website': forms.TextInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'cols': 30, 'rows': 10})
        }
