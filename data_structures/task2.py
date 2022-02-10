# STRING


def vebing(inp):
    """
    Если длина входной строки по крайней мере 3,
    добавить в конец 'ing', кроме случая, когда строка уже
    заканчивается на 'ing', тогда добавить в конец 'ly'.
    :param inp: строка
    :return: новая строка
    """
    if len(inp) < 3:
        return inp
    else:
        if inp.endswith('ing'):
            inp += 'ly'
        else:
            inp += 'ing'
    return inp


assert 'ab' == vebing('ab'), "Не учтена длина"
assert 'abcingly' == vebing('abcing'), \
    "Строка уже заканчивается на ing"
assert 'ingly' == vebing('ing'), \
    "Строка уже заканчивается на ing"
assert 'abcing' == vebing('abc'), \
    "Строка не заканчивается на ing"


def not_bad(inp):
    """
    Найти первые вхождения подстрок not и bad, если bad следует за not,
    замените всю подстроку not ... bad строкой good.
    :param inp: строка
    :return: новая строка
    """
    bad_ix = inp.find('bad')
    not_ix = inp.find('not')
    if bad_ix == -1 or not_ix == -1:
        return inp
    if bad_ix > not_ix:
        new_inp = inp[:not_ix] + "good" + inp[bad_ix + 3:]
        return new_inp
    return inp


assert 'good is good' == not_bad('not bad is good'), \
    "Нет замены"
assert 'good is good' == not_bad('not all what is bad is good'), \
    "Нет замены"
assert 'bad not good' == not_bad('bad not good'), \
    "Ненужная замена"
