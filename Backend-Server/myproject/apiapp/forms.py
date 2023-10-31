from django import forms


class RequestForm(forms.Form):
    request_text = forms.CharField(widget=forms.Textarea)
    recipes_to_receive = forms.IntegerField()
