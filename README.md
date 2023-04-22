# Проект "FunctionableCalculator"

### Цель
Предоставить пользователю сервис, на котором можно произвести различные математические вычисления

### Технологический стек:
- python 3.6
- django 3.0+
- sqlite 3.22+

### Инструкция по настройке проекта:
1. Склонировать проект
2. Открыть проект в PyCharm с наcтройками по умолчанию
3. Создать виртуальное окружение (через settings -> project "simple votings" -> project interpreter)
4. Открыть терминал в PyCharm, проверить, что виртуальное окружение активировано.
5. Обновить pip:
```bash
pip install --upgrade pip
```
6. Установить в виртуальное окружение необходимые пакеты: 
```bash
pip install -r requirements.txt
```
7. Синхронизировать структуру базы данных с моделями: 
```bash
python manage.py migrate
```
8. Создать суперпользователя
```bash
$ python manage.py createsuperuser --username vasya --email 1@abc.net
Password: promprog
Password (repeat): promprog
```
9. Создать конфигурацию запуска в PyCharm (файл `manage.py`, опция `runserver`)

# FunctionableCalculator
## Руководство пользователя

#### Описание

_FunctionableCalculator_ - веб приложение позволяющее понятным и удобным способом выполнять математические вычисления различного рода сложности
___

#### Основные возможности
__Аккаунт__
* Регистрация пользователя.
    * Для регистрации необходимо перейти в раздел _регистрация_. Ввести надежные логин и пароль, и создать аккаунт. 
* Авторизация пользоватлея.
    * Для авторизации нужно перейти в раздел _вход в аккаунт_. Ввести данные учетной записи. Далее будет предоставлен доступ в аккаутн пользователя.

__История вычисления__
* Сохранение истории вычислений.
  Каждое совершенное пользователем вычисление записывается в _историю_ и в дальнейшем может быть просмотрено. Функция требует наличия аккаунта и авторизации

__Математические вычисления__
Приложение поддерживает выполнение множества различных математических операций. Все они перечилсены ниже. 
* На данный момент в приложении доступны следующие типы вычислений
    * Обычный кальнулятор
    * Решение уравнений
    * Вычисление объемов и площадей стереометрических фигур
    * Подсчет факториалов
    * Вычисление тригонометрических функций
    * Курс валют и конвертация валют
    * Подсчет первообразной первого порядка
    * Построение графиков функций
    * Преобразование из одной системы счисления в другую
    * Подсчет интегралов

__Информация о проекте и обратная связь__
На главной странице ресурса доступна сводная информация о проекте, а так же контактные данные для обратной связи.