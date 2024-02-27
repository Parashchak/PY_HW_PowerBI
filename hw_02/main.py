# 1. Як вхідні дані запитайте ціле число.
# Якщо воно ділиться на 3, виведіть "foo";
# якщо воно ділиться на 5, виведіть "bar";
# якщо воно ділиться на обидва, виведіть "ham" (а не "foo" або "bar").
'''while True:
    num = input("Input integer: ")
    if num.isdigit():
        break

if int(num) % 3 == 0 and int(num) % 5 == 0:
    print("ham")
elif int(num) % 3 == 0 and int(num) % 5 != 0:
    print("foo")
elif int(num) % 3 != 0 and int(num) % 5 == 0:
    print("bar")
else:
    print("не ділиться ні на 3, ні на 5")'''

'''***************************************************************************************'''

# 2. Як вхідні дані запитайте два числа та виведіть яке з них менше і яке більше

#Варіанти вирішення
# --- 1 variant
'''num01 = int(input("Input first number: "))
num02 = int(input("Input second number: "))

if num01 > num02:
    print(f"{num01} > {num02}")
elif num02 > num01:
    print(f"{num02} > {num01}")
else:
    print(f"{num01} = {num02}")'''

# --- 2 variant
'''while True:
    num1 = input("Input first number: ")
    if num1.isdigit():
        while True:
            num2 = input("Input second number: ")
            if num2.isdigit():
                break
        break

firstNum = int(num1)
secondNum = int(num2)

if firstNum > secondNum:
    print(f"{firstNum} > {secondNum}")
elif secondNum > firstNum:
    print(f"{secondNum} > {firstNum}")
else:
    print(f"{firstNum} = {secondNum}")'''

# --- 3 variant
'''import random

numbers = [random.randint(100, 1000),random.randint(100, 1000)]

if numbers[0] > numbers[1]:
    print(f"{numbers[0]} > {numbers[1]}")
elif numbers[1] > numbers[0]:
    print(f"{numbers[1]} > {numbers[0]}")
else:
    print(f"{numbers[0]} = {numbers[1]}")'''

# Don`t commit and del
def numComp(firstNum, secondNum):
    if firstNum > secondNum:
        print(f"{firstNum} > {secondNum}")
    elif secondNum > firstNum:
        print(f"{secondNum} > {firstNum}")
    else:
        print(f"{firstNum} = {secondNum}")

# --- 4 variant
'''num01 = int(input("Input first number: "))
num02 = int(input("Input second number: "))
numComp(num01, num02)'''

# --- 5 variant
'''while True:
    num1 = input("Input first number: ")
    if num1.isdigit():
        while True:
            num2 = input("Input second number: ")
            if num2.isdigit():
                break
        break

firstNum = int(num1)
secondNum = int(num2)
numComp(firstNum,secondNum)'''

# --- 6 variant
'''import random

numbers = [random.randint(100, 1000), random.randint(100, 1000)]
numComp(numbers[0], numbers[1])'''

# --- 7 variant
'''a,b = map(int, input("Enter two numbers: ").split(" "))
numbers = [a,b,...]
numComp(numbers[0], numbers[1])'''

# --- 8 variant
'''while True:
    numbers = [*map(int, input("Enter two numbers: ").split(" "))]
    if len(numbers) == 2:
        break
numComp(numbers[0], numbers[1])'''

'''***************************************************************************************'''

# 3. Як вхідні дані запитайте три числа і виведіть найменше, середнє та найбільше.
# Припустимо, всі вони різні

'''***************************************************************************************'''

# 4. Зіграйте у гру Fizz-Buzz: виведіть усі числа від 1 до 100;
# якщо число ділиться на 3, замість числа виведіть "fizz".
# Якщо воно ділиться на 5, замість числа виведіть "Buzz".
# Якщо воно ділиться на обидва, виведіть "fizz buzz" замість числа.

'''***************************************************************************************'''

# 5. Зіграйте у гру 7-boom: виведіть усі числа від 1 до 100;
# якщо число ділиться на 7 або містить цифру 7, виведіть "BOOM" замість числа.
