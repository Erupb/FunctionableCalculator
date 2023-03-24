import datetime
import json

from django.views.decorators.csrf import csrf_exempt
from sympy import *
from django.shortcuts import render
from math import sqrt
from sympy import symbols, integrate
import requests
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from main.forms import IntegralForm, LoginForm
from django_tables2 import RequestConfig

from main.forms import IntegralForm, StereometryCubeForm, StereometryCubeResultForm, StereometryParallelepipedForm, \
    StereometryParallelepipedForm, StereometryParallelepipedResultForm, StereometryPrParallelepipedForm, \
    StereometryPrParallelepipedResultForm, StereometryPrismForm, StereometryPrismResultForm
from main.forms import LoginForm
from main.forms import RegistrationForm
from main.forms import StereometryForm
from main.forms import ValuteForm
from main.menuitems import ElMathMenuItem, TrigonometryMenuItem, GraphicMenuItem, EquationMenuItem, ValuteMenuItem, \
    NumberSystemMenuItem, StereometryMenuItem, AntiderivativeMenuItem, IntegralMenuItem, FactorialMenuItem
from main.models import ElementaryMath, Equation, Antiderivative
from main.models import History
from .tables import HistoryTable


def get_menu_context():
    return [
        {'url_name': 'index', 'name': 'Главная'},
        {'url_name': 'registration', 'name': 'Регистрация'},
    ]


def index_page(request):
    context = {
        'pagename': 'Главная',
        'author': 'Andrew',
        'pages': 4,
        'menu': get_menu_context(),
        'menuitems': [
            ElMathMenuItem,
            TrigonometryMenuItem,
            GraphicMenuItem,
            EquationMenuItem,
            ValuteMenuItem,
            NumberSystemMenuItem,
            StereometryMenuItem,
            AntiderivativeMenuItem,
            IntegralMenuItem,
            FactorialMenuItem,
        ]
    }
    return render(request, 'pages/index.html', context)


def graphic_page(request):
    context = {
        'pagename': 'Графики',
        'menu': get_menu_context()
    }
    return render(request, 'pages/graphic.html', context)


def factorial(request):
    context = {
        'pagename': 'Факторал',
        'menu': get_menu_context()
    }
    return render(request, 'pages/factorial.html', context)


def elementary_mathematics(request):
    context = {
        'pagename': 'Элементарная математика',
        'menu': get_menu_context()
    }
    if request.method == 'POST':
        data = request.POST['data']
        record = ElementaryMath(result=data)
        record.save()
    return render(request, 'pages/elementary_mathematics.html', context)


@login_required
def profile(request):
    all_equations = HistoryTable(History.objects.filter(author_id=request.user.id))
    RequestConfig(request).configure(all_equations)
    print(request.user.email)
    context = {
        'pagename': 'Профиль',
        'menu': get_menu_context(),
        'email': request.user.email,
        'username': request.user.username,
        'first_name': request.user.first_name,
        'last_name': request.user.last_name,
        'last_login': request.user.last_login,
        'all_equations': all_equations
    }
    return render(request, 'pages/profile.html', context)


def equation_page(request):
    context = {
        'pagename': 'Решение уравнений',
        'time': datetime.datetime.now().time(),
        'menu': get_menu_context()
    }
    if request.method == 'POST':
        data = request.POST['data']
        record = Equation(result=data)
        record.save()
    return render(request, 'pages/equation.html', context)


# def currency(request):

def antiderivative_page(request):
    context = {
        'pagename': 'Решение уравнений',
        'time': datetime.datetime.now().time(),
        'menu': get_menu_context()
    }
    if request.method == 'POST':
        data = request.POST['data']
        record = Antiderivative(result=data)
        record.save()
    return render(request, 'pages/antiderivative.html', context)


def currency(request):
    context = {
        'result': ' ',
        'menu': get_menu_context()
    }
    form = ValuteForm()
    context['form'] = form
    if request.POST:
        if request.POST['fromValute'] != 'RUB' and request.POST['toValute'] != 'RUB':
            list = json.loads(requests.get('https://www.cbr-xml-daily.ru/daily_json.js').text)
            rubles = list["Valute"][request.POST['fromValute']]["Value"] * int(request.POST['quantity']) / \
                     list["Valute"][request.POST['fromValute']]["Nominal"]
            to = request.POST['toValute']
            kurs = (rubles / list["Valute"][to]["Value"] * list["Valute"][to]["Nominal"])
            context['result'] = kurs
            if request.user.id:
                save_equation_to_history('Перевод валют', request.user.id, str(
                    request.POST['quantity'] + " " + request.POST['fromValute'] + ' в ' + request.POST['toValute']),
                                         result=kurs)
        if request.POST['fromValute'] == 'RUB':
            list = json.loads(requests.get('https://www.cbr-xml-daily.ru/daily_json.js').text)
            rubles = float(request.POST['quantity'])
            to = request.POST['toValute']
            kurs = (rubles / list["Valute"][to]["Value"] * list["Valute"][to]["Nominal"])
            context['result'] = kurs
            if request.user.id:
                save_equation_to_history('Перевод валют', request.user.id, str(
                    request.POST['quantity'] + " " + request.POST['fromValute'] + ' в ' + request.POST['toValute']),
                                         result=kurs)
        elif request.POST['toValute'] == 'RUB':
            list = json.loads(requests.get('https://www.cbr-xml-daily.ru/daily_json.js').text)
            rubles = float(list["Valute"][request.POST['fromValute']]["Value"] * int(request.POST['quantity']) /
                           list["Valute"][request.POST['fromValute']]["Nominal"])
            context['result'] = rubles
            if request.user.id:
                save_equation_to_history('Перевод валют', request.user.id, str(
                    request.POST['quantity'] + " " + request.POST['fromValute'] + ' в ' + request.POST['toValute']),
                                         result=rubles)
    return render(request, "pages/currency.html", context)


def trigonometry(request):
    context = {
        'pagename': 'Тригонометрия',
        'time': datetime.datetime.now().time(),
        'menu': get_menu_context()
    }
    return render(request, 'pages/trigonometry.html', context)


def registration_user(request):
    context = {'pagename': 'Регистрация', 'menu': get_menu_context(), 'nothing_entered': True}
    context = {'pagename': 'Регистрация', 'menu': get_menu_context(), 'nothing_entered': False}
    context = {'pagename': 'Регистрация', 'menu': get_menu_context(), 'nothing_entered': True}
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if (form.data['password1'] == form.data['password2']) and not form.data['password1'].isdigit() and not \
                form.data['password1'].isupper() and not form.data['password1'].islower():
            if not (User.objects.filter(email=form.data['email']).exists()):
                if not (User.objects.filter(username=form.data['login']).exists()):
                    user = User.objects.create_user(form.data['login'], form.data['email'], form.data['password1'])
                    user.first_name = form.data['first_name']
                    user.last_name = form.data['last_name']
                    user.save()
                    context['error'] = 'Вы успешно зарегистрировались'
                else:
                    context['error'] = 'Этот логин уже занят'
            else:
                context['error'] = 'Этот e-mail уже занят'
        else:
            context[
                'error'] = 'Пароль должен состоять из более 8 символов и иметь хотя бы одну цифру, букву в верхнем регистре и букву в нижнем регистре.'
    else:
        form = RegistrationForm()
        context['nothing_entered'] = True
    context['form'] = form
    return render(request, 'registration/reg.html', context)


def integral(request):
    context = {
        'pagename': 'Интеграл',
        'menu': get_menu_context(),
        'result': ''
    }
    if request.method == 'POST':
        data = json.loads(json.dumps(request.POST))
        x, y, a, b = symbols('x y a b')
        data['formula'] = data['formula'].replace('e', '2.71828')
        data['formula'] = data['formula'].replace('pi', '3.14')
        data['formula'] = data['formula'].replace('^', '**')
        context['result'] = integrate(data['formula'], (x, data['range_min'], data['range_max']))
        save_equation_to_history("Определенный интеграл",
                                 request.user.id,
                                 "{}, {}, {}".format(data['range_min'], data['range_max'], data['formula']),
                                 context['result'])
    else:
        form = IntegralForm()
        context['form'] = form
    return render(request, 'pages/integral.html', context)


def stereometry(request):
    context = {
        'pagename': 'Стереометрия',
        'menu': get_menu_context(),
        'widgets': [
            {
                'name': 'Куб',
                'image': 'images/steriometry/stereometry_cube.png',
                'input': StereometryCubeForm(),
                'js_function': 'cube()',
                'output': StereometryCubeResultForm(),
            },
            {
                'name': 'Призма',
                'image': 'images/steriometry/Prism_image.jpg',
                'input': StereometryPrismForm(),
                'js_function': 'prism()',
                'output': StereometryPrismResultForm(),
            },
            {
                'name': 'Параллелепипед',
                'image': 'images/steriometry/stereometry_paralepiped.png',
                'input': StereometryParallelepipedForm(),
                'js_function': 'parallelepiped()',
                'output': StereometryParallelepipedResultForm(),
            },
            {
                'name': 'Прямоугольный параллелепипед',
                'image': 'images/steriometry/stereometry_rectangular_parallelepiped.png',
                'input': StereometryPrParallelepipedForm(),
                'js_function': 'rectangular_box()',
                'output': StereometryPrParallelepipedResultForm(),
            },

        ]
    }
    if request.method == 'POST':
        form = StereometryForm(request.POST)
        if form.is_valid():
            a = int(form.data['first'])
            b = int(form.data['second'])
            c = int(form.data['third'])
            context['d'] = ''
            context['error'] = 'Ответ: '
            if ((a + b) >= c) and ((a + c) >= b) and ((c + b) >= a):
                d = sqrt((a + b + c) / 2 * ((a + b + c) / 2 - a) * ((a + b + c) / 2 - b) * ((a + b + c) / 2 - c))
                context['a'] = a
                context['b'] = b
                context['c'] = c
                context['d'] = d

            else:
                context['error'] = 'Треугольника с такими сторонами не существует'
    else:
        form = StereometryForm()
        context['nothing_entered'] = True

    context['form'] = form
    return render(request, 'pages/stereometry.html', context)


def number_system(request):
    context = {
        'pagename': 'Number system',
        'time': datetime.datetime.now().time(),
        'menu': get_menu_context()
    }
    return render(request, 'pages/number_system.html', context)

def radix(request):
    context = {
        'pagename': 'Number system',
        'menu': get_menu_context()
    }
    return render(request, 'pages/radix.html', context)


def landing_page(request):
    context = {
        'pagename': 'Welcome to our site',
        'menu': get_menu_context()
    }
    return render(request, 'pages/landing.html', context)


class MyLoginView(LoginView):
    authentication_form = LoginForm


@csrf_exempt
def save_data_to_db(request):
    data = json.loads(json.dumps(request.POST))
    save_equation_to_history(data['operation_type'], data['author_id'], data['equation'], data['result'])
    return 'OK'


def save_equation_to_history(operation_type, author_id, equation, result):
    print(type(author_id))
    if type(result) == int or type(result) == float:
        History(operation_type=operation_type,
                creation_time=str(datetime.datetime.now())[0:19],
                author_id=author_id,
                equation=equation,
                result='%.3f' % result).save()
    else:
        History(operation_type=operation_type, creation_time=str(datetime.datetime.now())[0:19],
                author_id=author_id, equation=equation, result=result).save()
