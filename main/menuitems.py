from abc import ABC


class Menuitem(ABC):
    url = 'Define me!'
    name = 'Define me!'
    text = 'Define me!'
    image = None


class ElMathMenuItem(Menuitem):
    url = 'elementary_mathematics'
    name = 'Калькулятор'
    text = 'Просто калькулятор'
    image_path = 'images/mainmenu_shortcut/loga_elementory.png'


class TrigonometryMenuItem(Menuitem):
    url = 'trigonometry'
    name = 'Тригонометрия'
    text = 'sin<sup>2</sup>(x) + cos<sup>2</sup>(x) = 1'
    image_path = 'images/mainmenu_shortcut/loga_trigonometry.png'


class GraphicMenuItem(Menuitem):
    url = 'graphic'
    name = 'Построение графиков'
    text = 'Создание графика по вашим данным'
    image_path = 'images/mainmenu_shortcut/loga_diagram.png'


class EquationMenuItem(Menuitem):
    url = 'equation'
    name = 'Уравнения'
    text = 'ax<sup>2</sup> + bx + c = 0'
    image_path = 'images/mainmenu_shortcut/loga_equation.png'


class ValuteMenuItem(Menuitem):
    url = 'currency'
    name = 'Курс валют'
    text = 'Узнайте курс валют'
    image_path = 'images/mainmenu_shortcut/loga_valute.png'


class NumberSystemMenuItem(Menuitem):
    url = 'number_system'
    name = 'Системы Счисления'
    text = '25<sub>10</sub> = 11001<sub>2</sub>'
    image_path = 'images/mainmenu_shortcut/loga_systemnum.png'


class StereometryMenuItem(Menuitem):
    url = 'stereometry'
    name = 'Стереометрия'
    text = 'DEFINE ME!'
    image_path = 'images/mainmenu_shortcut/loga_stereometry.png'


class AntiderivativeMenuItem(Menuitem):
    url = 'antiderivative'
    name = 'Первообразная'
    text = 'Производная первого порядка'
    image_path = 'images/mainmenu_shortcut/loga_antiderivative.png'


class IntegralMenuItem(Menuitem):
    url = 'integral'
    name = 'Интегралы'
    text = 'Определённые интегралы'
    image_path = 'images/mainmenu_shortcut/loga_integral.png'


class StereometryMenuItem(Menuitem):
    url = 'stereometry'
    name = 'Стереометрия'
    text = 'Посчитайте площали и объемы фигур'
    image_path = 'images/mainmenu_shortcut/loga_stereometry.png'


class FactorialMenuItem(Menuitem):
    url = 'factorial'
    name = 'Факториалы'
    text = 'С легкостью посчитайте факториал'
    image_path = 'images/mainmenu_shortcut/loga_factorial.png'
