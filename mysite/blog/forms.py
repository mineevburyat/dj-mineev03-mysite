from django import forms
from .models import Post



class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'slug', 'body', 'publish', 'categories']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            # 'body': ProseEditorFormField(),
        }