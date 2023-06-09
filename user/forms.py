import django
from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm

sex_choices = (
    ('M', 'Чоловіча'),
    ('F', 'Жіноча')
)
age_choices = (
    ('', 'Обрати...'),
    (1, '18-35'),
    (2, '35-60'),
    (3, '60+')
)
income_choices = (
    ('', 'Обрати...'),
    (1, 'Маленький'),
    (2, 'Середній'),
    (3, 'Великий')
)
marital_status_choices = (
    (1, 'Одружений'),
    (0, 'Неодружений')
)
children_status_choices = (
    (1, 'Є діти'),
    (0, 'Нема дітей')
)
education_choices = (
    ('', 'Обрати...'),
    (1, 'Повна середня'),
    (2, 'Професійно-технічна'),
    (3, 'Базова вища'),
    (4, 'Повна вища')
)
degree_choices = (
    ('', 'Обрати...'),
    (1, 'Немає'),
    (2, "Кандидат наук(доктор філософії)"),
    (3, 'Доктор наук'),
)
driving_experience_choices = (
    ('', 'Обрати...'),
    (1, 'Немає'),
    (2, 'Менше 1 року'),
    (3, '1-2 роки'),
    (4, '3-4 роки'),
    (5, '5-10 років'),
    (6, '10+ років'),
)
working_organization_choices = (
    ('', 'Обрати...'),
    (1, 'Бюджетна'),
    (2, "Комерційна"),
    (3, 'Не працюю/студент'),
)
district_choices = (
    ('', 'Обрати...'),
    (1, 'Малиновський'),
    (2, 'Приморський'),
    (3, 'Київський'),
    (4, 'Суворовський')
)
petrol_station_nearby_choices = (
    (1, 'Так'),
    (0, 'Ні')
)
dwelling_choices = (
    ('', 'Обрати...'),
    (1, 'Часний будинок'),
    (2, 'Квартира'),
)


class MyRadioSelect(django.forms.RadioSelect):
    option_template_name = "user/widgets/radio_option.html"


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'type': "text", 'class': "form-control", 'id': "Name"}))
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
    degree = forms.IntegerField(label="Науковий ступінь", widget=forms.Select(choices=degree_choices,
                                                                              attrs={
                                                                                  'class': 'custom-select d-block w-100',
                                                                                  'id': 'degree'}))
    driving_experience = forms.IntegerField(label="Досвід користування автомобілем",
                                            widget=forms.Select(choices=driving_experience_choices,
                                                                attrs={'class': 'custom-select d-block w-100',
                                                                       'id': 'driving_experience'}))

    technical_education_direction = forms.BooleanField(label="Технічна", required=False,
                                                       widget=forms.CheckboxInput(
                                                           attrs={'class': 'custom-control-input', 'id': 'technical',
                                                                  'name': 'education_direction'}))
    economical_education_direction = forms.BooleanField(label="Економічна", required=False,
                                                        widget=forms.CheckboxInput(
                                                            attrs={'class': 'custom-control-input', 'id': 'economical',
                                                                   'name': 'education_direction'}))
    environmental_education_direction = forms.BooleanField(label="Екологічна", required=False,
                                                           widget=forms.CheckboxInput(
                                                               attrs={'class': 'custom-control-input',
                                                                      'id': 'environmental',
                                                                      'name': 'education_direction'}))
    humanitarian_education_direction = forms.BooleanField(label="Гуманітарна", required=False,
                                                          widget=forms.CheckboxInput(
                                                              attrs={'class': 'custom-control-input',
                                                                     'id': 'humanitarian',
                                                                     'name': 'education_direction'}))

    working_organization = forms.IntegerField(label="Організація, в якій працюєте",
                                              widget=forms.Select(choices=working_organization_choices,
                                                                attrs={'class': 'custom-select d-block w-100',
                                                                       'id': 'working_organization'}))
    district = forms.IntegerField(label="Район розташування", widget=forms.Select(choices=district_choices,
                                                                attrs={'class': 'custom-select d-block w-100',
                                                                       'id': 'district'}))
    petrol_station_nearby = forms.IntegerField(label="Чи розташовано поблизу АЗС?",
                                               widget=MyRadioSelect(choices=petrol_station_nearby_choices, attrs={
                                                                                           'class': 'custom-control-input',
                                                                                           'name': 'petrol_station_nearby'}))

    dwelling = forms.IntegerField(label="Житло", widget=forms.Select(choices=dwelling_choices,
                                                                attrs={'class': 'custom-select d-block w-100',
                                                                       'id': 'dwelling'}))

    email = forms.EmailField(label="Email для зворотнього зв'язку", max_length=254,
                             help_text='Required. Enter the valid email.',
                             required=True,
                             widget=forms.TextInput(attrs={'type': "email", 'class': "form-control", 'id': "email"}))

    class Meta:
        model = User
        fields = ('username', 'sex', 'age', 'income', 'marital_status', 'children_status', 'education', 'degree',
                  'driving_experience', 'technical_education_direction', 'economical_education_direction',
                  'environmental_education_direction', 'humanitarian_education_direction', 'working_organization',
                  'district', 'petrol_station_nearby', 'dwelling', 'email')
        widgets = {'boolfield': 'marital_status'}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].required = False
        self.fields['password2'].required = False

    def clean_email(self):
        email = self.cleaned_data.get('email')
        user_count = User.objects.filter(email=email).count()

        if not any(i in email for i in ('.ru', '.com', '.ua', '.net')):
            raise forms.ValidationError('Enter the valid email')

        if user_count > 0:
            raise forms.ValidationError('A user with that email already exists.')
        return email
