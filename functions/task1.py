def product(*args):
    """
    :param args: произвольное количество множеств
    :return: кортежи, которые являются перечислением всех элементов декартова произведения
    """
    tuple_list = [tuple(s) for s in args]
    result = [[]]
    for t_l in tuple_list:
        cur_result = []
        for x in result:
            for y in t_l:
                cur_result.append(x + [y])
        result = cur_result

    res_tuples = [tuple(l) for l in result]
    return res_tuples


product_a = product({1, 2, 3}, {2, 3}, {3})
assert [(1, 2, 3), (1, 3, 3), (2, 2, 3), (2, 3, 3), (3, 2, 3), (3, 3, 3)] == \
       product_a, "Ошибка в произведении"


def lcm(first_value, second_value, *other_values):
    """
    :param first_value, second_value, *other_values: 2 или более целых числа
    :return: наименьшее общее кратное чисел
    """

    def swap(a, b):
        temp = a
        a = b
        b = temp
        return a, b

    def gcd(a, b):
        """
        Вычисляет НОД по алгоритму Евклида
        :return: НОД(a,b)
        """
        if a < b:
            a, b = swap(a, b)
        while b:
            a %= b
            a, b = swap(a, b)
        return a

    def lcm_2numbers(a, b):
        """
        :return: НОК(a,b)
        """
        return a * b // gcd(a, b)

    def compute_other(other_values):
        """
        Будет вычислять НОК последовательности с помощью lcm_2numbers()
        :return: НОК последовательности
        """
        a0 = other_values[0]
        other_values.pop(0)
        if len(other_values) > 1:
            return lcm_2numbers(a0, compute_other(other_values))
        else:
            return lcm_2numbers(a0, other_values[0])

    if len(other_values) > 0:
        res_other = compute_other(list(other_values))
        res12 = lcm_2numbers(first_value, second_value)
        res = lcm_2numbers(res12, res_other)
        return res

    else:
        res = lcm_2numbers(first_value, second_value)
        return res


assert 703500 == lcm(100500, 42), "Неверный результат"
assert 240 == lcm(2, 40, 8, 48, 16), "Неверный результат"
assert 19890 == lcm(*range(2, 40, 8)), "Неверный результат"


def compose(*funcs):
    """
    :param funcs: произвольное количество функций от одного аргумента
    :return: композиция функций, которая подсчитывает результат
    """
    if len(funcs) == 1:
        return funcs[0]

    def double_f(f1, f2):
        return lambda x: f1(f2(x))

    def more_f(funcs):
        if len(funcs) == 2:
            return double_f(funcs[0], funcs[1])
        else:
            a0 = funcs[0]
            funcs.pop(0)
            return double_f(a0, more_f(funcs))

    f_combination = more_f(list(funcs))
    return f_combination


f = compose(lambda x: 2 * x, lambda x: x + 1, lambda x: x % 9)
compose_a = f(42)
assert 14 == compose_a, "Неверный результат"
