# тут є детальна стаття щодо контекстного менеджера та застосувань: https://www.freecodecamp.org/news/context-managers-in-python/

from itertools import product, permutations, combinations # модуль для роботи з ітераторами
'''
#product - генерує усі можливі декартові добутки з декількох ітераторів тобто всі можливі комбінації елементів з кожного ітератора
a = [1, 2, 3]
b = ['a', 'b', 'c']
for i in product(a,b):
    print(i)

# product - генерує усі можливі декартові добутки з декількох ітераторів, тобто всі можливі комбінації елементів з кожного ітератора
a = ['email1', 'email2', 'email3']
b = ['a12r23', 'b32r23r', 'c3r23r2f']
c = ['d234wd', 'eed32de', 'fdtgbr']
for i in product(b, c, a):
    print(i)

# permutations -  генерує усі можливі перестановки заданого розміру з елементів ітератора
# Генерація усіх можливих перестановок трьох елементів
a = [1, 2, 3,4]
for i in permutations(a, 2):
    print(i)

help(combinations)
help(permutations)

# combinations генерує усі можливі комбінації заданого розміру з елементів ітератора.
# Генерація усіх можливих комбінацій з трьох елементів
a = [1, 2, 3, 4]
for i in combinations(a, 2):
    print(i)

# open - для відкриття файлу і роботи із ним 
help(open)
'''

# Відкриття файлу
file = open("/Users/vasylparashchak/Desktop/test-py/first_file.txt", "w")

print(file, type(file))

# Запис вмісту файлу
file.write('Hello World!')

# Закриття файлу
file.close()

# Відкриття файлу
file = open("/Users/vasylparashchak/Desktop/test-py/first_file.txt", "w")

# Запис вмісту файлу
file.write('One more line')

# Закриття файлу
file.close()

print('Hello World!','Name' ,sep = '\t')

# Відкриття файлу
file = open("/Users/vasylparashchak/Desktop/test-py/first_file.txt", "a")

# Запис вмісту файлу
file.write('\nOne more line') # Text object
file.writelines('\nSecond lines') # Python object

# Закриття файлу
file.close()

# Відкриття файлу
file = open("/Users/vasylparashchak/Desktop/test-py/first_file.txt", "r")

# Зчитування вмісту файлу
content = file.read()

# Виведення вмісту файлу на екран
print(content)

# Закриття файлу
file.close()

# Відкриття файлу
# a - append, + - 
file = open("/Users/vasylparashchak/Desktop/test-py/first_file.txt", "r+")

# Зчитування вмісту файлу
# for i in file.read():
#     print(i)
# readline - один рядок, readlines - many rows 
for i in file.readlines():
    print(i)

file.write('\nThierd line of text')    

# Закриття файлу
file.close()

# w - write
# r - read
# a - append
# t - text
# a+
# r+
# w+
# rb, wb,ab

# Відкриття файлу
file = open("/Users/vasylparashchak/Desktop/test-py/first_file.txt", "r+")

string = r'String \n\nNew test' # row - strings
print(string)
print(string.count("\n"))
# Зчитування першого рядка файлу
line1 = file.readline()
print(line1)

# Зчитування другого рядка файлу
line1 = file.readline()
print(line1)

line3 = file.readline()
print(line3)

# Закриття файлу
file.close()

import random as rn
import string 
string.ascii_uppercase

FILE_PATH = r"/Users/vasylparashchak/Desktop/test-py/"

'''
# Task1. Create files from A-Z(name of files). Write some text or number(range from 1 to 1000)
# Create files: name[A-Z]
for i in range(ord('A'), ord('Z') + 1):
    file = open(FILE_PATH + f'{chr(i)}.txt', 'w')
    
    file.write(str(rn.randint(1,1000)))
    
    file.close()
'''

# Task 2. After task 1. Read files and calculate sum of all number in this file. *Realize task 1 and task 2 using function
def generate_number(N: int = 1000) -> int:
    return rn.randint(1, N + 1) 

def create_file(name_of_file:str, text_data: int, file_path:str = FILE_PATH) -> None:
    
    file = open(file_path + name_of_file + '.txt', 'w')
    
    file.write(str(text_data))
    
    file.close()

def read_file(file_path: str) -> int:
    
    file = open(file_path, 'r')
    
    content = file.read().strip()
    
    return int(content)

for i in range(65, 91):
    create_file(chr(i), generate_number())

sum_ = 0
for i in range(65, 91):
    file = read_file(f'/Users/vasylparashchak/Desktop/test-py/{chr(i)}.txt')
    sum_ += file
print(sum_)

# del all created files from 'A' to 'Z'
import os 

for i in range(65, 91):
    file = f'/Users/vasylparashchak/Desktop/test-py/{chr(i)}.txt'
    
    try: 
        os.remove(file)
    except FileNotFoundError as fn:
        print(f'No such file in directory. Check file_path: {file}')
    except Exception as e:
        print(f'Something wrong: {e} Try later!. Check file: {file}')

ord('A'), ord('Z'), chr(65)

file = open(f'{FILE_PATH}Japan.txt', 'w')

file.write('Capital: Tokyo\nPopulation: 120_000_00')

file.close()

file = open(f'{FILE_PATH}UK.txt', 'w')

file.write('Capital: London\nPopulation: 90_0000')

file.close()

with open(f"{FILE_PATH}Japan.txt", 'r') as file, open(f"{FILE_PATH}UK.txt", 'r') as file1:
    data = file.read()
    print(data)
    print(file1.read())


#JSON (JavaScript Object Notation) - це формат обміну даними, доволі часто це словник
# pip install requests
# { key : {key: value } }


# Weather App
import requests
'''
API_KEY = "33d99a1c99c5ea82e6aaff8592cd6fc3"  

city = input('Enteryou city: ').strip().capitalize()

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}" # &units=metric

response = requests.get(url)

print(response.status_code, response) # відповідь сервера, від 1xx до 5xx


API_KEY = "33d99a1c99c5ea82e6aaff8592cd6fc3"  

city = input('Enteryou city: ').strip().capitalize()

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}" # &units=metric


with requests.Session() as session: 
    response = session.get(url)
    
    if check_status_code(response):
        weather_data = response.json()
        print(weather_data)
    else:
        print('No data')
'''
# Step 1. Get data from server(using GET), using API(openweathermap) we go to server and find weather for city
# Step 2. Check status_code, if status_code == 200, get json
# Step 3. From json extract fields 
city = input('Enteryou city: ').strip().capitalize()
API_KEY = "33d99a1c99c5ea82e6aaff8592cd6fc3"  
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}" # &units=metric

def connection_to_server(city: str, URL: str, API_KEY: str) -> requests.Response: 
    with requests.Session() as session: 
        response = session.get(URL)
        return response
    
from datetime import datetime as dt

def get_date():
    return dt.now()

def convert_kel_in_ceil(temp: int) -> int:
    return round(temp - 273.15,2) if isinstance(temp, (int, float)) else temp

def get_json(response: str) -> dict | None:
    if check_status_code(response):
        return response.json()
    else:
        return None
    
# Step 1
response = connection_to_server(city, url, API_KEY)

# Step 2
weather_data = get_json(response)

weather_data.keys()

weather_data.get('sys').get('country'), get_date()

weather_data.get('name'), weather_data.get('timezone')

print(f"Today {get_date()} weather in {weather_data.get('name')} in {weather_data.get('sys').get('country')}")

weather_data.keys()

weather_data

if response.status_code == 200:
    data = response.json()
    print(data, data.keys())

    temp = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    description = data["weather"][0]["description"]
    wind = data['wind']['speed'] 
    clouds = data['clouds']['all']
    print(f"Погода в місті {city}: {description}")
    print(f"Температура: {convert_kel_in_ceil(temp)}°F, відчувається як {convert_kel_in_ceil(feels_like)}°F")
    print(f'Wind speed: {wind}, Clouds: {clouds} ')
else:
    print("Не вдалося отримати дані про погоду")


data = response.json()
print(data)

print(data.keys())

print(data['main'])

print(data['main']['temp'])

# Link to find: https://api.monobank.ua/docs/
# Read json, and display dollar, euro info

# Monobank
import requests 
import time  

URL_MONO = 'https://api.monobank.ua/bank/currency'

CURRENCY = (840,978, 704)

dict_ = {
    840: '💲',
    978: '💶',
    704: '₫'
}
curr = requests.get(URL_MONO)

if curr.status_code == 200:
    data = curr.json()
elif curr.status_code == 428:
    time.sleep(15)
else:
    print(f'{curr.status_code}')

data[0]

for i in data:
    if i['currencyCodeA'] in CURRENCY:
        print(f"Currency: {i['currencyCodeA']}: \
              {dict_.get(i['currencyCodeA'])}, {i['currencyCodeB']}\n \
              Buy: {i['rateBuy']} Sell: {i['rateSell']}")
        
match curr.status_code:
    case 200: 
        curr = curr.json()
    case 428: 
        print('Many req: time to sleep')
        time.sleep(10)
    case 404:
        print('Error website')
    case _ as e:
        print(f'Error is {e}')

print(type(curr), type(curr[0]), curr[0].keys())

currency = []
for i in curr.json():
    if i['currencyCodeA'] in CURRENCY:
        currency.append(i)

print(currency)