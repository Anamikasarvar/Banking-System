from .models import *
from django import forms


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields=['name','number','email','balance']



class TransferFormm(forms.ModelForm):
    class Meta:
        model = Transfer
        fields = ['sender_name','amount','receiver_name']