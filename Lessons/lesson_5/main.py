# 12.03.2024

dict_1 = {} # create emp dict
dict_2 = dict() # create emp dict with system word
country = {
    'Ukraine': {'Kyiv': ('Teremku','Darn')},
    'Germany': 'Berlin',
    'UK': 'London',
}

print(f'Type: {type(dict_1)} Value: {dict_1} ')
print(f'Type: {type(dict_2)} Value: {dict_2} ')
print(f'Type: {type(country)} Value: {country} ')

# Dict - має внутрішні методи для виводу значеннь
print(country.items()) # Повертає ключ-значення пари
print(country.keys()) # Повертає ключі
print(country.values()) # Повертає значення

# Kwargs - parameter 
def user(**kwargs) -> str: 
    print(type(kwargs))
    for key, value in kwargs.items():
        print(f'Key {key} Value: {value}')
        
marks = {'User1': 90, 'User2': 100, 'User3': 60, 'User4': 75}
user(User1 = 10, User2 = 100)
print('*' * 50)
user(**marks)

def some_function(a:int, b:int, c:float, d: int = 10, *args, **kwargs):
    '''
    Doc 
    '''
    pass

# Task 1. Напишіть програму, яка приймає рядок від користувача та повертає словник, де ключами є унікальні символи з рядка,
# а значеннями - кількість входжень цих символів у рядок. 
# Example: aaabcb -> 'a': 3, 'b':2, c: '1'
# def, dict, count, for

def task1(string:str) -> dict: 
    result = {} 
    for i in string:
        if i not in result:
            result[i] = string.count(i)
    return result

def task1(string: str) -> dict:
    return {i: string.count(i) for i in set(string)} if len(string) != 0 else {}

# Створення двох множин
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Об'єднання множин
union_set = set1.union(set2)
print(union_set)  # виведе {1, 2, 3, 4, 5, 6}
print(set2.union(set1))

# Перетин множин
intersection_set = set1.intersection(set2)
print(intersection_set)  # виведе {3, 4}

# Різниця множин
difference_set = set1.difference(set2)
print(difference_set)  # виведе {1, 2}

# Підмножина
subset = {4, 5}.issubset(set1)
print(subset)  # виведе False

# Надмножина
superset = set1.issuperset({1, 2,3,4})
print(superset)  # виведе True

# Додавання елементу
set1.add(5)
print(set1)  # виведе {1, 2, 3, 4, 5}

# Видалення елементу
set1.remove(4)
print(set1)  # виведе {1, 2, 3, 5}

# Task 1. Напишіть функцію, яка приймає два списки і повертає список спільних елементів. Використовуйте множини для знаходження спільних елементів
def task__1(set_1:list, set_2:list)->list:
    return list(set(set_1) & set(set_2))
# Task 2. Напишіть функцію, яка приймає список та повертає True, якщо усі елементи унікальні, та False, якщо є дублікати. Використовуйте множини для визначення унікальних елементів.
def task__2(arr:list)->list:
    return len(arr) == len(set(arr))
# Task 3. Напишіть функцію, яка приймає список і повертає список без дублікатів. Використовуйте множини для видалення дублікатів
def task__3(set_1:list, set_2:list)->list:
    return list(set(set_1) | set(set_2))
# Union - | , intersection - & ,  difference - (-)

# defaultdict -  дозволяє створювати словники із дефолт value
from collections import defaultdict, Counter 

# key  - default value
# Створення defaultdict зі значенням за замовчуванням 0
my_dict = defaultdict(int) # ключове слово

# Рядок, який потрібно проаналізувати
my_string = "AABBCA"

# Підрахунок кількості букв у рядку
for letter in my_string:
    my_dict[letter.lower()] += 1

# Виведення кількості кожної букви
for key, value in my_dict.items(): # (key, value)
    print(f"{key}: {value}")

print(my_dict)
my_dict['e']
my_dict['f']

my_dict['a'] = '10'
print(my_dict) # ключове слово

# Рядок, який потрібно проаналізувати
my_string = "AABBCA"

# Підрахунок кількості букв у рядку
for letter in my_string:
    my_dict[letter.lower()] += 1

# Виведення кількості кожної букви
for letter, count in my_dict.items():
    print(f"{letter}: {count}")

print(my_dict)
my_dict['e']
my_dict['f']

my_dict['a'] = '10'
print(my_dict)

# Counter - контейнер для підрахунку входження елементів 
my_list = [1, 2, 3, 1, 2, 3, 4, 5, 1, 2, 1, 23, 23]
my_counter = Counter(my_list)
print(my_counter)


# Підрахунок кількості входжень символів у рядок
my_char_counter = Counter(my_string)
print(my_char_counter)

from collections import namedtuple # імпорт функціоналу із бібліотеки 

Person = namedtuple('User', ['name', 'age', 'gender']) # фактичне створення структури

person1 = Person(name='Alice', age=25, gender='Female') # init person1 = ('Alice', 25, 'Female' )
person2 = Person(name='Bob', age=30, gender='Male')

Auto = namedtuple('Auto', ['mark', 'engine', 'type_', 'color'])

jaguar = Auto(mark = 'Jaguar', engine= 2.5, type_ = 'titp', color= 'black')
print(jaguar)

print(person1.name, person1[0])  
print(person2.age, person2[1])   
print(person1.gender,person1[2]) 

for person in [person1, person2]:
    print(f"Name: {person.name}, Age: {person.age}, Gender: {person.gender}")

# Task 1. Знайти найчастіше елемент у послідовності
def task_01(arr:list) -> any:
    return Counter(arr).most_common(1)[0][0]
# Task 2. Створити структуру для роботи із user (id, name, surname , email)
user_001 = User('123abc', 'UserName', 'UserSurname', 'some_test@gmail.com')
user_001.id