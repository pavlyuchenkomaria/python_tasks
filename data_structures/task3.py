# DICT

import sys
from collections import defaultdict
from collections import OrderedDict


def read_files():
    """
    Считывает данные из файла, формат данных:
    apple - malum, pomum, popula
    :return: англо-латинский словарь
    """
    file_names = sys.argv[1:]
    d = defaultdict(set)
    for file in file_names:
        f = open(file, "r")
        for line in f:
            words = line.split(" - ")
            d[words[0]].update((words[1].rstrip().split(", ")))
        f.close()
    return d


def convert_dict(d):
    """
    Создает из англо-латинского латино-английский словарь, оставляя
    только уникальные слова.
    :param d: считанный из данных словарь
    :return: упорядоченный по алфовиту латино-английский словарь
    """
    res_d = defaultdict(set)
    for key, values in d.items():
        for value in values:
            res_d[value].add(key)
    return OrderedDict(sorted(res_d.items()))


def print_dict(res_d):
    """
    Печатает словарь в заданном виде.
    :param res_d: словарь
    """
    for key, values in res_d.items():
        val = ", ".join(values)
        print(f'{key} - {val}')


def dict_conversion():
    """
    Запускает функции по очереди.
    """
    d = read_files()
    res_d = convert_dict(d)
    print_dict(res_d)


dict_conversion()
