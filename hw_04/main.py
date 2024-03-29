'''
Домашнє завдання 4

1. Прочитайте офіційну специфікацію формату та приклади -
https://docs.python.org/3.4/library/string.html#formatspec

2. Прочитайте документацію формату дата та час -
https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior 
А краще тут
https://www.w3schools.com/python/python_datetime.asp
https://www.programiz.com/python-programming/time

3. Прочитайте цей посібник з функцій
https://docs.python.org/3.7/tutorial/controlflow.html#defining-functions
https://www.w3schools.com/python/python_functions.asp

4. Використовуйте модуль часу, щоб порівняти продуктивність «ефективного» методу пошуку простих чисел із простою реалізацією 
(без перерв, тестування за всіма числами тощо). Перевірте кілька діапазонів пошуку простих чисел (наприклад, до 100, до 1000 і т.д.) 
Ефективний метод - будь який математично визначиний підхід обрахунку.
Рекомендую дивитись метод Решето Эратосфена -
https://uk.wikipedia.org/wiki/%D0%A0%D0%B5%D1%88%D0%B5%D1%82%D0%BE_%D0%95%D1%80%D0%B0%D1%82%D0%BE%D1%81%D1%84%D0%B5%D0%BD%D0%B0


Рекомендації до виконання:

У 4 завданні має бути дві різні функції для пошуку простих чисел: simple_prime_search та sieve_eratosthenes. 
Також є функція measure_time, яка вимірює час виконання заданої функції та повертає результат разом із часом виконання.

simple_prime_search: Ця функція використовує простий спосіб перевірки, чи є число простим, перебираючи всі можливі дільники числа. 
Це доволі простий та очевидний спосіб пошуку простих чисел, але не є найефективнішим, особливо для великих чисел.

sieve_eratosthenes: Ця функція використовує решето Ератосфена, що є більш ефективним методом для пошуку простих чисел. 
Алгоритм працює шляхом виключення всіх чисел, які є кратними простим числам. Результатом є список простих чисел до заданого ліміту.

measure_time: Це функція вимірювання часу виконання іншої функції.

Вона приймає функцію func та додаткові аргументи *args та ключові аргументи **kwargs. Вона містить:

start = time.time(): Тут встановлюється початковий час виконання, використовуючи функцію time.time(), яка повертає поточний час у секундах.

result = func(*args, kwargs): Функція викликає передану функцію func з переданими аргументами *args та ключовими аргументами **kwargs. 
Використання *args дозволяє передавати будь-яку кількість позиційних аргументів, а **kwargs дозволяє передавати будь-яку кількість ключових аргументів.

end_time = time.time(): Тут встановлюється час завершення виконання функції.

print(f"Time of the {func.name} function: {end_time - start:.10f} sec."): 
Виводить інформацію про час виконання функції. func.__name__ дає ім'я переданої функції, і час виконання виводиться з точністю до 10 знаків після коми.

return result: Повертає результат виконання функції func.

Застосування *args і **kwargs дозволяє цій функції працювати з будь-якою функцією, незалежно від її сигнатури 
(кількість аргументів і їхні назви). Функція може бути викликана з будь-якою кількістю аргументів, і вони будуть передані відповідній функції.

Отже, функція measure_time повертає прості числа завдяки запису func(*args, **kwargs), 
тобто вона повертає результат виконання функції func, де func – це функція simple_prime_search або sieve_eratosthenes, тобто функція, 
що повертає прості числа, та друкує час виконання функції func. Функція measure_time приймає функцію func та її аргументи, викликає функцію, 
вимірює час її виконання та виводить результат та час виконання.

Остання частина коду викликає функцію measure_time для обидвох функцій 
(simple_prime_search та sieve_eratosthenes) для різних значень n (діапазони 100, 1000, 10000) 
та виводить час виконання кожної з них. Це дозволяє порівняти ефективність обох методів пошуку простих чисел для різних значень n.
'''

import time

# Проста функція для перевірки чисел
def simple_prime_search(n):
    primes = []
    for num in range(2, n):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

# функція Решето Ератосфена
def sieve_eratosthenes(n):
    primes = []
    sieve = [True] * (n + 1)
    for num in range(2, int(n ** 0.5) + 1):
        if sieve[num]:
            for multiple in range(num * num, n + 1, num):
                sieve[multiple] = False
    primes.extend(num for num in range(2, n + 1) if sieve[num])
    return primes

# Решето Вікіпедія
import math
def wiki_eratosthenes(n):
    prime = [True] * n
    prime[0], prime[1] = False, False # 0 та 1 не є простими
    for i in range(2, math.ceil(math.sqrt(n))):  # від 2 до квадратного кореня з N 
        if prime[i]:  # якщо просте видаляємо всі числа кратні до нього
            j = i * i   # для i=2,j будуть такі значення 4,6,8,10,12... для i=3 j — 9,12,15,18,21...
            while j < n:
                prime[j] = False
                j += i

# Функція для визначення часу відпрацювання функцій
def measure_time(func, *args, **kwargs):
    start = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    print(f"Час виконання функції {func.__name__}: {end_time - start} секунд")
    return result

# Діапазон перевірочних чисел
ranges = [100, 1000, 10000]

# Текст для виводу відпрацьованих функцій
for i in ranges:
    print(f"Діапазон пошуку простих чисел до {i}:")
    print("Простий метод пошуку:")
    measure_time(simple_prime_search, i)
    print("Метод решета Ератосфена:")
    measure_time(sieve_eratosthenes, i)
    print("Метод решета Ератосфена_Вікіпедія:")
    measure_time(wiki_eratosthenes, i)
    print("---------------------------------------")