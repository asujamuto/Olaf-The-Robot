from django import forms

class MessageForm(forms.Form):
    user = forms.CharField(label="Write to me", max_length = 200)