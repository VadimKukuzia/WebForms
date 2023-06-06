from django import forms
from .models import *


class EconomicBlastShockWaveForm(forms.ModelForm):
    class Meta:
        model = EconomicBlastShockWave
        fields = '__all__'
        exclude = ['author']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['adding_factors'].required = False
        self.fields['additional_comment'].required = False
