def decorator(func):
    def inner():
        print('Начало декоратора')
        func()
        print('Конец декоратора')

    return inner

def say():
    print('Привет мир!')

def bye():
    print('Пока мир!')

# Декоратор, который принимает аргументы
def decorator(func):
    def inner(*args, **kwargs):
        print('Начало декоратора')
        func(*args, **kwargs)
        print('Конец декоратора')
    return inner
# Принимает 2 аргумента на вход
def sey(name, lastname):
    print('Привет', name, lastname)
sey = decorator(sey)
sey('Иван','Иванов')
# 3 аргумента на вход
def sey(name, lastname, age):
    print('Привет', name, lastname, age)
sey = decorator(sey)
sey('Иван','Иванов', 30)

# Рассмотрю пример с навешивание двух деокаторов да еще и в формате HTML-документа
def header(func):
    def inner(*args, **kwargs):
        print('<h1>')
        func(*args, **kwargs)
        print('</h1>')
    return inner

def table(func):
    def inner(*args, **kwargs):
        print('<table>')
        func(*args, **kwargs)
        print('</table>')
    return inner

# навешиваю декоратор с помощью @
@header
def say(name, surname, age):
    print('hello', name, surname, age)
say('Vasya', 'Ivanov', 30)

@table
def say(name, surname, age):
    print('hello', name, surname, age)
say('Vasya', 'Ivanov', 30)


def html(func):
    def inner(*args, **kwargs):
        print('<body>')
        func(*args, **kwargs)
        print('</body>')
    return inner

@html # = webSite = html(webSite)
def webSite(header, content, footer):
    print(header, content, footer)






