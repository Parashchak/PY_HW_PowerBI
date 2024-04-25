'''
Домашнє завдання 6



1. Завантажте набір даних фільмів pandas

2. Перерахуйте всі стовпці набору даних та вивчіть їх типи. Вивчіть статистику з різних областей. Опишіть, які дані ми маємо

3.Скільки всього фільмів у наборі даних?

4. Скільки фільмів міститься у наборі даних за кожний рік?

5. Покажіть детальну інформацію про найменш і найприбутковіші фільми в наборі

6. Значення "Жанр" часом здається непослідовним; спробуйте знайти ці невідповідності та виправити їх

7. Збережіть (у новий файл CSV) 10 найкращих комедій за кількістю глядачів; покажіть лише назву фільму, рік та студію

8.Використовуйте pip для встановлення двох бібліотек: lxml, MySQL-connector-python#pip



Рекомендацї по виконанню:


1. Завантажте набір даних про фільми в бібліотеку pandas.

	https://gist.githubusercontent.com/tiangechen/b68782efa49a16edaf07dc2cdaa855ea/raw/0c794a9717f18b094eabab2cd6a6b9a226903577/movies.csv

	Спочатку перевіряється наявність файлу 'movies.csv' в поточному каталозі. Якщо файл вже існує, програма просто продовжує виконання. 
    У протилежному випадку відбувається завантаження файлу з вказаної URL-адреси.

	Перевіряється наявність файлу 'movies.csv' за допомогою функції os.path.exists().

	Якщо файл не існує, виконується HTTP-запит за допомогою бібліотеки requests для отримання вмісту документа за URL-адресою.

	Якщо статус відповіді є успішним, тобто

	requests.get(' URL-адреса').status_code == 200

(код 200), отриманий вміст записується у файл з розширенням csv.

	Завантажений файл зчитується у DataFrame за допомогою функції pandas.read_table().

	Після зчитування дублікати рядків видаляються з DataFrame за допомогою методу drop_duplicates().

	2 завдання. Виконуються такі кроки:

	Виводяться назви стовпців за допомогою атрибуту columns.

	Виводяться типи даних кожного стовпця за допомогою атрибуту dtypes.

	Інший підхід:

	Використовується метод info(), який надає загальну інформацію про DataFrame, таку як кількість ненульових значень у кожному стовпці та тип даних.

	Використовується метод describe(), який надає основні статистичні характеристики для числових стовпців у DataFrame, 
    такі як середнє значення, стандартне відхилення, мінімальне та максимальне значення, медіана тощо.

	3. Скільки всього фільмів у наборі даних?

	Існує щонайменше 5 способів:

1)   Використовується метод unique() для визначення унікальних значень у стовпці "Film", та обчислюється їхня кількість за допомогою len().

2)   Використовується функція len(), щоб порахувати загальну кількість рядків у DataFrame.

3)   Використовується метод count(), який підраховує кількість ненульових значень у стовпці "Film".

4)   Використовується метод value_counts(), який підраховує кількість кожного унікального значення у стовпці "Film".

5)   Використовується атрибут shape, щоб отримати кортеж, який містить кількість рядків і стовпців у DataFrame.

	4. Скільки фільмів є у наборі даних для кожного року?

	Існує щонайменше 5 способів:

1)   Використовується метод value_counts(), щоб підрахувати кількість фільмів для кожного унікального року у стовпці "Year".

2)   Використовується метод groupby() для групування рядків за значенням у стовпці "Year". 
Потім використовується метод agg() для обчислення кількості фільмів за кожний рік. Результат сортується за кількістю фільмів у зворотньому порядку.

3)   Застосовується метод groupby() для групування даних за роками, а потім застосовується метод count() для підрахунку кількості фільмів у кожній групі:

groupby('Year')['Film'].count()

Результат представляється у вигляді DataFrame.

4)   Застосовується метод groupby() для групування даних за роками, після чого обчислюється кількість фільмів у кожній групі: 

groupby('Year').count()

Результат представляється у вигляді DataFrame, де відображаються тільки стовпці "Year" і "Film" за допомогою функції loc:

loc[:, ['Year', 'Film']]

5)   Використовується цикл для перебору унікальних значень року зі стовпця "Year" і підрахунку кількості фільмів для кожного року. 
Кожний раз, коли відбувається ітерація, фільтрується DataFrame за значенням року, обчислюється його довжина (кількість рядків) і виводиться результат разом з відповідним роком.

 

5. Покажіть детальну інформацію про найменш та найбільш прибуткові фільми у наборі даних.

	Використаймо фільтрацію. Спочатку виводяться рядки, де значення стовпця "Profitability" дорівнює максимальному значенню у цьому стовпці, 
    щоб показати найбільш прибутковий фільм. Потім виводяться рядки, де значення стовпця "Profitability" дорівнює мінімальному значенню у цьому стовпці, 
    щоб показати найменш прибутковий фільм. 

	Інший синтаксис: Значення максимального та мінімального прибутку можна також знайти, використовуючи метод loc з умовою isin().

 

	6. Значення "Жанр" іноді здається непослідовним; спробуйте знайти  ці невідповідностей та виправити їх.

	У цьому рішенні використовується метод replace() для заміни неправильних значень у стовпці "Genre" на правильні.

	Спочатку виводиться унікальний список жанрів у наборі даних для виявлення непослідовностей.

	Потім використовується метод replace() для заміни неправильних значень у стовпці "Genre" на правильні значення.

	Після цього знову виводиться унікальний список жанрів, щоб перевірити, чи були вони правильно виправлені.

	7. Збережіть (у новий файл CSV) 10 найкращих комедій за кількістю глядачів;  покажіть лише назву фільму, рік та студію.

	Використовується наступний підхід:

	Відбираються всі комедії за допомогою фільтрування за жанром.

	Відбираються перші 10 комедій за оцінкою глядачів у порядку спадання.

	Обираються лише потрібні стовпці: назва фільму, рік та студія.

	Зберігається результат у новому CSV файлі.

	Інший синтаксис: Результати можна також знайти, використовуючи метод loc з умовою isin().
    '''