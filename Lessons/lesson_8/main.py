'''
PEP8 - це стиль кодування для мови програмування Python, 
рекомендований Python Software Foundation. 
Цей стиль включає набір правил та рекомендацій щодо форматування коду, 
найменування змінних та функцій, вирівнювання рядків і т.д. 
Його мета полягає в тому, щоб зробити код більш зрозумілим і легко зчитуваним для розробників.

Flake8 - аналізатор коду

reStructuredText - це стандарт документації для Python, 
який зазвичай використовується для документування модулів та функцій. 
Його можна використовувати в докстрінгах (тобто, у рядках документації, 
які містяться в модулях, функціях та класах) для надання детальної документації про функції та методи
'''

# pip install flake8 
# pip3 install flake8
# conda install flake8

def add(a, b):
    """
    This function adds two numbers.

    :param a: The first number to add.
    :type a: int
    :param b: The second number to add.
    :type b: int
    :return: The sum of a and b.
    :rtype: int
    """
    return a + b

print(add.__doc__)

'''
NumPyDoc - це варіант стандарту документації reStructuredText, 
який зазвичай використовується для документування бібліотек NumPy та SciPy. 
Він містить деякі додаткові мітки, які дозволяють вказати формат та тип параметрів та повернених значень.
'''

initial_amount = int(input('Write your initial amount of deposited money'))
interest_rate = float(input('write rate of interest for deposited money'))
number_years = int(input('Write number of years for deposited money'))
def simple_interest(initial_amount, interest_rate, number_years):
    total_amount = initial_amount
    for i in range(1, number_years+1):
        total_amount += (total_amount * interest_rate / 100)
    return total_amount

print(simple_interest(initial_amount, interest_rate, number_years))

def add(a, b) -> int:
    """
    Add two numbers.

    Parameters
    ----------
    a : int
        The first number to add.
    b : int
        The second number to add.

    Returns
    -------
    int
        The sum of a and b.
    """
    return a + b if isinstance(a, (int,float)) and isinstance(b, (int, float)) else None

print(add.__doc__)

# Asserts - key word for testing, if true - pass, else AssertitionError
def test_add_function():
    assert add(5, 5) == 10, 'Error'
    assert add(10, 10) == 20, 'Error'
    assert add('5', '5') == None, 'Concat'
    

test_add_function()

def minus(a: int, b:int) -> int: 
    return a - b 

assert minus(10, 5) == 5, 'Something wrong'

assert add(5,5) == 10

def is_even(num:int) -> bool:
    """
    Функція is_even перевіряє, чи є число парним.

    :param num: Число для перевірки.
    :type num: int
    :return: True, якщо число парне, False, якщо непарне.
    :rtype: bool
    """
    return num % 2 == 0

class Human:
    pass 

human1 = Human()

class Human:
    
    def __init__(self, name, age) -> None:
        self.name = name 
        self.age = age  
        
    def say_hello(self):
        print(f'Hello {self.name} You age is {self.age}')


class Deposit(object):
    
    def __init__(self, deposit_id, amount = 0) -> None:
        self.deposit_id = deposit_id
        self.amount = amount
        
    
    def add_money(self, money): 
        print(f'Now you have {self.amount} money')
        self.amount +=  money
        print(f'Now you have {self.amount} money') 
        
    def withdraw_money(self, money):
        if self.amount - money < 0:
            return f'Not secure operation {money}'
        self.amount -= money
                
    def check_dep(self): 
        print(f'Dep name: {self.deposit_id}. Amount: {self.amount}')


dep1 = Deposit('abgwdv134bvdfber')

dep1.deposit_id, dep1.amount

type(dep1)

dep1.add_money(10_00)

dep1.deposit_id, dep1.amount

dep1.withdraw_money(10_01)

dep1.withdraw_money(100)

dep1.check_dep()

human1 = Human('Human1', 26)

human1.name, human1.age

human2 = Human(name = 'Alina', age=23)

human2.name, human2.age

human2.say_hello()

# Task 1. Create class Auto. With next fields: mark, year, engine, fuel, color, speed = 0. 
# Create methods: display all information about auto.  Accelerate and break method. Start engine check fuel

class Auto(object):
    
    def __init__(self, mark, year, color, engine = False, fuel = 0, speed = 0) -> None:
        self.mark = mark
        self.year = year 
        self.color = color
        self.engine = engine
        self.fuel = fuel 
        self.speed = speed
        
    def __repr__(self) -> str:
        return f'Brand: {self.mark}. Year is {self.year}. Color is {self.color}. \
              \nEngine status {self.engine}. Fuel balance {self.fuel}. Speed: {self.speed}'
    
    def start_engine(self):
        self.engine = True
        
    def stop_engine(self):
        self.engine = False
         
    def is_engine_start(self): 
        return self.engine 
    
    def accelerate(self, new_speed):
        if self.speed + new_speed > 200:
            return None 
        self.speed += new_speed
        
    def brake(self, new_speed):
        if self.speed - new_speed < 0:
            return None 
        elif self.speed - new_speed == 0:
            self.speed -= new_speed
            self.engine = False
        else:
            self.speed -= new_speed


tesla = Auto('Tesla', 2019, 'black', fuel = 100)

print(tesla)

tesla.start_engine()

print(tesla)

# public - open in Any, 0 - _
class A():
    name = 'Name'
    
    def display(self):
        return self.name


# protected, 1 - _
class B():
    _name = 'Name'
    
    def _display(self):
        return self._name

# private , 2 - _
class C():
    __name = 'Name'
    
    def __init__(self, name, age):
        self.__name = name 
        self.__age = age
        
    def __display(self):
        return self.__name
    
    def print_name(self):
        return self.__display()
    
a = A()
print(a.name, a.display())
b = B()
b._name, b._display()
c = C()
c.__display()
class Test():
    pass
dir(Test)

class A(object):

    def say_hello(self):
        print('Hello world!')

class B(A):
    
    def say_hello(self):
        print(super().say_hello())
        print('Today is: some date')
    
    def say_bye(self):
        print('Bye')


class Shape(object):
    
    def __init__(self, param1) -> None:
        self.param1 = param1
        
        
class Square(Shape):
    
    def __init__(self, param1, param2) -> None:
        self.param1 = param1
        self.param2 = param2
        
    
    def calculate_area(self):
        return self.param1 * self.param2
    
sq = Square(4, 4)

sq.calculate_area()

a_ = A()

a_.say_hello()

b_ = B()

b_.say_hello()

b_.say_bye()

class Animal(object):
    
    def __init__(self, name) -> None:
        self.name = name  
        
    def sound(self):
        pass 
    
    def eat(self):
        print('Food')     
    
    def drink(self): 
        pass 
    
class Dog(Animal):
    
    def __init__(self, name, poroda) -> None:
        super().__init__(name)
        self.poroda = poroda
        
    def sound(self):
        print('Dog bark')  
   
        
dog1 = Dog('Dog1') # __init__ Animal
dog1
dog1.sound() 
dog1.eat()
dog1.name

dog1.sound()

class Cat(Animal):
    def sound(self):
        print('Cat cat sound')
        

cat1 = Cat('Cat1')
print(cat1.sound())

class T():
    pass

class T():
    pass
class A():
    
    def hello(self):
        print('Hello World!')
        return 2
        
    def bye(self):
        print('Bye!')
        return 1
        
        
class B(A):
    def _today(self):
        print('Date: 02.11.23') 


class C(A):    
    def next_day(self):
        print('Date: 03.11.23')

    @staticmethod
    def hello():
        print('Hello')


class D(B,C):
    pass 


object1 = D()


print(object1.hello(), object1.bye())# , object1.today())

print(object1._today())

print('&' * 50)
object2 = C()
print(object2.hello(), object2.bye(), object2.next_day(), object2.hello())

D.__mro__

class Figure(object):
    
    def __init__(self, name:str):
        self.name = name 
    
    def display(self):
        print(f'{self.name}')
        
        
    @classmethod
    def alternative_init(cls):
        print(f'Class {cls}')
        # context 
        return cls('romb')        
        
    @staticmethod
    def timer(func):
        def wrapper(*args, **kwargs):
            
            start = time.time()
            result = func(*args, **kwargs)

        return wrapper
    

rec = Figure('Rectangle')

romb = Figure.alternative_init()

romb.name

object1.hello()

print(D.__mro__)
print(D.mro())

class Person(object):
    somet_attr = 'Person'
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print( f"Hello, my name is {self.name} and I am {self.age} years old.")

    def __repr__(self): 
        return f"Hello, my name is {self.name} and I am {self.age} years old."
    
person1 = Person(name = "John", age= 30)

print(person1.name, person1.age)
print(person1)

person2 = Person('Person1', 25)
print(person2, person2.somet_attr)

person2.salary = 90000

print(person2.salary)


class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def say_hello(self):
        super().say_hello()
        print(f"My salary is {self.salary} dollars.")

employee1 = Employee("Jane", 25, 50000)
employee1.say_hello() 


class Person():
    
    def __init__(self, name, age):
        self.name = name 
        self.age = age   
        
        
    def __str__(self):
        return f'Name: {self.name} Age: {self.age}'
    
    
    def display(self):
        return f'Name: {self.name} Age: {self.age}'
    
    
    def __eq__(self, person1):
        return person1.name == person2.name 
        


person1 = Person('User1', 28)
person2 = Person('User1', 30 )
print(person1)
print(person1.display())
print(person1 == person2)


dir(A)


class Person:  # class <name_of_class>(object)
    pass 

user1 = Person()


user1, type(user1)
class Person:
    dt = '2023-11-09'

user2 = Person()
user2.dt = '2023-11-08'
user2.dt
user3 = Person()
user3.dt
user3.name = 'User3'
user2.name

class Person:
    dt = '2023-11-09'
    
    def __init__(self, name:str, surname:str, age:int, isAdmin:bool = False):
        self.name = name 
        self.surname = surname
        self.age = age 
        self.isAdmin = isAdmin
    
    def display(self):
        print(f'Name: {self.name}, Surname: {self.surname}')
        
    def fullname(self):
        return self.name + self.surname
    

user1 = Person('Person1', 'SurnamePerson1', 25)
print(user1, user1.age)
user1.isAdmin
user1.name, user1.surname
user2 = Person('Person2', 'SurnamePerson2', 30)
user2.name, user2.surname
user1.display()
user2.fullname()


dict_ = {}
dict_2 = {}

def add_dict(key, value):
    global dict_ 
    
    dict_[key] = value


class List_:
    
    def __init__(self, element):
        self.element = []
        
    def add(self, value):
        self.element.append(value)
        
    def display(self):
        print(self.element)


arr1 = List_([])
arr1.add(1)
arr1.add(2)
arr1.display()
arr1.dt = '2023-11-09'
arr1.dt


class Rectangle: # class - struc, blueprint 
    pass  
    
fig = Rectangle() 
print(fig, type(fig))

class Rectangle: 
    
    def __init__(self, width:float, height:float): # конструктор, fist arg self
        self.width = width
        self.height = height
    
    
    def display(self): 
        return f'Width {self.width}\nHeight {self.height}'
    
    
    def area(self):
        return self.width * self.height


sq = Rectangle(4, 4)
print(sq, sq.height, sq.width)
print(sq.display(), sq.area())

sq1 = Rectangle(5, 20)
print(sq1.area(), sq1.display())



class Rectangle:
    """
    Клас Rectangle представляє прямокутник з атрибутами width та height.

    :ivar width: Ширина прямокутника.
    :vartype width: float
    :ivar height: Висота прямокутника.
    :vartype height: float
    """
    def __init__(self, width, height):
        """
        Конструктор класу Rectangle.

        :param width: Ширина прямокутника.
        :type width: float
        :param height: Висота прямокутника.
        :type height: float
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Метод area обчислює площу прямокутника.

        :return: Площа прямокутника.
        :rtype: float
        """
        return self.width * self.height

    def perimeter(self):
        """
        Метод perimeter обчислює периметр прямокутника.

        :return: Периметр прямокутника.
        :rtype: float
        """
        return 2 * (self.width + self.height)
    


import seaborn as sns

df = sns.load_dataset('Iris')

df.head()

some_re = Rectangle(4, 4)
some_re.perimeter()

from faker import Faker

class A():
    pass 

a = A()

class BankAccount(object):
    
    def __init__(self, account_number:str, balance: float = 0.0) :
        self.account_number = account_number
        self.balance = balance
    
    def __repr__(self) :
        return f'Bank_name: {self.account_number} Balance: {self.balance}'
    
    def add_money(self, amount):
        self.balance += amount  
    
    def minus_money(self, amount):
        if amount > self.balance:
            print(f'No money: {self.balance - amount}')
        else: 
            self.balance -= amount
            
    def __eq__(self, param1) -> bool:
        return self.account_number == param1.account_number
    


dir(BankAccount)
acc1 = BankAccount('id1', 100)
acc2 = BankAccount('id2', 100)
acc1 == acc2
print(acc1)
acc1.add_money(10)
acc1.balance
acc1.minus_money(111)
acc1.balance
acc1.minus_money(100)
acc1.balance

print(Rectangle.__doc__, Rectangle.area.__doc__)

# Class 
# Task 1
class Rectangle:
    """
    Клас Rectangle представляє прямокутник з атрибутами width та height.

    :ivar width: Ширина прямокутника.
    :vartype width: float
    :ivar height: Висота прямокутника.
    :vartype height: float
    """
    def __init__(self, width, height):
        """
        Конструктор класу Rectangle.

        :param width: Ширина прямокутника.
        :type width: float
        :param height: Висота прямокутника.
        :type height: float
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Метод area обчислює площу прямокутника.

        :return: Площа прямокутника.
        :rtype: float
        """
        return self.width * self.height

    def perimeter(self):
        """
        Метод perimeter обчислює периметр прямокутника.

        :return: Периметр прямокутника.
        :rtype: float
        """
        return 2 * (self.width + self.height)
    

# Task 2 
class BankAccount(object):
    
    def __init__(self, account_number, balance = 0):
        self.account_number = account_number
        self.balance = balance 
        
    def check_balance(self):
        print(f'Account number: {self.account_number} Have balance: {self.balance}')
        
    def update_balance(self, value):
        self.balance = self.balance - value
        return self.balance
    
user1 = BankAccount('3040', 120_000)
print(user1.account_number)
print(user1.check_balance())

user1.update_balance(10_000)

print(user1.check_balance())


# Task 3
class Car:
    
    def __init__(self, make, model, year):
        self.make = make
        self.model = model 
        self.year = year 
    
    def fast(self):
        pass 
    
    def stop(self):
        pass


# Task 4
class Animal:
    
    def __init__(self, name, age):
        self.name = name 
        self.age = age 
    
    def sound(self):
        match self.name:
            case 'cat': print('some sound')
            case _: print(f'Sound animal:')
        
        
class Dog(Animal):
    def sound(self):
        super().sound()
        print('Bark Bark')
        
class Cat(Animal):
    def sound(self):
        super().sound()
        print('Some sound')


# Task 5
class Figure(object):
    
    PI = 3.14159 
    E = 2.71 
    
    def __init__(self, name) -> None:
        self.name = name
        
    def display(self):
        print(self.name)
        
        
class Circle(Figure):
    PI = 3.14159
    
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return round(self.radius ** 2 * Circle.PI, 2)
    
    
    def lenght_of_circle(self):
        return round(2 * Circle.PI * self.radius, 2)
    
circle1 = Circle(5)

print(circle1.area(), circle1.lenght_of_circle())


class People(object):
    def __init__(self, status:str = 'FTE', gender: str = 'M'):
        self.status = status
        self.gender = gender
        
        match status:
            case 'FTE':
                self.ft = 1.0
            case 'FTE 0.5':
                self.ft = 0.5

    def get_status(self):
        print(self.status)

    def get_gender(self):
        print(self.gender)



people1 = People('FTE', 'M')
people1.get_status(), people1.get_gender()


class Employee(People):
    def __init__(self, name, position, salary, status, gender):
        super().__init__(status, gender)
        self.name = name
        self.position = position
        self.salary =salary

    def increase_salary(self, incr_sal: float):

        if incr_sal < 0:
            print("Invalid operation: Salary increase should be a positive value.")
        else:
            self.salary += incr_sal


# Task 6
class Employee:
    
    def __init__(self, name, position, salary):
        self.name = name 
        self.position = position
        self.salary = salary
    
    def increase_salary(self, amount):
        return self.salary + amount
    
    def descrease_salary(self, amount):
        return self.salary - amount

# Task 7
class Book:
    
    def __init__(self, title, author, year) -> None:
        self.title = title 
        self.author = author 
        self.year = year 
        
    def display(self):
        print(f'Book name is {self.title}\nAuthor name {self.author}\nYear ob book: {self.year}')
        
    def __repr__(self):
        return f'Book name is {self.title}\nAuthor name {self.author}\nYear ob book: {self.year}'
    

night_of_dragon = Book(title = 'Нічь драконів',author = 'Артур Кнаак', year = '2015')
print(night_of_dragon)


# Task 8 
class RectangleArea:
    
    def __init__(self, length,  width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
class Shape:
    PI = 3.14159
    
    def __init__(self, *args) -> None:
        self.args = args
        
        
    def match_figure(self):
        if len(self.args) == 1:
            return 'Circle'
        elif len(self.args) == 2:
            if self.args[0] == self.args[1]:
             return 'rect'
    
    def is_match(self):
        self.figure_type = Shape.match_figure(self)
        self.is_match_ = True if self.figure_type is not None else False

    def calculate_per(self):
        if self.is_match_ == False:
            return None 
        
        match self.figure_type:
            case 'Circle':
                return 2 * Shape.PI * self.args[0]
            case _ :
                pass


circle = Shape(4,4)
circle.is_match()
circle.figure_type


circle.calculate_per()


# Task 10
class Shape(object):
    
    def __init__(self, name) -> None:
        self.name = name  
        
    def __repr__(self) -> str:
        return f'Name of figure {self.name}'
    

class Rectangle(Shape):
    
    def __init__(self, name, w:float, h:float) -> None:
        super().__init__(name)
        self.w = w  
        self.h = h  
    
    def __repr__(self) -> str:
        super().__repr__()
        return f'W: {self.w} H: {self.h}'
    
    def perim(self): 
        return 2 * (self.w + self.h)
    
    
class Circle(Shape):
    PI = 3.14
    
    def __init__(self, name, rad:float) -> None:
        super().__init__(name)
        self.rad = rad    
        
    def __repr__(self) -> str:
        super().__repr__()
        print(f' Rad: {self.rad}')
    
    def perim(self):
        return  2 * Circle.PI  * self.r
print('Hello World!')


'''
Console command
pwd - показати поточну директорію
mkdir - створити директорію (mkdir -p /)
cd - перехід на потрібну директорію
touch - створити файл
ls - показати список всіх директорій і файлів (ls -a, ls -l, ls -al)
clear - очистити консоль
mv - перемістити файл
rm/rmdir - видалити file/directory
cat - показати вміст файла
head/tail - показати вміст файла
open - відкрити файл
man - інформація про команду

Task 1. Create new dir with name TestCons. 
Task 2. Create test.txt. 
Task 3. Fill text with some data. 
Task 4. Display first 10 row from head and 5 rows from tail. 
Task 5. Delete dir  TestCons, before delete transfer test.txt file to Dowloands
1. pwd ->  mkdir TestCons -> ls -> cd TestCons -> touch test.txt -> nano test.txt -> head -n 10 test.txt -> tail -n 5 test.txt
2. mv test.txt /Users/alksandr/Desktop -> ls -> .. -> rmdir TestCons -> ls
Magic command
Task 1. Create new dir with name TestCons. 
Task 2. Create test.txt. 
Task 3. Fill text with some data. 
Task 4. Display first 10 row from head and 5 rows from tail. 
Task 5. Delete dir  TestCons, before delete transfer test.txt file to Dowloands 
%lsmagic # показати всі команди 


%run first_lesson.py # запустити файл %run <file_name>
%time  # exac time 
list1 = []
for i in range(0, 1000):
    list1.append(i)


%pycat <filename> # показати контент файлу 
%who first_lesson.py # показати зміннні у файлі 
%who list # показати змінни у поточному файлі 
#%pinfo  показати інформацію про змінну
%pinfo list1 
def create_list(number: int = 100) -> list:
    return [i for i in range(1, number)] if isinstance(number, int) else []
%timeit create_list() # %timeit - порахувати час виконання функції
Декоратори
Декоратор - це функція яка дозволяють змінювати поведінку інших функцій без необхідності змінювати їх початковий код
Функція в середині функції. Функція яка приймає аргумент функцію.
'''

from functools import * # бібліотека з декораторами 
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Час виконання {func.__name__}: {end_time - start_time} секунд")
        return result
    return wrapper
@timer
def create_list(number: int = 100) -> list:
    return [i for i in range(1, number)] if isinstance(number, int) else []

print(sum(create_list(10_000000)))

@timer # декора
@timer
def sum_(array: list) -> int:
    return sum(i for i in array) if array is not None else 0
sum_(create_list(10_000))

create_list(10000)


def log_function_data(func):
    def wrapper(*args, **kwargs):
        print(f"Call function : **{func.__name__}** with arguments: {args} and {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@log_function_data
def add(x, y):
    return x + y
add(10, 5)


registered_functions = []

def register(func):
    
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        registered_functions.append(func.__name__)
        return result
    
    return wrapper

@register
def func1():
    pass

@register
def func2():
    pass
func2()
func1()


registered_functions

func1()
func2()
registered_functions

func1.__name__

registered_functions

@timer
@cache
def factorial(n):
    return n * factorial(n-1) if n else 1
@lru_cache(maxsize=10)
def factorial(n):
    return n * factorial(n-1) if n else 1


def memoize(func):
    cache = {}
    @wraps(func)
    def wrapper(*args, **kwargs):
        if args in cache:
            return cache[args]
        result = func(*args, **kwargs)
        print(f'Add new elements to cache: {cache}')
        cache[args] = result 
        
        return result 
    return wrapper
def retry_connection(func,max_attemps: int = 4, delay = 5):
    
    @wraps(func)
    def wrapper(*args, **kwargs):
        attemps = 0 
        while attemps < max_attemps:
            try: 
                return func(*args, **kwargs)
            except Exception as e:
                print(f'Something wrong with called function: {func.__name__}. Attems left {attemps}')
                time.sleep(delay)
                attemps += 1
        return func(*args, **kwargs)
    return wrapper


@retry_connection
def factorial(n):
    return n * factorial(n-1) if n else 1
@memoize
def factorial(n):
    return n * factorial(n-1) if n else 1
factorial(10)


@timer
def factorial(n):
    return n * factorial(n-1) if n else 1
factorial(5)


factorial(10)

factorial(100)


# Task 1. Написати декоратор, де буде показувати імя функції та дату 
import datetime 

def name_and_time(func): 
    
    def wrapper(*args, **kwargs):
        
        print(f'Name of function: {func.__name__}\nToday date is {datetime.datetime.now()}')
        result = func(*args, **kwargs)
        return result 
    return wrapper 
@name_and_time
def hello(name: str) -> str:
    return f'Hello {name}'

hello('User1')


# Task 2. Написати декоратор, де буде перед викликом кожної функції delay 30 seconds
def delay_dec(func):
    
    def wrapper(*args, **kwargs): 
        time.sleep(30)
        return func(*args, **kwargs)
    return wrapper

@delay_dec
def connection(api_name: str) -> str | None:
    pass 
connection('API')
#while attems < 3:
#   connection 
# Task 3. Використати декоратор, який буде зберігати cache, реалізувати для чисел Фіббоначі
# * - додаткова зробити власний декоратор memoize, та використати декоратор lru_cache, який буде працювати швидше

def fibb(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibb(n - 1) + fibb(n - 2)


@cache
def fibb(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibb(n - 1) + fibb(n - 2)
%%timeit
fibb(1200)


@lru_cache(maxsize = 4)
def fibb(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibb(n - 1) + fibb(n - 2)
%%timeit
fibb(1200)


'''
Git
Базові команди:

git
git --version # перевірити git версію 

git config --global user.name "your_username"
git config --global user.email "your_email_address@example.com"
git config --global --list

git init # start 
git status - показати поточний статус 
git add (добавити файл-и) ./-A/--all - добавити всі файли 
git commit -m 'описати дії які були зроблені, зазвичай перший комміт Init commit'
git push -u origin <branch name> # відправити на зовній репозіторій 

git pull # підтягунути змінни з серверу 

git checkout -b <створити альтернативну версію коду>

Add commands
git
git log - показати історію 
git log --since <вказати з якої дати показати історію>

git annotate <імя файлу> # показати історію змінн файлу

git diff <показати змінни> <з чим будемо порівнювати>

git branch # показати всі гілки 


git config --global alias.<псевдонім> <команда>
git config --global alias.st status

Best practise
Use:

freeze - pip freeze > requirements.txt # запиши всі залежності в текстовий файл
flake8 - аналізатор коду, для налаштування використовуйте .flake8
gitignore - файл для ігнорування файлів
'''