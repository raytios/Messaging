from django import forms
from pagedown.widgets import PagedownWidget

from .models import Collaborate_Messaging_A00

class PostForm(forms.ModelForm):
    message = forms.CharField(widget=PagedownWidget)

    class Meta:
        model = Collaborate_Messaging_A00
        fields = ["message"]

class ReplyForm(forms.ModelForm):

    class Meta:
        model = Collaborate_Messaging_A00
        fields = ["message"]