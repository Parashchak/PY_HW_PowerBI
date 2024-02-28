# 1. Запросіть у користувача ім'я та місячну зарплату
# в доларах та виведіть їхню річну зарплату в тисячах доларів.
# Наприклад: «Мішель», «12345» → «Річна зарплата Мішель складає 148 тис. доларів».
'''name = str(input("Please, input Your name: "))
monthSalary = int(input("Please, input Your month salary: "))
yearSalary = monthSalary * 12 / 1000
print(f"{name}, Your salary is {yearSalary} K per year")'''

# 2. Запросіть ціле число і виведіть True, якщо це парне число діапазоні від 100 до 999, інакше - «False».
'''num = input("Please, enter an integer between 100 and 999: ")
x = num.isdigit()
if x:
    if 100 <= int(num) <= 999 and int(num) % 2 == 0:
        print("True")
    else:
        print("False")
else:
    print("False")'''
#Вітаю.
#Рішення 2 завдання можна записати лаконічніше:
'''user_input = input("Enter an integer: ")

if user_input.isdigit():
  number = int(user_input)
  print(number % 2 == 0 and 100 <= number <= 999)
else:
  print("\nInvalid input format. Please enter a positive integer.")'''

# 3. Як вхідні дані візьмемо ціле число;
# Це число від 101 до 999, а його остання цифра не дорівнює нулю.
# Виведіть число, що складається з чисел першого у зворотньому порядку.
# Наприклад: 256 → 652.
'''num = input("Enter an integer number: ")
x = num.isdigit()
if x:
    if 101 <= int(num) <= 999 and int(num[2]) > 0:
        print(int(num[::-1]))
    else:
        print("The last num in the number must not be 0 and number must be from 101 to 999")
else:
    print("Please enter an integer number from 101 to 999")'''

import random

'''while True:
    num = random.randint(101, 999)
    if int(str(num)[2]) > 0:
        print(int(str(num)[::-1]))
        break'''

# 4. Запитайте два цілих числа та виведіть:
# a. Їхню суму
# b. Їхня різниця
# c. результат множення
# d. Результат поділу першого на друге
# e. Залишок від поділу першого на друге
# f. True, якщо перше число більше або дорівнює другому, інакше False

'''num1 = int(input("Please, input first number: "))
num2 = int(input("Please, input second number: "))

if num2 > 0:
    print(f"Sum: {num1 + num2}")
    print(f"Diff: {num1 - num2}")
    print(f"Multi: {num1 * num2}")
    print(f"Div: {num1 / num2}")
    print(f"Modulus: {num1 % num2}")
    print(num1 >= num2)
else:
    print("Second number must be more that 0")'''

'''num01 = input("Please, input first number: ")
num02 = input("Please, input second number: ")

if num01.isdigit() and num02.isdigit():
    num1 = int(num01)
    num2 = int(num02)
    if num2 > 0:
        print(f"Sum: {num1 + num2}")
        print(f"Diff: {num1 - num2}")
        print(f"Multi: {num1 * num2}")
        print(f"Div: {num1 / num2}")
        print(f"Modulus: {num1 % num2}")
        print(num1 >= num2)
    else:
        print("Second number must be more that 0")
else:
    print("The numbers must be an integers")'''