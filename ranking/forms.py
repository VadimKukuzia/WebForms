from django import forms
from .models import *


# Economical
class EconomicBlastShockWaveForm(forms.ModelForm):
    class Meta:
        model = EconomicBlastShockWave
        fields = '__all__'
        exclude = ['author']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({"class": "form-control form-control-sm", 'min': "1", 'max': '10'})
        self.fields['adding_factors'].required = False
        self.fields['adding_factors'].widget.attrs.update(
            {"class": "form-control", 'id': "adding_factors", 'rows': '1', 'placeholder': 'Optional input'})
        self.fields['additional_comment'].required = False
        self.fields['additional_comment'].widget.attrs.update(
            {"class": "form-control", 'id': "additional_comment", 'rows': '1', 'placeholder': 'Optional input'})


class EconomicFireForm(forms.ModelForm):
    class Meta:
        model = EconomicFire
        fields = '__all__'
        exclude = ['author']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({"class": "form-control form-control-sm", 'min': "1", 'max': '10'})
        self.fields['adding_factors'].required = False
        self.fields['adding_factors'].widget.attrs.update(
            {"class": "form-control", 'id': "adding_factors", 'rows': '1', 'placeholder': 'Optional input'})
        self.fields['additional_comment'].required = False
        self.fields['additional_comment'].widget.attrs.update(
            {"class": "form-control", 'id': "additional_comment", 'rows': '1', 'placeholder': 'Optional input'})


class EconomicBlastFireBallForm(forms.ModelForm):
    class Meta:
        model = EconomicBlastFireBall
        fields = '__all__'
        exclude = ['author']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({"class": "form-control form-control-sm", 'min': "1", 'max': '10'})
        self.fields['adding_factors'].required = False
        self.fields['adding_factors'].widget.attrs.update(
            {"class": "form-control", 'id': "adding_factors", 'rows': '1', 'placeholder': 'Optional input'})
        self.fields['additional_comment'].required = False
        self.fields['additional_comment'].widget.attrs.update(
            {"class": "form-control", 'id': "additional_comment", 'rows': '1', 'placeholder': 'Optional input'})


# Social

class SocialBlastShockWaveForm(forms.ModelForm):
    class Meta:
        model = SocialBlastShockWave
        fields = '__all__'
        exclude = ['author']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({"class": "form-control form-control-sm", 'min': "1", 'max': '10'})
        self.fields['adding_factors'].required = False
        self.fields['adding_factors'].widget.attrs.update(
            {"class": "form-control", 'id': "adding_factors", 'rows': '1', 'placeholder': 'Optional input'})
        self.fields['additional_comment'].required = False
        self.fields['additional_comment'].widget.attrs.update(
            {"class": "form-control", 'id': "additional_comment", 'rows': '1', 'placeholder': 'Optional input'})


class SocialFireForm(forms.ModelForm):
    class Meta:
        model = SocialFire
        fields = '__all__'
        exclude = ['author']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({"class": "form-control form-control-sm", 'min': "1", 'max': '10'})
        self.fields['adding_factors'].required = False
        self.fields['adding_factors'].widget.attrs.update(
            {"class": "form-control", 'id': "adding_factors", 'rows': '1', 'placeholder': 'Optional input'})
        self.fields['additional_comment'].required = False
        self.fields['additional_comment'].widget.attrs.update(
            {"class": "form-control", 'id': "additional_comment", 'rows': '1', 'placeholder': 'Optional input'})


class SocialBlastFireBallForm(forms.ModelForm):
    class Meta:
        model = SocialBlastFireBall
        fields = '__all__'
        exclude = ['author']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({"class": "form-control form-control-sm", 'min': "1", 'max': '10'})
        self.fields['adding_factors'].required = False
        self.fields['adding_factors'].widget.attrs.update(
            {"class": "form-control", 'id': "adding_factors", 'rows': '1', 'placeholder': 'Optional input'})
        self.fields['additional_comment'].required = False
        self.fields['additional_comment'].widget.attrs.update(
            {"class": "form-control", 'id': "additional_comment", 'rows': '1', 'placeholder': 'Optional input'})


# Environmental
class EnvironmentalBlastShockWaveForm(forms.ModelForm):
    class Meta:
        model = EnvironmentalBlastShockWave
        fields = '__all__'
        exclude = ['author']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({"class": "form-control form-control-sm", 'min': "1", 'max': '11'})
        self.fields['adding_factors'].required = False
        self.fields['adding_factors'].widget.attrs.update(
            {"class": "form-control", 'id': "adding_factors", 'rows': '1', 'placeholder': 'Optional input'})
        self.fields['additional_comment'].required = False
        self.fields['additional_comment'].widget.attrs.update(
            {"class": "form-control", 'id': "additional_comment", 'rows': '1', 'placeholder': 'Optional input'})


class EnvironmentalFireForm(forms.ModelForm):
    class Meta:
        model = EnvironmentalFire
        fields = '__all__'
        exclude = ['author']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({"class": "form-control form-control-sm", 'min': "1", 'max': '11'})
        self.fields['adding_factors'].required = False
        self.fields['adding_factors'].widget.attrs.update(
            {"class": "form-control", 'id': "adding_factors", 'rows': '1', 'placeholder': 'Optional input'})
        self.fields['additional_comment'].required = False
        self.fields['additional_comment'].widget.attrs.update(
            {"class": "form-control", 'id': "additional_comment", 'rows': '1', 'placeholder': 'Optional input'})


class EnvironmentalBlastFireBallForm(forms.ModelForm):
    class Meta:
        model = EnvironmentalBlastFireBall
        fields = '__all__'
        exclude = ['author']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({"class": "form-control form-control-sm", 'min': "1", 'max': '11'})
        self.fields['adding_factors'].required = False
        self.fields['adding_factors'].widget.attrs.update(
            {"class": "form-control", 'id': "adding_factors", 'rows': '1', 'placeholder': 'Optional input'})
        self.fields['additional_comment'].required = False
        self.fields['additional_comment'].widget.attrs.update(
            {"class": "form-control", 'id': "additional_comment", 'rows': '1', 'placeholder': 'Optional input'})
