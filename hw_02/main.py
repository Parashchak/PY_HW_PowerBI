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

# Variants
# -- 1 variant
'''
num1 = int(input("Enter 1-st number: "))
num2 = int(input("Enter 2-nd number: "))
num3 = int(input("Enter 3-rd number: "))

numbers = [num1,num2,num3]

maximal_num = max(numbers)
minimal_num = min(numbers)
median_num = sum(numbers) - maximal_num - minimal_num

print("Maximal num is: ", maximal_num, "\n", "Minimal num is: ", minimal_num, "\n", "Average num is: ", median_num)
'''
# -- 2 variant
'''
num1 = int(input("Enter 1-st number: "))
num2 = int(input("Enter 2-nd number: "))
num3 = int(input("Enter 3-rd number: "))

numbers = [num1,num2,num3]

maximal_num = 0
minimal_num = 0
median_num = 0

for i in numbers:
    if i == max(numbers):
        maximal_num = i
    elif i == min(numbers):
        minimal_num = i
    else:
        median_num = i

print(f"Максимальне число: {maximal_num}", f"Середнє число: {median_num}", f"Мінімальне число: {minimal_num}", sep='\n')
'''
# -- 3 variant
'''
while True:
    num1 = input("Введіть перше число: ")
    if num1.isdigit():
        num1 = int(num1)
        while True:
            num2 = input("Введіть друге число: ")
            if num2.isdigit():
                num2 = int(num2)
                while True:
                    num3 = input("Введіть третє число: ")
                    if num3.isdigit():
                        num3 = int(num3)
                        break
                break    
        break

maximal_num = max(num1, num2, num3)
minimal_num = min(num1, num2, num3)
median_num = num1 + num2 + num3 - maximal_num - minimal_num

print(f"Максимальне число: {maximal_num}", f"Середнє число: {median_num}", f"Мінімальне число: {minimal_num}", sep='\n')
'''
# -- 4 varint
'''
import random

numbers = [random.randint(100, 1000) for _ in range(3)]
numbers.sort()

print(f"Максимальне число: {numbers[2]}", f"Середнє число: {numbers[1]}", f"Мінімальне число: {numbers[0]}", sep='\n')
'''
# -- 5 variant
'''
import random

numbers = [random.randint(100, 1000) for _ in range(3)]

print(f"Максимальне число: {sorted(numbers)[2]}", f"Середнє число: {sorted(numbers)[1]}", f"Мінімальне число: {sorted(numbers)[0]}", sep='\n')
'''
# -- 6 variant
'''
while True:
    numbers = list(map(int, input("Введіть три числа через пробіл: ").split(" ")))
    if len(numbers) == 3:
        break

maximal_num = max(numbers)
minimal_num = min(numbers)
median_num = sum(numbers) - maximal_num - minimal_num

print(f"Максимальне число: {maximal_num}", f"Середнє число: {median_num}", f"Мінімальне число: {minimal_num}", sep='\n')
'''
# -- 7 variant
'''
import statistics

while True:
    numbers = list(map(int, input("Введіть три числа через пробіл: ").split(" ")))
    if len(numbers) == 3:
        break

maximal_num = max(numbers)
minimal_num = min(numbers)
median_num = statistics.median(numbers)

print(f"Максимальне число: {maximal_num}", f"Середнє число: {median_num}", f"Мінімальне число: {minimal_num}", sep='\n')
'''

'''***************************************************************************************'''

# 4. Зіграйте у гру Fizz-Buzz: виведіть усі числа від 1 до 100;
# якщо число ділиться на 3, замість числа виведіть "fizz".
# Якщо воно ділиться на 5, замість числа виведіть "Buzz".
# Якщо воно ділиться на обидва, виведіть "fizz buzz" замість числа.
'''
for i in range(1,100,1):
    if i % 3 == 0 and i % 5 == 0:
        print("fizz buzz")
    elif i % 3 == 0 and i % 5 != 0:
        print("fizz")
    elif i % 3 != 0 and i % 5 == 0:
        print("Buzz")
    else:
        print(i)
'''

'''***************************************************************************************'''

# 5. Зіграйте у гру 7-boom: виведіть усі числа від 1 до 100;
# якщо число ділиться на 7 або містить цифру 7, виведіть "BOOM" замість числа.

'''
for i in range(1,100,1):
    if (i % 7 == 0) or ('7' in str(i)):
        print("BOOM")
    else:
        print(i)
'''
