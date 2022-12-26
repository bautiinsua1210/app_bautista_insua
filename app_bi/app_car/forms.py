from django import forms

class ClientForm(forms.Form):
    name= forms.CharField(label="Client's name", max_length=50)
    surnmae= forms.CharField(label="Client's surname", max_length=50)
    email= forms.EmailField(label="Client's email")
    role= forms.CharField(label="Client's role", max_length=50)