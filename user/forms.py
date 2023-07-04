import django
from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm

data_processing_consent_choices = (
    (1, 'Yes'),
    (0, 'No')
)
content_familiar_choices = (
    (1, 'Yes'),
    (0, 'No')
)

sex_choices = (
    ('M', 'Male'),
    ('F', 'Female')
)
age_choices = (
    ('', 'Choose...'),
    (1, '18-35'),
    (2, '35-60'),
    (3, '60+')
)
income_choices = (
    ('', 'Choose...'),
    (1, 'Low'),
    (2, 'Medium'),
    (3, 'High')
)
marital_status_choices = (
    (1, 'Married'),
    (0, 'Single')
)
children_status_choices = (
    (1, 'I have children'),
    (0, 'I have no children')
)
education_choices = (
    ('', 'Choose...'),
    (1, 'Complete secondary'),
    (2, 'Bachelor`s degree'),
    (3, 'Master`s degree')
)
degree_choices = (
    (1, 'Yes'),
    (0, 'No')
)
driving_experience_choices = (
    ('', 'Choose...'),
    (1, 'None'),
    (2, 'Less than 1 year'),
    (3, '1-2 years'),
    (4, '3-4 years'),
    (5, '5-10 years'),
    (6, '10+ years'),
)
working_organization_choices = (
    ('', 'Choose...'),
    (1, 'Budget'),
    (2, 'Commercial'),
    (3, 'Not working/student'),
)
district_choices = (
    ('', 'Choose...'),
    (1, 'Малиновський'),
    (2, 'Приморський'),
    (3, 'Київський'),
    (4, 'Суворовський')
)
petrol_station_nearby_choices = (
    (1, 'Yes'),
    (0, 'No')
)
dwelling_choices = (
    ('', 'Choose...'),
    (1, 'Private house'),
    (2, 'Flat'),
)
work_risk_choices = (
    (1, 'Yes'),
    (0, 'No')
)
station_nearby_work_choices = (
    (1, 'Yes'),
    (0, 'No')
)
station_nearby_house_choices = (
    (1, 'Yes'),
    (0, 'No')
)


class MyRadioSelect(django.forms.RadioSelect):
    option_template_name = "user/widgets/radio_option.html"


class UserRegisterForm(UserCreationForm):
    data_processing_consent = forms.IntegerField(widget=MyRadioSelect(choices=data_processing_consent_choices,
                                                                      attrs={'class': 'custom-control-input',
                                                                             'name': 'data_processing_consent'}))
    content_familiar = forms.IntegerField(widget=MyRadioSelect(choices=content_familiar_choices,
                                                               attrs={'class': 'custom-control-input',
                                                                      'name': 'content_familiar'}))

    name = forms.CharField(widget=forms.TextInput(
        attrs={'type': "text", 'class': "form-control", 'id': "Name", 'placeholder': 'Your answer'}))
    sex = forms.CharField(label="Стать", widget=MyRadioSelect(choices=sex_choices,
                                                              attrs={'class': 'custom-control-input',
                                                                     'name': 'sex'}))
    age = forms.IntegerField(label="Вік", widget=forms.Select(choices=age_choices,
                                                              attrs={'class': 'custom-select d-block w-100',
                                                                     'id': 'age',
                                                                     'name': 'age'}))
    income = forms.IntegerField(label="Дохід", widget=forms.Select(choices=income_choices,
                                                                   attrs={'class': 'custom-select d-block w-100',
                                                                          'id': 'income'}))
    marital_status = forms.IntegerField(label="Сімейний стан", widget=MyRadioSelect(choices=marital_status_choices,
                                                                                    attrs={
                                                                                        'class': 'custom-control-input',
                                                                                        'name': 'marital_status'}))
    children_status = forms.IntegerField(label="Наявність дітей", widget=MyRadioSelect(choices=children_status_choices,
                                                                                       attrs={
                                                                                           'class': 'custom-control-input',
                                                                                           'name': 'children_status'}))

    education = forms.IntegerField(label="Освіта", widget=forms.Select(choices=education_choices,
                                                                       attrs={'class': 'custom-select d-block w-100',
                                                                              'id': 'education'}))
    degree = forms.IntegerField(label="Науковий ступінь", widget=MyRadioSelect(choices=degree_choices,
                                                                               attrs={
                                                                                   'class': 'custom-control-input',
                                                                                   'name': 'degree'}))
    driving_experience = forms.IntegerField(label="Досвід користування автомобілем",
                                            widget=forms.Select(choices=driving_experience_choices,
                                                                attrs={'class': 'custom-select d-block w-100',
                                                                       'id': 'driving_experience'}))

    technical_education_direction = forms.BooleanField(label="Technical", required=False,
                                                       widget=forms.CheckboxInput(
                                                           attrs={'class': 'custom-control-input', 'id': 'technical',
                                                                  'name': 'education_direction'}))
    economical_education_direction = forms.BooleanField(label="Economic", required=False,
                                                        widget=forms.CheckboxInput(
                                                            attrs={'class': 'custom-control-input', 'id': 'economical',
                                                                   'name': 'education_direction'}))
    environmental_education_direction = forms.BooleanField(label="Environmental", required=False,
                                                           widget=forms.CheckboxInput(
                                                               attrs={'class': 'custom-control-input',
                                                                      'id': 'environmental',
                                                                      'name': 'education_direction'}))
    humanitarian_education_direction = forms.BooleanField(label="Humanitarian", required=False,
                                                          widget=forms.CheckboxInput(
                                                              attrs={'class': 'custom-control-input',
                                                                     'id': 'humanitarian',
                                                                     'name': 'education_direction'}))
    work_risk = forms.IntegerField(
        label="Чи пов’язана ваша проф. діяльність з ризиком, або його оцінкою чи управлінням?",
        widget=MyRadioSelect(choices=work_risk_choices,
                             attrs={
                                 'class': 'custom-control-input',
                                 'name': 'work_risk'}))
    station_nearby_work = forms.IntegerField(label="Чи розташовано АЗС поблизу місця Вашої роботи?",
                                             widget=MyRadioSelect(choices=station_nearby_work_choices,
                                                                  attrs={
                                                                      'class': 'custom-control-input',
                                                                      'name': 'station_nearby_work'}))
    station_nearby_house = forms.IntegerField(label="Чи розташовано АЗС поблизу місця Вашого житла?",
                                              widget=MyRadioSelect(choices=station_nearby_house_choices,
                                                                   attrs={
                                                                       'class': 'custom-control-input',
                                                                       'name': 'station_nearby_house'}))

    email = forms.EmailField(label="Email для зворотнього зв'язку", max_length=254,
                             help_text='Required. Enter the valid email.',
                             required=True,
                             widget=forms.TextInput(attrs={'type': "email", 'class': "form-control", 'id': "email",
                                                           'placeholder': 'Your answer'}))

    class Meta:
        model = User
        fields = ('data_processing_consent', 'content_familiar', 'name', 'sex', 'age', 'income', 'marital_status',
                  'children_status', 'education', 'degree',
                  'driving_experience', 'technical_education_direction', 'economical_education_direction',
                  'environmental_education_direction', 'humanitarian_education_direction', 'work_risk',
                  'station_nearby_work', 'station_nearby_house', 'email')
        widgets = {'boolfield': 'marital_status'}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].required = False
        self.fields['password2'].required = False
