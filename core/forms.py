from django import forms
from . import models

class BirthdayWishForm(forms.ModelForm):
    class Meta:
        model = models.BirthdayWish
        fields = '__all__'