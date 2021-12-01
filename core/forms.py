from django import forms
from django.db.models import fields
from . import models

class BirthdayWishForm(forms.ModelForm):
    class Meta:
        model = models.BirthdayWish
        fields = '__all__'

class MessageForm(forms.ModelForm):
    class Meta:
        model = models.Message
        fields = '__all__'

class TransactionFrom(forms.ModelForm):
    class Meta:
        model = models.Transation
        fields = [
            'name',
            'transaction_id',
            'email',
            'amount',
        ]