import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import warnings
Lesson 8. Pandas
Date: 2024-04-09
Topics:

Series
Dataframe
Aggregation function
Drop missing value
Slice - loc/iloc
Materials:

Pandas
Pandas w3
Stat of using Pandas
Markdown
Pandas - liblary for:
Data Manipulation - work with Series - DataFrame
Data Visualization
Pandas - Numpy + Matplotlib


warnings.simplefilter(action='ignore', category=FutureWarning)
%matplotlib inline
sns.get_dataset_names()
df = sns.load_dataset('iris')  # transform csv to dataframe
df.head()  # показати n - перших записів, n - default 5
sepal_length	sepal_width	petal_length	petal_width	species
0	5.1	3.5	1.4	0.2	setosa
1	4.9	3.0	1.4	0.2	setosa
2	4.7	3.2	1.3	0.2	setosa
3	4.6	3.1	1.5	0.2	setosa
4	5.0	3.6	1.4	0.2	setosa
df.shape
(150, 5)
df.head(n=10)
sepal_length	sepal_width	petal_length	petal_width	species
0	5.1	3.5	1.4	0.2	setosa
1	4.9	3.0	1.4	0.2	setosa
2	4.7	3.2	1.3	0.2	setosa
3	4.6	3.1	1.5	0.2	setosa
4	5.0	3.6	1.4	0.2	setosa
5	5.4	3.9	1.7	0.4	setosa
6	4.6	3.4	1.4	0.3	setosa
7	5.0	3.4	1.5	0.2	setosa
8	4.4	2.9	1.4	0.2	setosa
9	4.9	3.1	1.5	0.1	setosa
df.head(n=10)  # показати 10 первих записів
sepal_length	sepal_width	petal_length	petal_width	species
0	5.1	3.5	1.4	0.2	setosa
1	4.9	3.0	1.4	0.2	setosa
2	4.7	3.2	1.3	0.2	setosa
3	4.6	3.1	1.5	0.2	setosa
4	5.0	3.6	1.4	0.2	setosa
5	5.4	3.9	1.7	0.4	setosa
6	4.6	3.4	1.4	0.3	setosa
7	5.0	3.4	1.5	0.2	setosa
8	4.4	2.9	1.4	0.2	setosa
9	4.9	3.1	1.5	0.1	setosa
df.columns  # display all columns in df
Index(['sepal_length', 'sepal_width', 'petal_length', 'petal_width',
       'species'],
      dtype='object')
df.index  # range index for df
RangeIndex(start=0, stop=150, step=1)
df.shape  # отримати tuple - div
df.tail()  # останні n - записів, n - default 5
sepal_length	sepal_width	petal_length	petal_width	species
145	6.7	3.0	5.2	2.3	virginica
146	6.3	2.5	5.0	1.9	virginica
147	6.5	3.0	5.2	2.0	virginica
148	6.2	3.4	5.4	2.3	virginica
149	5.9	3.0	5.1	1.8	virginica
df.tail(n=10)
sepal_length	sepal_width	petal_length	petal_width	species
140	6.7	3.1	5.6	2.4	virginica
141	6.9	3.1	5.1	2.3	virginica
142	5.8	2.7	5.1	1.9	virginica
143	6.8	3.2	5.9	2.3	virginica
144	6.7	3.3	5.7	2.5	virginica
145	6.7	3.0	5.2	2.3	virginica
146	6.3	2.5	5.0	1.9	virginica
147	6.5	3.0	5.2	2.0	virginica
148	6.2	3.4	5.4	2.3	virginica
149	5.9	3.0	5.1	1.8	virginica
df.sample()  # check random value, n - default 1
sepal_length	sepal_width	petal_length	petal_width	species
5	5.4	3.9	1.7	0.4	setosa
df.sample(n=5)
sepal_length	sepal_width	petal_length	petal_width	species
111	6.4	2.7	5.3	1.9	virginica
55	5.7	2.8	4.5	1.3	versicolor
16	5.4	3.9	1.3	0.4	setosa
28	5.2	3.4	1.4	0.2	setosa
103	6.3	2.9	5.6	1.8	virginica
df.info()  # short info about df
<class 'pandas.core.frame.DataFrame' >
RangeIndex: 150 entries, 0 to 149
Data columns(total 5 columns):
 #   Column        Non-Null Count  Dtype
--- ------ -------------- -----
0   sepal_length  150 non-null    float64
1   sepal_width   150 non-null    float64
2   petal_length  150 non-null    float64
3   petal_width   150 non-null    float64
4   species       150 non-null    object
dtypes: float64(4), object(1)
memory usage: 6.0 + KB
df.select_dtypes(include=['float64'])  # обрати потрібні типи данних
sepal_length	sepal_width	petal_length	petal_width
0	5.1	3.5	1.4	0.2
1	4.9	3.0	1.4	0.2
2	4.7	3.2	1.3	0.2
3	4.6	3.1	1.5	0.2
4	5.0	3.6	1.4	0.2
...	...	...	...	...
145	6.7	3.0	5.2	2.3
146	6.3	2.5	5.0	1.9
147	6.5	3.0	5.2	2.0
148	6.2	3.4	5.4	2.3
149	5.9	3.0	5.1	1.8
150 rows × 4 columns

df.describe()  # basic statis df
sepal_length	sepal_width	petal_length	petal_width
count	150.000000	150.000000	150.000000	150.000000
mean	5.843333	3.057333	3.758000	1.199333
std	0.828066	0.435866	1.765298	0.762238
min	4.300000	2.000000	1.000000	0.100000
25 % 5.100000 2.800000 1.600000 0.300000
50 % 5.800000 3.000000 4.350000 1.300000
75 % 6.400000 3.300000 5.100000 1.800000
max	7.900000	4.400000	6.900000	2.500000
df.isnull()  # функія для підрахунки  Null/None значеннь
sepal_length	sepal_width	petal_length	petal_width	species
0	False	False	False	False	False
1	False	False	False	False	False
2	False	False	False	False	False
3	False	False	False	False	False
4	False	False	False	False	False
...	...	...	...	...	...
145	False	False	False	False	False
146	False	False	False	False	False
147	False	False	False	False	False
148	False	False	False	False	False
149	False	False	False	False	False
150 rows × 5 columns

df.isnull().sum()  # підрахувати кількість відсутніх value
sepal_length    0
sepal_width     0
petal_length    0
petal_width     0
species         0
dtype: int64
df['species']
0         setosa
1         setosa
2         setosa
3         setosa
4         setosa
...
145    virginica
146    virginica
147    virginica
148    virginica
149    virginica
Name: species, Length: 150, dtype: object
df.species
0         setosa
1         setosa
2         setosa
3         setosa
4         setosa
...
145    virginica
146    virginica
147    virginica
148    virginica
149    virginica
Name: species, Length: 150, dtype: object
df['species'].values  # показати по колонці значення
array(['setosa', 'setosa', 'setosa', 'setosa', 'setosa', 'setosa',
       'setosa', 'setosa', 'setosa', 'setosa', 'setosa', 'setosa',
       'setosa', 'setosa', 'setosa', 'setosa', 'setosa', 'setosa',
       'setosa', 'setosa', 'setosa', 'setosa', 'setosa', 'setosa',
       'setosa', 'setosa', 'setosa', 'setosa', 'setosa', 'setosa',
       'setosa', 'setosa', 'setosa', 'setosa', 'setosa', 'setosa',
       'setosa', 'setosa', 'setosa', 'setosa', 'setosa', 'setosa',
       'setosa', 'setosa', 'setosa', 'setosa', 'setosa', 'setosa',
       'setosa', 'setosa', 'versicolor', 'versicolor', 'versicolor',
       'versicolor', 'versicolor', 'versicolor', 'versicolor',
       'versicolor', 'versicolor', 'versicolor', 'versicolor',
       'versicolor', 'versicolor', 'versicolor', 'versicolor',
       'versicolor', 'versicolor', 'versicolor', 'versicolor',
       'versicolor', 'versicolor', 'versicolor', 'versicolor',
       'versicolor', 'versicolor', 'versicolor', 'versicolor',
       'versicolor', 'versicolor', 'versicolor', 'versicolor',
       'versicolor', 'versicolor', 'versicolor', 'versicolor',
       'versicolor', 'versicolor', 'versicolor', 'versicolor',
       'versicolor', 'versicolor', 'versicolor', 'versicolor',
       'versicolor', 'versicolor', 'versicolor', 'versicolor',
       'versicolor', 'versicolor', 'versicolor', 'virginica', 'virginica',
       'virginica', 'virginica', 'virginica', 'virginica', 'virginica',
       'virginica', 'virginica', 'virginica', 'virginica', 'virginica',
       'virginica', 'virginica', 'virginica', 'virginica', 'virginica',
       'virginica', 'virginica', 'virginica', 'virginica', 'virginica',
       'virginica', 'virginica', 'virginica', 'virginica', 'virginica',
       'virginica', 'virginica', 'virginica', 'virginica', 'virginica',
       'virginica', 'virginica', 'virginica', 'virginica', 'virginica',
       'virginica', 'virginica', 'virginica', 'virginica', 'virginica',
       'virginica', 'virginica', 'virginica', 'virginica', 'virginica',
       'virginica', 'virginica', 'virginica'], dtype=object)
df['species'].value_counts()  # select column, count() .... group by <column>
species
setosa        50
versicolor    50
virginica     50
Name: count, dtype: int64
df['species'].value_counts(normalize=True)  # порахувати кількість данних
species
setosa        0.333333
versicolor    0.333333
virginica     0.333333
Name: proportion, dtype: float64
df['species'].hist()

sns.displot(df['species'])
plt.show()

species = df['species'].value_counts()
print(species)
plt.hist(df['species'], bins=7, color='red')

plt.title('Розподіл для species')
plt.xlabel('species')
plt.ylabel('Частота')
plt.show()
df['species'].value_counts()
plt.pie?
setosa = df['species'].value_counts()[0]
versicolor = df['species'].value_counts()[1]
virginica = df['species'].value_counts()[2]
plt.pie([setosa, versicolor, virginica], labels=['S', 'Vers', 'Virn'],
        colors=['blue', 'yellow', 'purple'], normalize=True)
plt.show()
df.head()
df['species'].unique()  # показати унікальні значення
df['species'].nunique()
df.columns
plt.plot('species', 'sepal_length', data=df)
plt.grid()
plt.show()
# Boolesn masks, same as NumPy masks
mask = df['sepal_length'] > 5.0
df[mask]
sepal_length	sepal_width	petal_length	petal_width	species
0	5.1	3.5	1.4	0.2	setosa
5	5.4	3.9	1.7	0.4	setosa
10	5.4	3.7	1.5	0.2	setosa
14	5.8	4.0	1.2	0.2	setosa
15	5.7	4.4	1.5	0.4	setosa
...	...	...	...	...	...
145	6.7	3.0	5.2	2.3	virginica
146	6.3	2.5	5.0	1.9	virginica
147	6.5	3.0	5.2	2.0	virginica
148	6.2	3.4	5.4	2.3	virginica
149	5.9	3.0	5.1	1.8	virginica
118 rows × 5 columns

df[df['sepal_length'] > 5.0]
sepal_length	sepal_width	petal_length	petal_width	species
0	5.1	3.5	1.4	0.2	setosa
5	5.4	3.9	1.7	0.4	setosa
10	5.4	3.7	1.5	0.2	setosa
14	5.8	4.0	1.2	0.2	setosa
15	5.7	4.4	1.5	0.4	setosa
...	...	...	...	...	...
145	6.7	3.0	5.2	2.3	virginica
146	6.3	2.5	5.0	1.9	virginica
147	6.5	3.0	5.2	2.0	virginica
148	6.2	3.4	5.4	2.3	virginica
149	5.9	3.0	5.1	1.8	virginica
118 rows × 5 columns

df[df['sepal_length'] == 5.4]
df[(df['sepal_length'] >= 3.15) & (df['petal_length'] <= 4.5)]  # & | ~
sepal_length	sepal_width	petal_length	petal_width	species
0	5.1	3.5	1.4	0.2	setosa
1	4.9	3.0	1.4	0.2	setosa
2	4.7	3.2	1.3	0.2	setosa
3	4.6	3.1	1.5	0.2	setosa
4	5.0	3.6	1.4	0.2	setosa
...	...	...	...	...	...
96	5.7	2.9	4.2	1.3	versicolor
97	6.2	2.9	4.3	1.3	versicolor
98	5.1	2.5	3.0	1.1	versicolor
99	5.7	2.8	4.1	1.3	versicolor
106	4.9	2.5	4.5	1.7	virginica
87 rows × 5 columns

df[df['species'].ne('virginica')]  # виключити данні
sepal_length	sepal_width	petal_length	petal_width	species
0	5.1	3.5	1.4	0.2	setosa
1	4.9	3.0	1.4	0.2	setosa
2	4.7	3.2	1.3	0.2	setosa
3	4.6	3.1	1.5	0.2	setosa
4	5.0	3.6	1.4	0.2	setosa
...	...	...	...	...	...
95	5.7	3.0	4.2	1.2	versicolor
96	5.7	2.9	4.2	1.3	versicolor
97	6.2	2.9	4.3	1.3	versicolor
98	5.1	2.5	3.0	1.1	versicolor
99	5.7	2.8	4.1	1.3	versicolor
100 rows × 5 columns

# Sort_values - відсортувати значення
df.sort_values('sepal_length', ascending=False)  # сортування по одній колонці
sepal_length	sepal_width	petal_length	petal_width	species
131	7.9	3.8	6.4	2.0	virginica
135	7.7	3.0	6.1	2.3	virginica
122	7.7	2.8	6.7	2.0	virginica
117	7.7	3.8	6.7	2.2	virginica
118	7.7	2.6	6.9	2.3	virginica
...	...	...	...	...	...
41	4.5	2.3	1.3	0.3	setosa
42	4.4	3.2	1.3	0.2	setosa
38	4.4	3.0	1.3	0.2	setosa
8	4.4	2.9	1.4	0.2	setosa
13	4.3	3.0	1.1	0.1	setosa
150 rows × 5 columns

# можна сортувати по n - колонках, потрібно передати у вигляді списку
df.sort_values(['sepal_length', 'sepal_width'], ascending=[True, False])
sepal_length	sepal_width	petal_length	petal_width	species
13	4.3	3.0	1.1	0.1	setosa
42	4.4	3.2	1.3	0.2	setosa
38	4.4	3.0	1.3	0.2	setosa
8	4.4	2.9	1.4	0.2	setosa
41	4.5	2.3	1.3	0.3	setosa
...	...	...	...	...	...
117	7.7	3.8	6.7	2.2	virginica
135	7.7	3.0	6.1	2.3	virginica
122	7.7	2.8	6.7	2.0	virginica
118	7.7	2.6	6.9	2.3	virginica
131	7.9	3.8	6.4	2.0	virginica
150 rows × 5 columns

df[df['species'].isin(['setosa', 'virginica'])]  # перевіряємо значення
sepal_length	sepal_width	petal_length	petal_width	species
0	5.1	3.5	1.4	0.2	setosa
1	4.9	3.0	1.4	0.2	setosa
2	4.7	3.2	1.3	0.2	setosa
3	4.6	3.1	1.5	0.2	setosa
4	5.0	3.6	1.4	0.2	setosa
...	...	...	...	...	...
145	6.7	3.0	5.2	2.3	virginica
146	6.3	2.5	5.0	1.9	virginica
147	6.5	3.0	5.2	2.0	virginica
148	6.2	3.4	5.4	2.3	virginica
149	5.9	3.0	5.1	1.8	virginica
100 rows × 5 columns

# Summaty Stati
df.head()
sepal_length	sepal_width	petal_length	petal_width	species
0	5.1	3.5	1.4	0.2	setosa
1	4.9	3.0	1.4	0.2	setosa
2	4.7	3.2	1.3	0.2	setosa
3	4.6	3.1	1.5	0.2	setosa
4	5.0	3.6	1.4	0.2	setosa
df['sepal_length'].max(), df['sepal_length'].min()
(7.9, 4.3)
df[df['species'] == 'virginica'].max(), df[df['species'] == 'setosa'].min()
(sepal_length          7.9
 sepal_width           3.8
 petal_length          6.9
 petal_width           2.5
 species         virginica
 dtype: object,
 sepal_length       4.3
 sepal_width        2.3
 petal_length       1.0
 petal_width        0.1
 species         setosa
 dtype: object)
df[df['species'] == 'virginica'].sort_values('sepal_length', ascending=True)
sepal_length	sepal_width	petal_length	petal_width	species
106	4.9	2.5	4.5	1.7	virginica
121	5.6	2.8	4.9	2.0	virginica
113	5.7	2.5	5.0	2.0	virginica
101	5.8	2.7	5.1	1.9	virginica
114	5.8	2.8	5.1	2.4	virginica
142	5.8	2.7	5.1	1.9	virginica
149	5.9	3.0	5.1	1.8	virginica
119	6.0	2.2	5.0	1.5	virginica
138	6.0	3.0	4.8	1.8	virginica
127	6.1	3.0	4.9	1.8	virginica
134	6.1	2.6	5.6	1.4	virginica
126	6.2	2.8	4.8	1.8	virginica
148	6.2	3.4	5.4	2.3	virginica
136	6.3	3.4	5.6	2.4	virginica
123	6.3	2.7	4.9	1.8	virginica
146	6.3	2.5	5.0	1.9	virginica
133	6.3	2.8	5.1	1.5	virginica
100	6.3	3.3	6.0	2.5	virginica
103	6.3	2.9	5.6	1.8	virginica
115	6.4	3.2	5.3	2.3	virginica
111	6.4	2.7	5.3	1.9	virginica
128	6.4	2.8	5.6	2.1	virginica
137	6.4	3.1	5.5	1.8	virginica
132	6.4	2.8	5.6	2.2	virginica
116	6.5	3.0	5.5	1.8	virginica
147	6.5	3.0	5.2	2.0	virginica
110	6.5	3.2	5.1	2.0	virginica
104	6.5	3.0	5.8	2.2	virginica
108	6.7	2.5	5.8	1.8	virginica
145	6.7	3.0	5.2	2.3	virginica
144	6.7	3.3	5.7	2.5	virginica
140	6.7	3.1	5.6	2.4	virginica
124	6.7	3.3	5.7	2.1	virginica
143	6.8	3.2	5.9	2.3	virginica
112	6.8	3.0	5.5	2.1	virginica
141	6.9	3.1	5.1	2.3	virginica
120	6.9	3.2	5.7	2.3	virginica
139	6.9	3.1	5.4	2.1	virginica
102	7.1	3.0	5.9	2.1	virginica
129	7.2	3.0	5.8	1.6	virginica
109	7.2	3.6	6.1	2.5	virginica
125	7.2	3.2	6.0	1.8	virginica
107	7.3	2.9	6.3	1.8	virginica
130	7.4	2.8	6.1	1.9	virginica
105	7.6	3.0	6.6	2.1	virginica
117	7.7	3.8	6.7	2.2	virginica
135	7.7	3.0	6.1	2.3	virginica
122	7.7	2.8	6.7	2.0	virginica
118	7.7	2.6	6.9	2.3	virginica
131	7.9	3.8	6.4	2.0	virginica
df['sepal_length'].agg([np.max, np.min, np.median, np.mean])
max       7.900000
min       4.300000
median    5.800000
mean      5.843333
Name: sepal_length, dtype: float64
df.agg({'sepal_length': 'max', 'sepal_width': [np.mean, 'median']})
sepal_length	sepal_width
max	7.9	NaN
mean	NaN	3.057333
median	NaN	3.000000
year_df = df.groupby('species')['sepal_length'].mean()
print(year_df)
species
setosa        5.006
versicolor    5.936
virginica     6.588
Name: sepal_length, dtype: float64
mean = df_tips.groupby("sex")["tips"].mean()
print(mean)
# Tasks
df_tips = sns.load_dataset('tips')
df_tips.head()
total_bill	tip	sex	smoker	day	time	size
0	16.99	1.01	Female	No	Sun	Dinner	2
1	10.34	1.66	Male	No	Sun	Dinner	3
2	21.01	3.50	Male	No	Sun	Dinner	3
3	23.68	3.31	Male	No	Sun	Dinner	2
4	24.59	3.61	Female	No	Sun	Dinner	4
df_tips.tail()
df_tips.sample(5)
df_tips.shape
df_tips.dtypes
df_tips.describe()
df_tips.info()
df_tips.isnull().sum()
df_tips.isna().sum()
# Task 1 - Який середній розмір чайових залежно від статі клієнта?
df_tips.groupby('sex')[['total_bill', 'tip']].mean()
total_bill	tip
sex
Male	20.744076	3.089618
Female	18.056897	2.833448
# Task 2 - Яка загальна сума рахунку залежно від дня тижня та часу доби?
df_tips.groupby(['day', 'time'])['total_bill'].sum().reset_index()
day	time	total_bill
0	Thur	Lunch	1077.55
1	Thur	Dinner	18.78
2	Fri	Lunch	89.92
3	Fri	Dinner	235.96
4	Sat	Lunch	0.00
5	Sat	Dinner	1778.40
6	Sun	Lunch	0.00
7	Sun	Dinner	1627.16
weekend = df_tips[(df_tips['day'] == 'Sat') | (df_tips['day'] == 'Sun')]
weekend['time'].value_counts()
# Task 3 - Яка залежність між розміром рахунку та курінням?
df_tips.groupby('smoker')['total_bill'].mean()
smoker
Yes    20.756344
No     19.188278
Name: total_bill, dtype: float64
df_tips.shape
# Task 4 - Яка залежність між розміром чайових та курінням?
df_tips.groupby('smoker')['tip'].mean()
smoker
Yes    3.008710
No     2.991854
Name: tip, dtype: float64
# Create new column
df_tips['binary_gender'] = df_tips['sex'].apply(
    lambda x: 0 if x == 'Male' else 1)
df_tips.head()

Header1
Header1
Header2
Header3
Header4
Header5
text
Some text some text, some text

Dataframe use in Python

One sent
Two sent

In sent  Python tu
