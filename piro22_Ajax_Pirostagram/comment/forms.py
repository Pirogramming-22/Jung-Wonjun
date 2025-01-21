from django import forms
from .models import Comment

class Commentform(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 4, 'placeholder': '댓글을 작성하세요...'}),
        }