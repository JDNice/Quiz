from Quiz_app.models import *
from django import forms


class AnswerForm(forms.Form):
    class Meta:
        choices = forms.TextInput()
