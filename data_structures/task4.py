# MATRIX

def matrix_product(m1, m2):
    """
    :param m1, m2: две матрицы
    :return: произведение матриц или исключение, если это невозможно
    Пример: a = [[1, 2], [3, 4]]; b = [[3, 6], [8, 9]]
     a: 1 2    b: 3 6     c=a*b: 1*3+2*8  1*6+2*9   c: 19 24
        3 4       8 9            3*3+4*8  3*6+4*9      41 54
    условия на размер матриц: n*l и l*m
    """
    try:
        assert (len(m1[0]) == len(m2)), "Problems with matrices size"
    except Exception as e:
        print(e)
        exit()
    else:
        res = [[0] * len(m2[0]) for i in range(len(m1))]
        for i in range(len(m1)):
            for j in range(len(m2[0])):
                for k in range(len(m2)):
                    res[i][j] += m1[i][k] * m2[k][j]
        return res


m1 = [[1, 2], [3, 4]]
m2 = [[3, 6], [8, 9]]
assert [[19, 24], [41, 54]] == matrix_product(m1, m2),\
    "Ошибка в перемножении"
# тест размерностей
m1 = [[1, 2], [3, 4]]
m2 = [[3, 6]]
matrix_product(m1, m2) # Problems with matrices size


def matrix_pretty_print(matr):
    """
    Печать матрицы в красивом виде
    :param matr: матрица
    """
    len_of_line = len(matr[0]) * 8

    print("_" * len_of_line)
    print('\n'.join(['\t'.join(['|' + str(cell) for cell in row]) +
                     '\n' + "_" * len_of_line for row in matr]))


matrix_pretty_print([[-111, -444], [-111, -999]])
"""
________________
|-111	|-444
________________
|-111	|-999
________________
"""

