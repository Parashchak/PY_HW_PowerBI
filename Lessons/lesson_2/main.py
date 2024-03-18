'''
name = 'Sasha'
age = 18
surname = 'Surname'

print('Hello', name, '\nYou are years old', age,  '\nYou surname is ', surname, name)

print('Hello {0} \nYou are years old {1}\nYou surname is {2} \n{1} {2}'.format(name, age, surname))

print('Hello {name} \nYou are years old {age}\nYou surname is {surname} \n{name}  {surname}, {plus}'.format(name = name, \
                                                                                                   age = age,  \
                                                                                                   surname = surname, \
                                                                                                   plus = name + ' ' + surname))

# name.capitalize() - переводить перший символ в верхній ригістр
# name.upper() - переводить все у верхній регістр
# name.lower() - переводить все у нижній регістр
# r рядок викоистовується для відображення з усіма символами r'Hello/\nWorld/\n'

sente = r'Hello World!\nMy name {name} and my surname \'{surname}\n\t\t{age}\t\t'
print(sente)
print('Hello World!\nMy name {name} and my surname \'{surname}\n\t\t{age}\t\t')
'''

#sql_query = rf'''
 #   select id, name from db 
  #  where name = {name};
#'''


'''
# Task1. Прийняти від корустувача: марку, рік, тип двигуна. Вивезти всю інформацію use 3 - types of format - виправити 
mark_auto = input('Enter mark auto: ').rstrip()
year_auto = input(f'Enter year auto: {mark_auto}: ').rstrip() # [0:4]
type_of_engine = input('Enter type/size of engine: ').rstrip()

# First, simple concat 
print('Mark: ', mark_auto, '\nYear: ', year_auto, '\nType of engine: ', type_of_engine, end = '\n\n')

# Second var, with format 
print('Mark: {mark}\nYear: {year}\mType of engine: {type}'.format(mark = mark_auto, year = year_auto, type = type_of_engine), end = '\n\n')


# Thierd var, using f-strings
print(f'Mark: {mark_auto} \nYear: {year_auto} \nType of engine: {type_of_engine}')
'''

'''
my_first_list = []
print(my_first_list, type(my_first_list))

my_first_list.append(1)
my_first_list.append(2)
my_first_list.append([3, 4])
print(my_first_list, my_first_list[0])

arr = ['name', 'surname', 18, True, [], 3.14] # create list by using []
arr_1 = list() # create emp list or use []
print(arr)

arr.append([9, 10])
print(arr)

arr.extend([11, 12,11])
print(arr)

matrix = [
    [1,2,[3,4,5]], # 0
    [4,5,6], # 1
    [7,8,9] # 2
]

print(matrix[0][-1][0]) # 0 - [1,2,[3,4,5]], -1 - [3,4,5], 0 - 3
print(matrix[0][0], matrix[1][1], matrix[2][2])

# if/stat - Оператори Розгла
# if <operation> and/or/not <operation>:
age = 17
if age >= 18 and age <= 100:
    print('You can go bar')
elif age < 18:
    print('You can\'t go bar')
else: 
    print('No info ')

age = 101
if age >= 18 and age <= 100: # first statement
    # indent block
    print('You can go bar')
elif age <= 18: # next stat if first False
    print(f'wait {18 - age}')
else: # if other block false, than up to else
    print('No info')

from random import choice

auto = ['Jaguar', 'Porsche', 'Tesla', 'Reno']

val = choice(auto)
print(val)

match val: # val 
    case 'Jaguar': # val == 'Jaguar'
        print('Jaguar best car')
    case 'Porsche': print('It is not Jaguar 😟')
    case 'Tesla':   print('Buy Jaguar')
    case _ : print('error') # else block
'''

'''
# 1. Take an integer number as input and print if it’s “Even” or “Odd”.
# input, print, cast, if
num = int(input('Please enter num: '))
#result = print('odd') if num % 2 else print('Even')

match num % 2:
    case 0:
        print('odd')
    case _ : print('Even')
'''

'''
# 2. Take as inputs sides of rectangular and print “Big” if the area is larger than 100, otherwise “small”.
hei = int(input('enter hei: '))
wei = int(input('enter wei: '))
if (hei * wei) > 100:
    print('Big')
else:
    print('Small')

# Second var
result = 'Big' if (hei * wei) > 100 else 'Small'
print(result)

result = 'Big' if (hei * wei) < 500 else 'Very Big' if (hei * wei) > 100 else 'Small'
'''

'''
a = 5
b = 5
operator = '//'
eval(f'{a} {operator} {b}')
'''

'''
# 3. Введіть назву фігури та відповідні параметри для того, щоб дізнатись її площу. 
# Виведіть напис «Великий», якщо площа більше 100, «Маленький», якщо менше. І якщо відповідь від'ємна – «Помилка»
# Ромб, трик, квадрату, коло, прямокутник
# 3 - зробити перевірки чи  існує  фігура, match/case
list_of_figure = ['Ромб','Треугольник']
name_of_figure = input('Выберите фигуру: Ромб или Треугольник: ').capitalize()

while not (name_of_figure in list_of_figure):
    print('Пожалуйста выберите только ту фигуру которая присутствует в этом списке')
    name_of_figure = input('Выберите фигуру: Ромб или Треугольник: ').capitalize()

if name_of_figure in list_of_figure:
    print(f'Вы выбрали фигуру {name_of_figure}')

if name_of_figure == 'Ромб':
    d1 = float(input('Пожалуйста введите первую диагональ: '))
    while d1 == 0:
        d1 = float(input('Ни одна из диагоналей не может быть равна нулю! Пожалуйста введите первую диагональ еще раз: '))

    d2 = float(input('Пожалуйста введите вторую диагональ: '))
    while d2 == 0:
        d2 = float(input('Ни одна из диагоналей не может быть равна нулю! Пожалуйста введите вторую диагональ еще раз: '))

    area_of_a_rhombus = d1 * d2
    print(f'Площадь вашего Ромба равна: {area_of_a_rhombus} см²')

elif name_of_figure == 'Треугольник':
    a = float(input('Пожалуйста введите первую сторону треугольника: '))
    while a == 0:
        a = float(input('Ни одна из сторон не может быть равна нулю! Пожалуйста введите первую сторону еще раз: '))

    b = float(input('Пожалуйста введите вторую сторону треугольника: '))
    while b == 0:
        b = float(input('Ни одна из сторон не может быть равна нулю! Пожалуйста введите вторую сторону еще раз: '))

    c = float(input('Пожалуйста введите третью сторону треугольника: '))
    while c == 0:
        c = float(input('Ни одна из сторон не может быть равна нулю! Пожалуйста введите третью сторону еще раз: '))

    area_of_a_triangle = (a + b + c) / 2
    print(f'Площадь вашего Треугольника равна: {area_of_a_triangle} см²')
'''