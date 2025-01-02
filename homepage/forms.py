from django import forms

class LeadForm(forms.Form):
    name = forms.CharField(max_length=100, label="Name")
    phone = forms.CharField(max_length=15, label="Phone Number")
    message = forms.CharField(widget=forms.Textarea, label="Message")
