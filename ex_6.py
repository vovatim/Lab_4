import json
import sys
from librip.ctxmngrs import timer
from librip.decorators import print_result
from librip.gen import *
from librip.iterators import Unique as unique

path = "data_light.json"

# Здесь необходимо в переменную path получить
# путь до файла, который был передан при запуске

with open(path) as f:
    data = json.load(f)


# Далее необходимо реализовать все функции по заданию, заменив `raise NotImplemented`
# Важно!
# Функции с 1 по 3 дожны быть реализованы в одну строку
# В реализации функции 4 может быть до 3 строк
# При этом строки должны быть не длиннее 80 символов

@print_result
def f1(arg):
    return list(unique(list(field(arg, "job-name")), ignore_case=True))


@print_result
def f2(arg):
    return list(filter(lambda _: "Программист" in _, arg))


@print_result
def f3(arg):
    return list(map(lambda x: x + " с опытом Python", arg))


@print_result
def f4(arg):
    random_salaries = gen_random(100000, 200000, len(arg))
    zipped_workers_with_salaries = zip(arg, random_salaries)
    return list(map(lambda x: "{}, зарплата {} руб.".format(x[0], x[1]), zipped_workers_with_salaries))


with timer():
    f4(f3(f2(f1(data))))
