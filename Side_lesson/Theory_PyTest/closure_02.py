# Замыкания Часть 2

def average_numbers():
    numbers = []
    def inner(number):
        # Беру number и помещаю его в список numbers[] с помощью метода .append
        numbers.append(number)
        # Печатаю все что было помещено в список
        print(numbers)
        # Возвращаю сумму всех чисел, деленных на длину списка
        return sum(numbers) / len(numbers)
    return inner


"""
Можно использовать две переменные, вместо списка. 
summa - будет хранить сумму всех чисел введенных в функцию
"""
def average_numbers():
    summa = 0
    count = 0

    def inner(number):
        nonlocal summa
        nonlocal count
        summa = summa + number
        count += 1

        return summa / count

    return inner

# Функция возвращающая разницу во времени старта и вызова функции
from datetime import datetime

def timer():
    start = datetime.now()
    def inner():
        return datetime.now() - start
    return inner

# Та же функция, только с нормальным форматом даты
from time import perf_counter
def timer():
    start = perf_counter()
    def inner():
        return perf_counter() - start
    return inner

# В качестве дз поручено создать функцию, которая считает время между вызовами
def timer_hw():
    start = perf_counter()
    def inner():
        # Готовлюсь изменять время старта
        nonlocal start
        # Отнимаю от настоящего времени время старта и печатаю его
        print(perf_counter()-start)
        # Обновляю время старта 
        start = perf_counter()
    return inner

def add(a, b):
    return a + b

def counter(func):
    count = 0
    def inner(*args, **kwargs):
        nonlocal count
        count +=1
        print(f"Функция {func.__name__} вызывалась {count} раз")
        return func(*args, **kwargs)
    return inner




