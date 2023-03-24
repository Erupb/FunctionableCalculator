from django import forms
from django.contrib.auth.forms import AuthenticationForm



class ValuteForm(forms.Form):
    valuteList = [
        ('RUB', "Российский рубль"),
        ('USD', "Доллар США"),
        ('EUR', "Евро"),
        ('AUD', "Австралийский доллар"),
        ('AZN', "Азербайджанский манат"),
        ('GBP', "Фунт стерлингов"),
        ('AMD', "Армянский драм"),
        ('BYN', "Белорусский рубль"),
        ('BGN', "Болгарский лев"),
        ('BRL', "Бразильский реал"),
        ('HUF', "Венгерский форинт"),
        ('HKD', "Гонконгский доллар"),
        ('DKK', "Датская крона"),
        ('INR', "Индийская рупия"),
        ('KZT', "Казахстанский тенге"),
        ('CAD', "Канадский доллар"),
        ('KGS', "Киргизский сом"),
        ('CNY', "Жэньминьби"),
        ('MDL', "Молдавский лей"),
        ('NOK', "Норвежская крона"),
        ('PLN', "Польский злотый"),
        ('RON', "Румынский лей"),
        ('SGD', "Сингапурский доллар"),
        ('TJS', "Таджикский сомони"),
        ('TRY', "Турецкая лира"),
        ('TMT', "Туркменский манат"),
        ('UZS', "Узбекский сум"),
        ('UAH', "Украинская гривна"),
        ('CZK', "Чешская крона"),
        ('SEK', "Шведская крона"),
        ('CHF', "Швейцарский франк"),
        ('ZAR', "Южноафриканский рэнд"),
        ('KRW', "Южнокорейская вона"),
        ('JPY', "Японская иена"),
        

    ]
    fromValute = forms.TypedChoiceField(choices=valuteList, label="Из валюты")
    quantity = forms.IntegerField(label="Количество")
    toValute = forms.TypedChoiceField(choices=valuteList, label="Перевести в")


class RegistrationForm(forms.Form):
    login = forms.CharField(
        label='Логин',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': "uk-input uk-form-success",
                'minlength': "4"
            }
        )
    )
    email = forms.EmailField(
        label='E-mail',
        required=True,
        widget=forms.EmailInput(
            attrs={
                'class': "uk-input  uk-form-success"
            }
        )
    )
    password1 = forms.CharField(
        label='Пароль',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': "uk-input  uk-form-success",
                'minlength': "8",
            }
        )
    )
    password2 = forms.CharField(
        label='Подтверждение пароля',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': "uk-input  uk-form-success",
                'minlength': "8"
            }
        )
    )
    first_name = forms.CharField(
        label='Имя',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': "uk-input  uk-form-success"
            }
        )
    )
    last_name = forms.CharField(
        label='Фамилия',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': "uk-input  uk-form-success"
            }
        )
    )


class IntegralForm(forms.Form):
    range_max = forms.IntegerField(
        label='Максимальное значение',
        required=True,
        widget=forms.NumberInput(
            attrs={
                'class': 'uk-column-1-4 uk-input',
                'placeholder': 'a',
                'id': 'range_max',
            }
        )
    )

    formula = forms.CharField(
        label='Формула',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': "uk-width-1-2@s uk-input uk-form-width-large",
                'placeholder': 'f(x)',
                'id': 'formula',
            }
        )
    )

    range_min = forms.IntegerField(
        label='Минимальное значение',
        required=True,
        widget=forms.NumberInput(
            attrs={
                'class': 'uk-column-1-4 uk-input',
                'placeholder': 'b',
                'id': 'range_min',
            }))
    result = forms.CharField(
        required=False,
        )


class StereometryForm(forms.Form):
    first = forms.IntegerField(
        label='Первое число',
        max_value=1000,
        min_value=0,
        required=True,
        widget=forms.NumberInput(
            attrs={
                'style': 'margin-bottom:10px;',
                'class': "uk-input",
                'id': "firstval",
                'placeholder': 'Введите число'
            }
        )
    )
    second = forms.IntegerField(
        label='Второе число',
        max_value=1000,
        min_value=0,
        required=True,
        widget=forms.NumberInput(
            attrs={
                'class': "uk-input",
                'id': "secondval",
                'placeholder': 'Введите число'
            }
        )
    )
    third = forms.FloatField(
        label='Третье число',
        max_value=1000,
        min_value=0,
        required=True,
        widget=forms.NumberInput(
            attrs={
                'style': 'margin-bottom:10px;',
                'class': "uk-input",
                'id': "thirdval",
                'placeholder': 'Введите число'
            }
        )
    )

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Логин',
        required=True,
        widget=forms.TextInput(
            attrs={
            'class': "uk-input",
            'style': 'width:1000px;',
            'minlength': "8",
            }
        )
    )
    password = forms.CharField(
        label='Пароль',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': "uk-input",
                'style': 'width:1000px;',
                'minlength': "4",
            }
        )
    )


class StereometryCubeForm(forms.Form):
    cube_edge_size = forms.IntegerField(
        label='Ребро куба',
        widget=forms.NumberInput(
            attrs={
                'class': 'uk-input',
                'id': 'cube_edge_size',
                'placeholder': 'Введите целое число',
            }
        )
    )


class StereometryCubeResultForm(forms.Form):
    cube_square = forms.CharField(
        label='Площадь поверхности',
        widget=forms.TextInput(
            attrs={
                'class': 'uk-input',
                'disabled': 'true',
                'id': 'cube_square',
                'placeholder': 'Значение не вычислено',
            }
        )
    )
    cube_volume = forms.CharField(
        label='Объём куба',
        widget=forms.TextInput(
            attrs={
                'class': 'uk-input',
                'disabled': 'true',
                'id': 'cube_volume',
                'placeholder': 'Значение не вычислено',
            }
        )
    )


class StereometryParallelepipedForm(forms.Form):
    pp_square = forms.IntegerField(
        label='Площадь основания',
        widget=forms.NumberInput(
            attrs={
                'class': 'uk-input',
                'id': 'pp_square',
                'placeholder': 'Введите целое число',
            }
        )
    )
    pp_height = forms.IntegerField(
        label='Высота',
        widget=forms.NumberInput(
            attrs={
                'class': 'uk-input',
                'id': 'pp_height',
                'placeholder': 'Введите целое число',
            }
        )
    )


class StereometryParallelepipedResultForm(forms.Form):
    pp_volume = forms.CharField(
        label='Объём параллелепипеда',
        widget=forms.TextInput(
            attrs={
                'class': 'uk-input',
                'disabled': 'true',
                'id': 'pp_volume',
                'placeholder': 'Значение не вычислено',
            }
        )
    )


class StereometryPrParallelepipedForm(forms.Form):
    pr_a = forms.IntegerField(
        label='Ребро A',
        widget=forms.NumberInput(
            attrs={
                'class': 'uk-input',
                'id': 'pr_a',
                'placeholder': 'Введите целое число',
            }
        )
    )
    pr_b = forms.IntegerField(
        label='Ребро B',
        widget=forms.NumberInput(
            attrs={
                'class': 'uk-input',
                'id': 'pr_b',
                'placeholder': 'Введите целое число',
            }
        )
    )
    pr_c = forms.IntegerField(
        label='Ребро C',
        widget=forms.NumberInput(
            attrs={
                'class': 'uk-input',
                'id': 'pr_c',
                'placeholder': 'Введите целое число',
            }
        )
    )


class StereometryPrParallelepipedResultForm(forms.Form):
    pr_side_square = forms.CharField(
        label='Площадь боковой поверхности',
        widget=forms.TextInput(
            attrs={
                'class': 'uk-input',
                'disabled': 'true',
                'id': 'pr_side_square',
                'placeholder': 'Значение не вычислено',
            }
        )
    )
    pr_square = forms.CharField(
        label='Площадь поверхности',
        widget=forms.TextInput(
            attrs={
                'class': 'uk-input',
                'disabled': 'true',
                'id': 'pr_square',
                'placeholder': 'Значение не вычислено',
            }
        )
    )
    pr_volume = forms.CharField(
        label='Объём параллелепипеда',
        widget=forms.TextInput(
            attrs={
                'class': 'uk-input',
                'disabled': 'true',
                'id': 'pr_volume',
                'placeholder': 'Значение не вычислено',
            }
        )
    )


class StereometryPrismForm(forms.Form):
    prism_square = forms.IntegerField(
        label='Площадь основания',
        widget=forms.NumberInput(
            attrs={
                'class': 'uk-input',
                'id': 'prism_square',
                'placeholder': 'Введите целое число',
            }
        )
    )
    prism_height = forms.IntegerField(
        label='Высота',
        widget=forms.NumberInput(
            attrs={
                'class': 'uk-input',
                'id': 'prism_height',
                'placeholder': 'Введите целое число',
            }
        )
    )


class StereometryPrismResultForm(forms.Form):
    prism_volume = forms.CharField(
        label='Объём призмы',
        widget=forms.TextInput(
            attrs={
                'class': 'uk-input',
                'disabled': 'true',
                'id': 'prism_volume',
                'placeholder': 'Значение не вычислено',
            }
        )
    )
