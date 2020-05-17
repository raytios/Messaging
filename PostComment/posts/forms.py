from django import forms
from pagedown.widgets import PagedownWidget

from .models import Post, Employee

class PostForm(forms.ModelForm):
    message = forms.CharField(widget=PagedownWidget)

    class Meta:
        model = Post
        fields = ["message"]

class ReplyForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ["message"]