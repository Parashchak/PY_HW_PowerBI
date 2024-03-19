# 14.03.2024
from collections import OrderedDict

ord_dict = OrderedDict([('Person3', 3), ('Person2', 2), ('Person1', 1)])

print(ord_dict, type(ord_dict), ord_dict.__sizeof__())

ord_dict['per'] = 3

for i in ord_dict:
    print(i)

from collections import OrderedDict

ord_dict = OrderedDict([('Person3', 'abc'), ('Person2', 'dba'), ('Person1', 'rt')])

print(ord_dict, type(ord_dict), ord_dict.__sizeof__())

ord_dict['per'] = 3

for i in ord_dict:
    print(i)

# Time - для роботи із часом
import time # імпорт додаткового функціоналу для робити з часом

current_time = time.time()  # Повертає кількість секунд, що пройшли з 1 січня 1970 року
print(current_time)

print("Початок")
# -> API 
for i in range(0, 10):
    # -> API
    time.sleep(2)  # Затримка на 3 секунди
# -> API
print("Кінець")

timestamp = time.time()  # Поточний час
local_time = time.localtime(timestamp)  # Перетворення часу на локальний часовий пояс
print(local_time, type(local_time))
print(local_time.tm_year, local_time.tm_mday, local_time.tm_mon) # отримати складову часу за допомогою дот нотації

# Task 1. Write function to find current date - return date in format day of week month name year(yyyy)
# Task 2. Write cycle iterate 100 elements after last element sleep for 10 seconds, and display test 'All done'

def current_date(date: time.time) -> time.time:
    
    if not isinstance(date, float):
        return False
  
    local_time = time.localtime(date)
    
    # MONTH = ['Jan', 'Feb', 'Mart']
    
    # month = ''
    
    # match local_time.tm_mon:
    #     case 1: month = MONTH[0]
    #     case 2:
    #         month = MONTH[1]
    #     case 3 :
    #         month = MONTH[2]
    #     case _ :
    #         return False
    
    month_date = {
        1 : 'Jan' ,
        2 : 'Feb' ,
        3 : 'March'
    }
    
    return str(local_time.tm_wday) + '-' + month_date.get(local_time.tm_mon) + '-' + str(local_time.tm_year)

# Datetime - бібліотека для зручних математичних обрахунків із датою
from datetime import datetime, date  # НЕ рекомендую

date = date(2023, 10 , 26)  # Створення об'єкта дати зі значеннями "2023-10-26"
print(date, type(date))

now = datetime.now()  # Повертає поточний об'єкт дати та часу
print(now)

import datetime

date1 = datetime.date(2023, 4, 10)
date2 = datetime.date(2024, 4, 10)

delta = date2 - date1  # Різниця між датами
print(delta.days, delta)  # Виведення кількості днів між датами

add = lambda x, y : x + y # def _ (param1, param2): дія 
div = lambda x,y : x / y if y != 0 else 0
pres = add(5,10)
print(pres)
print(add(10,10))
print(div(10, 0))

arr = [i for i in range(1, 11)]

print(arr)

print(list(map(lambda x: x ** 2 if x > 10 else x + 3, arr)))

arr = ['1', '2', '3', '4', '5', '6', '7']

result = []
for i in arr:
    result.append(int(i))
print(result)

# filter - filter(function, iterable object)
numbers = [i for i in range(0, 15)]
even = tuple(filter(lambda x: x % 2 == 0, numbers))
print(even)

from functools import reduce # потрібно імпортувати із built-in бібліотеки

numbers = [i for i in range(1, 16)]

product = reduce(lambda x, y: x*y, numbers)

numbers = [i for i in range(0, 15)]
even = ''.join(str(i) for i in filter(lambda x: x % 2 == 0, numbers))
print(even)

# str 
string = ['1', '2', '3', '4', '5', '6', '7']

result = reduce(lambda x,y: x + y , map(lambda x: int(x), string))
print(result)

# завдання 
# 1. Використайте map() для перетворення списку зі рядок на список чисел: ['1', '2', '3', '4', '5'] → [1, 2, 3, 4, 5].
# 2. Використайте filter() для знаходження всіх парних чисел у списку: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] → [2, 4, 6, 8, 10].
# 3. Використайте reduce() для обчислення добутку всіх елементів у списку: [1, 2, 3, 4, 5] → 120 (1 * 2 * 3 * 4 * 5).
# 4. Використайте map() для перетворення списку зі рядок на список квадратів цих чисел: [1, 2, 3, 4, 5] → [1, 4, 9, 16, 25].
# 5. Використайте filter() для знаходження всіх позитивне чисел у списку: [1, -2, 3, -4, 5, -6, 7, -8, 9, -10] → [1, 3, 5, 7, 9].
# 6. Використайте reduce() для обчислення суми всіх елементів у списку: [1, 2, 3, 4, 5] → 15 (1 + 2 + 3 + 4 + 5).
# 7. Використайте map() для перетворення списку зі рядок на список їхніх довжин: ['apple', 'banana', 'cherry'] → [5, 6, 6].
# 8. Використайте filter() для знаходження всіх елементів списку, які більше за середнє значення списку: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] → [6, 7, 8, 9, 10].
# 9. Використайте reduce() для обчислення найбільшого елемента у списку: [1, 5, 3, 9, 2] → 9.
# 10. Використайте map() для перетворення списку зі рядок на список великих літер: ['apple', 'banana', 'cherry'] → ['APPLE', 'BANANA', 'CHERRY'].

try:
    number = float(input('Input value: '))
   # print(number / 0)
   # print(str(number)[10])
# except ValueError: 
#     print('Wrong value input ')
except ZeroDivisionError:
    print('ZeroDivisionError')
except TimeoutError:
    time.sleep(10)
    # connection to server
except Exception as e:
    print(f'Wrong data, you error is {e} {e.with_traceback}')
finally:
    print('All okey')

try_numbers = 1
while try_numbers < 2:
    try:
        number = float(input('Input value: '))
    # print(number / 0)
    # print(str(number)[10])
    # except ValueError: 
    #     print('Wrong value input ')
    except ZeroDivisionError:
        print('ZeroDivisionError')
    except Exception as e:
        print(f'Wrong data, you error is {e} {e.with_traceback}')
    finally:
        print(f'Try number: {try_numbers}')
        try_numbers += 1

number = input('Input value: ')

if not number.isdigit():
    raise ValueError("It isn't number.Try later!")

# Task: try/except
# 1. Написати калькультор, який при діленні на нуль повертає текст помилки, опрацювати інші можливі помилки також 
# 2. Написати функцію, яка при вводі юзера не числа, буде повторювати дію, до тих пір поки user - не введе позитивне число
