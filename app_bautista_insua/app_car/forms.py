from django import forms

class ClientForm(forms.Form):
    name= forms.CharField(label="Client name", max_length=50)
    surname= forms.CharField(label="Client surname", max_length=50)
    email= forms.EmailField(label="Client email")
    job= forms.CharField(label="Client job", max_length=50)

class CarForm(forms.Form):
    brand= forms.CharField(label="Brand", max_length=50)
    model= forms.CharField(label="Model", max_length=50)
    year= forms.IntegerField(label="Year")
    miles= forms.IntegerField(label="miles")

class ServiceForm(forms.Form):
    type= forms.CharField(label="Type", max_length=50)
    time= forms.IntegerField(label="Time")
    price= forms.IntegerField(label="Price")