#!/usr/bin/env python3
import sys
from librip.ctxmngrs import json_from_file
from librip.decorators import print_result
from librip.gens import field, gen_random
from librip.iterators import Unique as unique

path = None

# Здесь необходимо в переменную path получить
# путь до файла, который был передан при запуске

with json_from_file(path) as data:
    data = data


# Далее необходимо реализовать все функции по заданию, заменив `raise NotImplemented`
# Важно!
# Функции с 1 по 3 дожны быть реализованы в одну строку
# В реализации функции 4 может быть до 3 строк
# При этом строки должны быть не длиннее 80 символов

@print_result
def func_1(arg):
    raise NotImplemented


@print_result
def func_2(arg):
    raise NotImplemented


@print_result
def func_3(arg):
    raise NotImplemented


@print_result
def func_4(arg):
    raise NotImplemented


func_4(func_3(func_2(func_1(data))))
