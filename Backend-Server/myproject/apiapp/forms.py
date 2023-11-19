from django import forms


class RequestForm(forms.Form):
    user_name = forms.CharField(widget=forms.Textarea)
    request_text = forms.CharField(widget=forms.Textarea)
    recipes_to_receive = forms.IntegerField()
