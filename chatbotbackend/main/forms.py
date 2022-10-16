from django import forms

class MessageForm(forms.Form):
    user = forms.CharField(label = "", max_length = 200)

class EmailForm(forms.Form):
    user = forms.CharField(label="", max_length = 500)

