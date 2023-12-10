from django import forms

from blogapp.models import Post


class PostCreateModelForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('views', 'slug',)


