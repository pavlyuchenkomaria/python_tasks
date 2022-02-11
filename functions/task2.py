import pandas as pd

# lambda functions


# 1. Выбрать нечетные с помощью filter (структура filter(function, iterable)).
l = [i for i in range(10)]
odd_l = filter(lambda x: x % 2 != 0, l)
assert [1, 3, 5, 7, 9] == list(odd_l)


# 2. Возвести все числа в списке в куб с помощью map (структура map(function, iterable)).
cube_l = map(lambda x: x ** 3, l)
assert [0, 1, 8, 27, 64, 125, 216, 343, 512, 729] == list(cube_l)


# 3. Увеличить зарплату каждого сотрудника на 5%.
d = {'name': ['A', 'B', 'C', 'D', 'EE', 'FF'], 'fare': [34, 32, 36, 23, 54, 56]}
df = pd.DataFrame(d)
"""
  name  fare
0    A    34
1    B    32
2    C    36
3    D    23
4   EE    54
5   FF    56
"""

df['fare'] = df['fare'].apply(lambda x: x * 1.05)
"""
  name   fare
0    A  35.70
1    B  33.60
2    C  37.80
3    D  24.15
4   EE  56.70
5   FF  58.80
"""

# 4. Увеличить зп на 15% тем, у кого в имени два символа.
df['fare'] = df['fare'].apply(lambda x: round(x * 1.15, 2) if len(df['name']) > 1 else round(x, 2))
"""
  name   fare
0    A  41.05
1    B  38.64
2    C  43.47
3    D  27.77
4   EE  65.20
5   FF  67.62
"""

# 5. Оставить только тех, у кого зп больше 40, у остальных пропуск.

df['fare'] = df['fare'].apply(lambda y: y if y in list(filter(lambda x: x > 40, df['fare'])) else '-')
"""
  name   fare
0    A  41.05
1    B      -
2    C  43.47
3    D      -
4   EE   65.2
5   FF  67.62
"""

##################################

"""
Write a Python program to create a function that takes one argument, and that argument will be 
multiplied with an unknown given number.
"""
def multiplier(n):
    return lambda x: x * n

assert 45 == multiplier(3)(15)

"""
Write a Python program to sort a list of tuples using Lambda.
Original list of tuples:
[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
"""
unsorted_list = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
unsorted_list.sort(key=lambda x: x[1])
sorted_list = unsorted_list
assert sorted_list == [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]

"""
Write a Python program to sort a list of dictionaries using Lambda.
Original list of dictionaries :
[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, 
{'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
"""
d = [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': 2, 'color': 'Gold'},
     {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]

sorted_d = sorted(d, key=lambda x: x['model'])
assert sorted_d == [{'make': 'Mi Max', 'model': 2, 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'},
                    {'make': 'Nokia', 'model': 216, 'color': 'Black'}]

"""
Write a Python program to find if a given string starts with a given character using Lambda. 
"""
def start_check(x):
    return lambda s: True if s.startswith(x) else False

assert 1 == start_check('x')('x or not')
assert 0 == start_check('x')('y or not')


