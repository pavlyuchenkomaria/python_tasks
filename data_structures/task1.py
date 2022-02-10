# LIST

def remove_adjacent(arr):
    """
    :param arr: список чисел
    :return: новый список, равный исходному,
    если бы из него удалили одинаковые смежные числа
    """
    res_arr = []
    for i in range(len(arr) - 1):
        if arr[i] != arr[i + 1]:
            res_arr.append(arr[i])
    return res_arr + [arr[-1]]


a = [1, 2, 2, 1, 2, 2, 2, 2, 2, 3]
remove_adjacent_a = remove_adjacent(a)
assert [1, 2, 1, 2, 3] == remove_adjacent_a, \
    "Не все лишние символы удалены"


def linear_merge(arr1, arr2):
    """
    Функция работает за линейное время.
    :param ar1, ar2: два отсортированных списка
    :return: объединенный список
    """
    res_arr = []
    i, j = 0, 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            res_arr.append(arr1[i])
            i += 1
        else:
            res_arr.append(arr2[j])
            j += 1
    res_arr.extend(arr1[i:])
    res_arr.extend(arr2[j:])
    return res_arr


a1 = [0, 1, 3, 5]
a2 = [2, 4, 9, 15, 17]
linear_merge_a = linear_merge(a1, a2)
assert [0, 1, 2, 3, 4, 5, 9, 15, 17] == linear_merge_a, \
    "Нарушен порядок символов!"


brace_dict = {
    '(': ')',
    '[': ']',
    '{': '}'
}
def ok_braces(inp, brace_dict):
    """
    :param inp: входящая последовательность скобок
    :param brace_dict: словарь с правилом открытия-закрытия скобок
    :return: логический результат проверки скобочной последовательности
    """
    stack = []
    is_correct = True
    for br in inp:
        if br in list(brace_dict.keys()):
            stack.append(br)
        elif br in list(brace_dict.values()):
            if len(stack) == 0:
                is_correct = False
                break
            last_br = stack.pop()
            if brace_dict[last_br] == br:
                continue
            else:
                is_correct = False
                break
    if len(stack) != 0:
        is_correct = False
    return is_correct


inp_OK = ['(', '[', ']', '{', '}', ')']
inp_WRONG = ['(', '[', '{', ']', '}', ')']
inp_WRONG2 = [']']
inp_WRONG3 = ['(', '[', ']']

assert 1 == ok_braces(inp_OK, brace_dict), \
    "Проверка дала неверный результат"
assert 0 == ok_braces(inp_WRONG, brace_dict), \
    "Проверка дала неверный результат"
assert 0 == ok_braces(inp_WRONG2, brace_dict), \
    "Проверка дала неверный результат"
assert 0 == ok_braces(inp_WRONG3, brace_dict), \
    "Проверка дала неверный результат"


