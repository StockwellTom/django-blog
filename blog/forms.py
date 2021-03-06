from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class SearchForm(forms.Form):
        search = forms.CharField(max_length=20)
