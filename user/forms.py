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
    (1, 'Маленький'),
    (2, 'Середній'),
    (3, 'Великий')
)
marital_status_choices = (
    (True, 'Одружений'),
    (False, 'Неодружений')
)
children_status_choices = (
    (True, 'Є діти'),
    (False, 'Нема дітей')
)
education_choices = (
    (1, 'Повна середня'),
    (2, 'Професійно-технічна'),
    (3, 'Базова вища'),
    (4, 'Повна вища')
)
degree_choices = (
    (1, 'Немає'),
    (2, "Кандидат наук(доктор філософії)"),
    (3, 'Доктор наук'),
)
driving_experience_choices = (
    (1, 'Немає'),
    (2, 'Менше 1 року'),
    (3, '1-2 роки'),
    (4, '3-4 роки'),
    (5, '5-10 років'),
    (6, '10+ років'),
)
working_organization_choices = (
    (1, 'Бюджетна'),
    (2, "Комерційна"),
    (3, 'Не працюю/студент'),
)
district_choices = (
    (1, 'Малиновський'),
    (2, 'Приморський'),
    (3, 'Київський'),
    (4, 'Суворовський')
)
petrol_station_nearby_choices = (
    (True, 'Так'),
    (False, 'Ні')
)
dwelling_choices = (
    (1, 'Часний будинок'),
    (2, 'Квартира'),
)


class MyRadioSelect(django.forms.RadioSelect):
    option_template_name = "user/widgets/radio_option.html"


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'type': "text", 'class': "form-control", 'id': "Name"}))
    sex = forms.ChoiceField(label="radio-stacked",
                            widget=MyRadioSelect(
                                attrs={'class': 'custom-control-input'}),
                            choices=sex_choices)
    age = forms.IntegerField(label="Вік", widget=forms.Select(choices=age_choices, attrs={'class': 'custom-select d-block w-100', 'id': 'age'}))
    income = forms.IntegerField(label="Дохід", widget=forms.Select(choices=income_choices))
    marital_status = forms.ChoiceField(label="Сімейний стан", widget=forms.RadioSelect, choices=marital_status_choices)
    children_status = forms.ChoiceField(label="Наявність дітей",
                                        widget=forms.RadioSelect, choices=children_status_choices)

    education = forms.IntegerField(label="Освіта", widget=forms.Select(choices=education_choices))
    degree = forms.IntegerField(label="Науковий ступінь", widget=forms.Select(choices=degree_choices))
    driving_experience = forms.IntegerField(label="Досвід користування автомобілем",
                                            widget=forms.Select(choices=driving_experience_choices))

    technical_education_direction = forms.BooleanField(label="Технічна", required=False)
    economical_education_direction = forms.BooleanField(label="Економічна", required=False)
    environmental_education_direction = forms.BooleanField(label="Екологічна", required=False)
    humanitarian_education_direction = forms.BooleanField(label="Гуманітарна", required=False)

    working_organization = forms.IntegerField(label="Організація, в якій працюєте",
                                              widget=forms.Select(choices=working_organization_choices))
    district = forms.IntegerField(label="Район розташування", widget=forms.Select(choices=district_choices))
    petrol_station_nearby = forms.BooleanField(label="Чи розташовано поблизу АЗС?",
                                               widget=forms.RadioSelect(choices=petrol_station_nearby_choices))

    dwelling = forms.IntegerField(label="Житло", widget=forms.Select(choices=dwelling_choices))

    email = forms.EmailField(label="Email для зворотнього зв'язку", max_length=254,
                             help_text='Required. Enter the valid email.',
                             required=True)

    class Meta:
        model = User
        fields = ('username', 'sex', 'age', 'income', 'marital_status', 'children_status', 'education', 'degree',
                  'driving_experience', 'technical_education_direction', 'economical_education_direction',
                  'environmental_education_direction', 'humanitarian_education_direction', 'working_organization',
                  'district', 'petrol_station_nearby', 'dwelling', 'email')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].required = False
        self.fields['password2'].required = False
        self.fields['sex'].label = 'radio-stacked'

    def clean_email(self):
        email = self.cleaned_data.get('email')
        user_count = User.objects.filter(email=email).count()

        if not any(i in email for i in ('.ru', '.com', '.ua', '.net')):
            raise forms.ValidationError('Enter the valid email')

        if user_count > 0:
            raise forms.ValidationError('A user with that email already exists.')
        return email
