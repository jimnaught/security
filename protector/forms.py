from django import forms
from . import models
from django.forms import TextInput, Textarea


class ClientsMessagesForm(forms.ModelForm):
    class Meta:
        model = models.ClientsMessages
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget = TextInput(
            attrs={
                'placeholder': 'Enter your name',
                'required': 'required',
            }
        )
        self.fields['phone'].widget = TextInput(
            attrs={
                'placeholder': 'Enter your contacts',
                'required': 'required',
            }
        )
        self.fields['email'].widget = TextInput(
            attrs={
                'placeholder': 'Enter your email',
                'required': 'required',
            }
        )
        self.fields['subject'].widget = TextInput(
            attrs={
                'placeholder': 'Enter your subject',
                'required': 'required',
            }
        )
        self.fields['message'].widget = Textarea(
            attrs={
                'placeholder': 'Enter your message',
                'required': 'required',
                'cols': 40,
                'rows':7
            }
        )
