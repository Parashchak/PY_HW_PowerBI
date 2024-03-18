# 05.03.2024

arr = []

while len(arr) < 3:
    number = input('Enter value: ').strip()
    
    if number.isdigit():
        arr.append(int(number))
    
    
print(arr)

while True: # cond 
    
    number = input('Enter value: ').strip()
    
    if number.isdigit():
        print('Yes it is number')
        break

number = 1

while number <= 5:
    print(number)
    number += 1
else:
    print('All done')

number = [1,2,3,4,5,6,7,8,9,10,11,12]

for i in number:
    if i % 2 != 0:
        continue
    else:
        print(i)
else:
    print('All done')

index_ = 0
while index_ != len(arr):
  if arr[index_].split(' ')[0].strip() in black_list:
    print('Black list name: ', arr[index_])
    break 
    
  index_ += 1
  print(arr[index_])

arr = [fake.name() for i in range(0, 10)]

black_list = ['Alfred']

# range - [) - діапозон 
range(0, 10)

# string string 
name = 'string string'
for i in range(0, len(name)): # iter 
    print(name[i],i)

# range - [) - діапозон 
range(0, 10)

# string string 
name = 'string string'
for i in range(0, len(name)): # iter 
    print(name[i],i)

# Task 1. Цикл - створити список із 10 element use - loops: while/for
# Task 2. Take as input 10 real numbers and calculate their average.
# Task 3. Print all multiples of 14 smaller than 1000.
# Task 4. Take an integer as input and test whether or not it is prime (a prime number is divisible only by 1 and itself).

# Task 1. Цикл - створити список із 10 element use - loops: while/for

# While loop
arr_1 = []
while len(arr_1) < 10:
    number = input('Enter you value: ')
    arr_1.append(number)
print(arr_1)

# for 
arr_2 = []
for i in range(1, 11):
    arr_2.append(i)
    
print(arr_2) 

# list comp 
arr_3 = [i for i in range(1, 11)] # element_add_tolist for value in iter
print(arr_3)

N = int(input('Enter n-value: ')) 

n_value = 0
sum_ = 0

while n_value < N:
    number = input('Enter number: ')

    if number.isdigit():
        sum_ += int(number)
        n_value += 1
        
print(sum_ / N)

# Task 1. Згенерувати список значеннь, від min до max. Min/Max - задає користувач 
#  Знайти в ньому суми чисел, для всіх значеннь які парні

# Task 1. Згенерувати список значеннь, від min до max. Min/Max - задає користувач 
#  Знайти в ньому суми чисел, для всіх значеннь які парні 

# 1 - var
min_num = 5 # rstrip, int
max_numb = 10 # rstrip, int

min_num, max_num = int(input('Enter min value: ').strip()), int(input('Enter max value: ').strip())
result = 0
if min_num > max_num:
    print('False')
else:
    for i in range(min_num, max_num + 1): # O(N)
        if i %  2 == 0:
            result += i
print(f'Min: {min_num} Max: {max_num} Sum: {result}')

# 2 - var
result_sum = sum([i for i in range(min_num,max_num + 1) if i % 2 == 0])
print(f'Result sum: {result_sum}')

# 3 - var
result_sum1 = sum(i for i in range(min_num,max_num + 1) if i % 2 == 0)
print(result_sum1)

# Task 3. Calculate sum of string. For calculate sum - using function ord. String -> s - 98, t - 99, -> sum
# Task 4. Check if all char in strings is number. String - it is user number
# Task 5.  User enter number. Next calculate power number from 1 to 10. Example: 5, 5  1, 5  2 .. 5 ** 10

