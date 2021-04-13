from django import forms


class FeedBackForm(forms.Form):
    firstname = forms.CharField(max_length=50, required=True)
    lastname = forms.CharField(max_length=60, required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea, max_length=1000)
    response = forms.BooleanField(required=False)

    firstname.widget.attrs.update({'class' : 'form-control'})
    lastname.widget.attrs.update({'class': 'form-control'})
    email.widget.attrs.update({'class': 'form-control'})
    message.widget.attrs.update({'class': 'form-control'})
