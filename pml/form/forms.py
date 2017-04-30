from django import forms


class PostForm(forms.Form):
    input_test = forms.CharField(max_length=40)
    input_test2 = forms.CharField(max_length=40)
