'''
04/04/2024
Lesson 7. Intro to NumPy
Date: 2024-04-04
Topics:

Numpy intro
Vector/Matrix/Tensor
Vector math
Filter array(boolen mask, where)
SQlite3
Materials:

NumPy
NumPy doc
Tutorial
Sqlite3
NumPy - це бібліотека для мови програмування Python, призначена для виконання обчислювальних завдань на багатовимірних масивах або матрицях.

NumPy дозволяє створювати масиви даних будь-якого розміру, а також виконувати операції з ними, такі як математичні операції, зрізи, індексування та багато іншого. Вона також надає функції для лінійної алгебри, статистичного аналізу, перетворення Фур'є та багатьох інших алгоритмів.

Використання NumPy в Python дозволяє швидко та зручно обробляти великі обсяги даних та прискорює виконання математичних операцій. Вона також може бути використана разом з іншими бібліотеками Python для створення наукових додатків та інструментів.

NumPy - написаний на С, в основу покладені наступні бібліотеки: BLAS, LAPACK - Fortran

Install Numpy:

Conda: conda install numpy

Pip-pip3: pip install numpy


import numpy as np # імпорт функціоналу та даємо псевдонім 
import matplotlib.pyplot as plt 
import seaborn as sns
# from numpy import arange, stack, ethc
Python list:

Save information different type
Numpy array:

Save inforamtion one type
Less memory
Fast math operation
list1 = [[1,2,3, 4], [5, 6, 7, 8]]
arr = np.array([[1,2,3, 4], [5, 6, 7, 8]])
print(list1, list1.__sizeof__(), end = '\n\n')
print(arr, arr.__sizeof__())
[[1, 2, 3, 4], [5, 6, 7, 8]] 56

[[1 2 3 4]
 [5 6 7 8]] 192
# Vector - one dim array 
vector = np.array([1,2,3,4,5])
print(vector, vector.shape)
print(vector.reshape(-1,1),vector.reshape(-1,1).shape)
# Matrix - two dim array, n * m - table , rows * columns = mat
arr = np.array([[1,2,3, 4], [5, 6, 7, 8]])
print(f'Array: {arr}\nShape: {arr.shape}', end = '\n\n')
print(arr.reshape(4, 2), arr.reshape(1, 8))

# Квадратая матрица - row = column , 2x2, 3x3, 4x4, etc rows = columns
arr1 = np.array([[1,2], [5, 6]])
print(f'Array: {arr1}\nShape: {arr1.shape}')
# Tensor - многомірна matrix
arr = np.array([
    [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],
    [[13, 14, 15, 16], [17, 18, 19, 20], [21, 22, 23, 24]]
])
print(f'Array: {arr}\nShape: {arr.shape}')




[1, 2.5, True, 0, 10.0, 'string']
# Zeros - create zero array
zero = np.zeros(5)
print(zero)
zero_2d = np.zeros((2, 5)) # arg - tuple, where first arg - row, second - column
print(zero_2d)
zero_3d = np.zeros((2, 5, 2))
print(zero_3d)
# Ones - create one-value matrix
arr = np.ones((3,4)) # tuple: [0] - row, [1] - columns
print(arr, arr.shape)
# Arange - generate vector
arr = np.arange(1, 13) # range - start, end, step
print(arr, arr.shape)

arr1 = np.arange(1, 13).reshape(3, 4) # 2d - matrix
print(arr1, arr1.shape, arr1.size)
# Linspace - рівномірний розподіл
arr = np.linspace(0, 1, 10) # three arg - start, end, count of values
print(arr)
dir(arr)[96:] # check all methods
arr_bool = np.array([True, False, True, False, False])
print(arr_bool) # Bool

arr_float = np.array([True, 3.14, 1, 15, False])
print(arr_float) # Float

arr_string = np.array(['String', 3.14, 15, False, True])
print(arr_string) # String
[ True False  True False False]
[ 1.    3.14  1.   15.    0.  ]
['String' '3.14' '15' 'False' 'True']
# to create with dtype, use dtype 
arr_uint8 = np.arange(1, 12, dtype= np.uint8) # unsig type
print(arr_uint8, arr_uint8.dtype)

arr_float32 = np.array([1,2,3,4, 5.14, False, True, -17], dtype= np.float32)
print(arr_float32, arr_float32.dtype, arr_uint8.size)
# Astype - convert data type
arr1 = np.array([9, 12, True, 3.13]).astype('<U5') # string Unicode
arr2 = np.array([9, 12, True, 3.13, 'Numpy']) # string
arr3 = np.array([9, 12, True, 3.13]).astype(np.uint16) # +int
arr4 = np.array([9, 12, True, 3.13]).astype(np.int64)  # int
arr5 = np.random.random((3,4))
arr6 = np.array([[1,2,3], [4,5,6.0], [7, 8, 9]])

for i in range(1, 7):
    print(eval(f'arr{i}'))
    print(eval(f'arr{i}.dtype'), end = '\n\n') # <U - unicode with len
np.random.randint(5, 10, size = 10)
numpy.add(x1, x2) - додавання двох векторів
numpy.subtract(x1, x2) - віднімання одного вектора з іншого
numpy.multiply(x1, x2) - поелементне множення двох векторів
numpy.divide(x1, x2) - поелементне ділення одного вектора на інший
numpy.dot(x1, x2) - скалярний добуток двох векторів \

# Vector math 
x1 = np.array([1, 2, 3])
x2 = np.array([4, 5,6])
print(f'Add: {x1 + x2} or {np.add(x1, x2)}')
print(f'Subtract: {x1 - x2} or {np.subtract(x1, x2)}')
print(f'Multiply: {x1 * x2} or {np.multiply(x1, x2)}')
print(f'Divide: {x1 / x2} or {np.divide(x1, x2)}')
print(f'Dot: {np.dot(x1, x2)}')
print(f'Multiply by number: {x1 * 3}')
Index and Slicing
basic: [start: stop: steps]
n-d index: [start:stop:steps][start:stop:steps]

arr = np.array([[1,2,3, 4], [5, 6, 7, 8]])
# arr[refers to axis 0(rows), refers to axis 1 (columns)]
print(arr, arr[0, :], arr[:, 1], arr.shape, sep= '\n\n') # [][]
Filtering data in numpy:

Fancy index with boolen mask - return array of elements
where - return index
# & - логічне так(and)
# | - логічне або(or)- pipe
# ~ - логічне ні(not)
arr = np.array([[1,2,3, 4], [5, 6, 7, 8], [9,10,11,12]])

even_number = arr % 2 == 0 # Arr true/false
print(even_number, arr[~even_number], arr[~(arr % 2 == 0) & (arr > 5)], end = '\n\n')

big_mean = arr > arr.mean()
print(big_mean, arr[big_mean], end = '\n\n')
Comdine diff statemens
& - логічне та
| - логічне або
~ - логічні ні

two_statemnt = (arr > 2) & (arr < 10)
print(two_statemnt, arr[two_statemnt], end = '\n\n')

two_statemnt = (arr > 2) | (arr != 10)
print(two_statemnt, arr[two_statemnt], end = '\n\n')

print(arr[(arr % 2 == 0) & (arr < 10)]) # or you write in []
arr.shape[0]
# Task 1. Create list with 50 elements, reshape in 3 - var
# 10x5, 25x2, 5x10, 2x25, 1x50, 2x5x5 - arange/randint 
arr = np.arange(1, 51, dtype = np.uint16)
print(arr.reshape((10, 5)), arr.reshape((2, 25)), arr.reshape((1, 50)), sep= '\n\n' )
# Task 2. Find elements, where elements more than 20 and less 30 
print(arr[(arr > 20) & (arr < 30)])
# Task 3. Find elements, where elements is even 
print(arr[~arr % 2 == 1])
# Task 4. Generate chess dashboard - elem 
print(np.zeros((8, 8)))
# Task 5. Find elements, where elements is NOT even, less than 41 and more then 15 and elements not equal 21
print(arr[(arr % 2 != 0) & ((arr > 15) & (arr < 41)) & (arr != 21)])
# Task 6. Find sum of diagonal for matrix (5, 5). Step 1: generate matrix. Step 2: display diagonal, Step 3: Find sum of main dianogal, Step 3: Find alternative diagonal, find elements what more than sum of main diagonal 
# - elem diagonal
arr = np.arange(1, 26).reshape((5,5))
arr
Where - function numpy.where(condition[, x, y])

print(arr)
print(np.where(arr == 4)) # return position(index)
print(np.where(arr % 2 == 0))
print(arr)
print(np.where(arr % 2 == 0,arr, 'Not True')) # three args: condit, array, default value
arr = np.array([[1,2,3, 4], [5, 6, 7, 8]])
print(arr, end = '\n\n')
print(arr.flatten(), end = '\n\n') # to one dimension, сплющує в одномірний массив, але при цьому створює копію 
print(arr.ravel()) # to one dimension, не створює копію
arr = np.arange(1, 65)
print(arr) 

print(arr.reshape((8,8)), arr.reshape((32,2)), sep = '\n\n')
help(np.ravel)
print(arr)
print(arr.reshape(4, 2)) # change size 
print(arr.shape[0], arr.shape[1],  arr.size)
print(arr.dtype)
one_to_ten = np.arange(1, 11)

plt.scatter(x = one_to_ten, y = one_to_ten * 2)
plt.show()
arr3d = np.array([[1,2,3, 4], [5, 6, 7, 8], [9, 10, 11, 22]])
print(arr3d, arr3d.shape)
print(arr3d.reshape(1, 2, 6))
Concatenate : join arrays, use axis
numpy.concatenate((a1, a2, ...), axis=0)





np.concatenate?
arr1 = np.arange(1, 5)
arr2 = np.arange(5, 10)
print(arr1, arr2)
arr_concate = np.concatenate((arr1, arr2))
print(arr_concate)
arr1 = np.array([[1,2,3], [4,5, 6]])
arr2 = np.array([[2,3, 4], [7,8,9]])
arr1
arr2
arr_concate = np.concatenate((arr1, arr2)) # Join array
print(arr_concate)
Stack - використовується для об'єднання масивів уздовж нової осі
numpy.stack(arrays, axis=0)

hstack - використовується для горизонтальної конкатенації (об'єднання) двох або більше масивів вздовж другої осі (осі 1) - тобто об'єднання елементів рядків.
vstack - використовується для вертикальної конкатенації (об'єднання) двох або більше масивів вздовж першої осі (осі 0) - тобто об'єднання елементів стовпців.
dstack використовується для об'єднання двох або більше масивів вздовж третьої осі (ось 2) - тобто об'єднання елементів у глибину
a1 = np.array([1, 2, 3])
a2 = np.array([4, 5, 6])
a3 = np.array([7, 8, 9])
print(a1,a2,a3)
result = np.stack((a1, a2, a3), axis=1)

print(result)
#  display:
# [[1 4 7]
#  [2 5 8]
#  [3 6 9]]
# Hstack 
a1 = np.array([1, 2, 3])
a2 = np.array([4, 5, 6])
print(np.hstack((a1, a2)))
# Vstack
a1 = np.array([1, 2, 3])
a2 = np.array([4, 5, 6])

print(np.vstack((a1, a2)))
# Dstack
a1 = np.array([[1, 2], [3, 4]])
a2 = np.array([[5, 6], [7, 8]])

print(np.dstack((a1, a2)))
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

arr = np.stack((arr1, arr2))
print(arr, ) # axis add 

print(np.hstack((arr1, arr2)))
print(np.vstack((arr1, arr2)))
print(np.dstack((arr1, arr2)))
Array_split - function to split array multiple sub-arrays of equal or near-equal size.
arr = np.arange(1, 12)
new_arr = np.array_split(arr, 3) # розбити на підмассиви
print(new_arr)
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
result = np.array_split(arr, 3)
print(result)
Sort - function return sorted copy
arr = np.array([[3, 2, 4], [6, 5, 1]])
arr
np.sort?
result = np.sort(arr, axis=1,  kind = 'mergesort')[::-1]
print(result)
arr
np.sum(arr, axis = 1)
np.sum(arr)
np.max(arr, axis = 1)
np.mean(arr, axis = 0)
list_  = [
    [1, 2, 3]
    , [4,5,6]
    , [7,8,9]
]
for i in list_:
    for j in i:
        print(j * 3)
3
6
9
12
15
18
21
24
27
ORM
# Connect with BD 
import sqlite3

# create a connection to the database
conn = sqlite3.connect('example.db')

print(conn)
# create a table
conn.execute('''CREATE TABLE IF NOT EXISTS
             users (id INTEGER PRIMARY KEY, name TEXT)''')
'''
'''
# commit the changes
conn.commit()

# close the connection
conn.close()
<sqlite3.Connection object at 0x1568acc40>
!pip install Faker
DEPRECATION: Configuring installation scheme with distutils config files is deprecated and will no longer work in the near future. If you are using a Homebrew or Linuxbrew Python, please see discussion at https://github.com/Homebrew/homebrew-core/issues/76621
Requirement already satisfied: Faker in /usr/local/lib/python3.9/site-packages (19.13.0)
Requirement already satisfied: python-dateutil>=2.4 in /Users/alksandr/Library/Python/3.9/lib/python/site-packages (from Faker) (2.8.2)
Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.9/site-packages (from python-dateutil>=2.4->Faker) (1.16.0)
DEPRECATION: Configuring installation scheme with distutils config files is deprecated and will no longer work in the near future. If you are using a Homebrew or Linuxbrew Python, please see discussion at https://github.com/Homebrew/homebrew-core/issues/76621

[notice] A new release of pip is available: 23.3.1 -> 24.0
[notice] To update, run: python3.9 -m pip install --upgrade pip
!python 3.10 -m install faker
/Library/Frameworks/Python.framework/Versions/3.11/Resources/Python.app/Contents/MacOS/Python: can't open file '/Users/alksandr/Desktop/BI-18-Python/Lesson_files/3.10': [Errno 2] No such file or directory
from faker import Faker

fake = Faker()

for i in range(1, 10):
    print(fake.first_name())
---------------------------------------------------------------------------
ModuleNotFoundError                       Traceback (most recent call last)
Cell In[15], line 1
----> 1 from faker import Faker
      3 fake = Faker()
      5 for i in range(1, 10):

ModuleNotFoundError: No module named 'faker'
from faker import Faker

fake = Faker()

Faker.seed(42)

name = ['User1', 'User2', 'User3', 'User4']

conn = sqlite3.connect('example.db')

for i in range(1, 4):
    conn.execute("INSERT INTO users (id, name) VALUES (?, ?)", (i, name[i]))

conn.commit()

# close the connection
conn.close()
---------------------------------------------------------------------------
IntegrityError                            Traceback (most recent call last)
Cell In[19], line 12
      9 conn = sqlite3.connect('example.db')
     11 for i in range(1, 4):
---> 12     conn.execute("INSERT INTO users (id, name) VALUES (?, ?)", (i, name[i]))
     14 conn.commit()
     16 # close the connection

IntegrityError: UNIQUE constraint failed: users.id
# create a connection to the database
conn = sqlite3.connect('example.db')

# retrieve data from the table
cursor = conn.execute("SELECT id, name FROM users")
cursor.fetchall()
[(1, 'User1'), (2, 'User1'), (3, 'User1')]
rows = cursor.fetchall() # fetchone
print(rows)

# print the data
for row in rows:
    print(row)

# close the connection
conn.close()
conn.close()
with sqlite3.connect('example.db') as conn:
    # create a cursor
    cursor = conn.cursor()

    # create a table
    # cursor.execute('''CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)''')
'''
'''
    # insert some data
    #cursor.execute("INSERT INTO users (id, name) VALUES (21, 'Alice')")
    #cursor.execute("INSERT INTO users (id, name) VALUES (22, 'Bob')")

    # commit the changes
    # conn.commit()

    # retrieve data from the tableike '
    cursor.execute("SELECT  id, name FROM users WHERE length(name) = 15 ORDER BY id DESC")
    rows = cursor.fetchmany(10) #fetchall, fetchone

    # _ - один символ 
    # % - будь-яку символ
    # print the data
    for row in rows:
        print(row)
# Task 1. Знайти всіх людей у кого на 3 позиції є літера f - like, substr
# Task 2. Знайти всіх людей у кого всього 14 символів імя - lenght, like
# Task 3. Знайти всіх людей у кого id < 50 - where 
with sqlite3.connect('example.db') as conn:
    
    cursor = conn.cursor()
    
    cursor.execute('''SELECT name FROM sqlite_master where type = 'table' ''')
'''
'''
    result = cursor.fetchall()
    
    for i in result:
        print(i)
with sqlite3.connect('example.db') as conn:
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE person (id INTEGER PRIMARY KEY, name TEXT, surname TEXT)''')
'''
'''
    for i in range(1, 16):
        conn.execute("INSERT INTO person (id, name, surname) VALUES (?, ?, ?)", (i, fake.first_name(), fake.last_name()))

    conn.commit()

    cursor.execute("SELECT id, name, surname FROM person")
    rows = cursor.fetchall()

    for row in rows:
        print(row)
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Cell In[22], line 6
      3 cursor.execute('''CREATE TABLE person (id INTEGER PRIMARY KEY, name TEXT, surname TEXT)''')
'''
'''
      5 for i in range(1, 16):
----> 6     conn.execute("INSERT INTO person (id, name, surname) VALUES (?, ?, ?)", (i, fake.first_name(), fake.last_name()))
      8 conn.commit()
     10 cursor.execute("SELECT id, name, surname FROM person")

NameError: name 'fake' is not defined
# Sqlite3 - create table person, with id: int, primary key, name: text, surname: text 
# заповнити 15 кортежі, use - faker, use - context manager
'''