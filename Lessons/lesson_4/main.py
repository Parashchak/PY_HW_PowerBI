# 10.03.2024 

'''
# try використовується для відловлення помилки
try:
    number = int(input('Enter you number: ').strip())
    print(number)
except Exception as ex: 
    print(ex)

# Task 6. Check if first symbol in strings equal last symbol in strings.
string = 'abca'
print(string[0] == string[-1])

# Task 7. Password check. If password have: спец символ, + 15б, більше 8 літер + 10б, має заглавну літеру +5б, містить число +2
# +1 for symb
# Create groups
password = input('Enter your password: ').rstrip()

count_ = 0

if len(password) > 8:
    count_ += 10

for i in password:
    if not i.isdigit() and not i.isalpha() and i not in ['.', '_', '-', ',', ' ']:
        count_ += 15
    elif i == i.upper():
        count_ += 5
    elif i == i.isdigit():
        count_ += 2
    else:
        count_ += 1

if count_ < 50:
    print(f'Week password {count_}')
elif count_ >= 50 and count_ < 65:
    print(f'Middle password {count_}')
else:
    print(f'High password {count_}')

# String:
   # Task 1. Write a program that takes a string and returns it in reverse order.
string = 'hello'
print(string[::-1])
   # Task 2. Check if the input string is a palindrome, disregarding case and spaces.
string_ = 'helleH'.lower()
print(string_ == string_[::-1])
   # Task 3. Write a program that counts the number of words in a sentence.
string3 = 'hello world'
count_3 = 0
for i in string3.split(' '):
    count_3 += 1
print(f'Sentence has a {count_3} words')
#var -- 2
print(f'Sentence has a {len(string3.split(' '))} words')

# Task *. Напишіть програму, що виводить таблицю множення, але у зворотному порядку: від 10х10 до 1х1
n = 10
for i in range(n,0,-1):
    for j in range(n,0,-1):
        print(f'{i} * {j} = {i*j}')
'''
    
def hello1(name: str, age:int) -> str:
    ''' Doc-s file function with parameters '''
    print(f'Name user: {name} Age user: {age}')

hello1.__annotations__, hello1.__doc__

# assert використовується для прописання тесту (Приклад: assert add(10,5) == 15, "Помилка з операцією" (ассерт назва функції(аргументи) == очікуване значення, опис помилки)) 

import datetime as dt

# Type 1
def current_date() -> str: 
    return dt.datetime.now()

print(current_date())

start  = current_date()
print(start) 
s = 0
for i in range(0, 10_000_00_00):
    s += i 
print(s) 
end = current_date()
print(f'Start : {start} End : {end} \nTime: {end - start}')

def check_status_code(status_code: str) -> bool:
    match status_code:
        case 200: 
            return True
        case 404:
            return False
        case _ as e:
            return f'Error {e}'

#!pip install requests

#conda install requests

import requests 

req = requests.get('https://api.monobank.ua/bank/currency')

print(req, req.status_code)

currency = {
    840: '💵',
    978: '💶'
}

if check_status_code(req.status_code) == True:
    print('We can work with currency')
    for i in req.json():
        if i.get('currencyCodeA') in (840, 978):
            print(f"Code is: {i['currencyCodeA']} Image: {currency[i['currencyCodeA']]} Buy: {i['rateBuy']}")
else:
    print(f'we can\'t work with currency {check_status_code(req)}')


# Creating a tuple
fruits = ("apple", "banana", "cherry", "melon")

# can use index
print(fruits[0])  
print(fruits[2])

# collection can iterate
for fruit in fruits:
    print(fruit)

print('*' * 50)
# Tuple unpacking
first_fruit, second_fruit, *remaining_fruits = fruits
print(first_fruit)        # Output: apple
print(second_fruit)       # Output: banana
print(remaining_fruits)   

*all_f, = fruits
# Tuple concatenation - one more operation 
more_fruits = ("elderberry", "fig")
all_fruits = fruits + more_fruits
print(all_fruits)
print(all_f)

def example(a: int, b:int, c:int = 0, *args):
    print(type(a), type(b), type(c), type(args))
    
    return a + b + c + sum(args)

print(example(5,10,15,20,25,30))

# Task 1. Створити пусту функцію із назвою  try_p
def try_p():
    pass
# Task 2. Функція яка повертає який аргумент більший(а, b)
def gross_num (a:int,b:int) -> int:
    if a > b :
        return print(f'{a} > {b}')
    elif a == b :
        return print(f'{a} = {b}')
    else:
        return print(f'{a} < {b}')

# var 2
def max_arg (a:int,b:int) -> int:
    return max(a,b) if isinstance(a, int) and isinstance(b, int) else 'Work only with Int'
# Task 3. Функція для inf кількості аргументів, повинна повертати суму чисел 
def sum_(*args):
    return sum(args) if not args else 'Wrong data'
# Task 4. Реалізувати функцію калькулятор, приймає 3 аргументи, a, b, operation, вивезти дію
def calculator(a: int, b: int, operation: str) -> int:
    match operation.strip():
        case '+' : return a + b
        case '-' : return a - b
        case '*' : return a * b
        case '/' : return a / b if a != 0 and b != 0 else 0
        case '**' : return a ** b
        case '//' : return a // b if a != 0 and b != 0 else 0
        case _ : return f'Unk operation {operation}'


#* Тести для 2, 4

