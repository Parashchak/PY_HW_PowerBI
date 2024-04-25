'''
Домашнє завдання 5

Для завантаження: https://drive.google.com/uc?id=1IOPTVq2ooQfZRkF3rAjGkTjRtbotG7FF


Спочатку напишіть код для читання та аналізу даних замовлення - поділ замовлень по рядках та продуктів по «@@@». 
Якщо завантажуємо файл у ручному форматі (зберегти файл через завантаження, то робимо ось так, головне щоб файл був в одній директорії з кодом)


Для того, щоб завантажити файл в автоматичному режимі ознайомтесь з пакетом requests

Потім напишіть код для розрахунку підтримки та впевненості для кожної пари продуктів.

1 - Список усіх продуктів

2 - Словник з кількістю кожного продукту

3 - Словник підрахунку кожної пари продуктів.

4. Словник підрахунку пар містить підтримку кожної пари елементів.

5. Використовуйте два словники, щоб розрахувати впевненість для кожної пари елементів.



* Зверніть увагу, що підтримка симетрична, а впевненість – ні. Наприклад, якщо є 100 замовлень з "bananas", 
200 замовлень з «peanut butter» та 30 замовлень з обома, тоді впевненість bananas => peanut butter становить 30%, 
тоді як впевненість peanut butter => bananas - 15%.

** Пам'ятайте, що не можна розраховувати впевненість продукту в (вона завжди буде 100%, але це не цікаво).


Зрештою, враховуючи мінімальні вимоги до впевненості та підтримці, переберіть усі пари продуктів та надрукуйте пари, 
що відповідають критеріям, у такому форматі:

p1 Cranberry Pomegranate Sparkling Yerba Mate => Organic Grapefruit Ginger Sparkling Yerba Mate (60.00% confidence), 15 support

p2 Antioxidant Infusions Ipanema Pomegranate Beverage => Antioxidant Infusions Brasilia Blueberry (45.45% confidence), 15 support



Рекомендації по виконанню: 


У п’ятому завданні мова йде про алгоритм асоціативних правил, який використовується для аналізу даних і виявлення кореляцій між різними продуктами або подіями. 
Ось пояснення основних термінів:

Підтримка (support): У контексті асоціативних правил support визначає частоту, з якою певна комбінація продуктів (або подій) з'являється у даних. 
Визначається в абсолютних значеннях.

Мінімальна підтримка (min_support) — це мінімальне значення support, яке необхідно для того, щоб вважати правило значущим. 
Якщо support комбінації продуктів нижче min_support, то вона не буде виведена як результат аналізу асоціаційних правил. 

Я рекомендую для min_support встановити значення 15, що означає, що друкуватимуться лише правила з рівнем підтримки 15 або більше випадків.

Впевненість (confidence) - це міра того, як часто правило виявляється істинним.

В контексті асоціативних правил confidence означає ймовірність, з якою товар B купується після того, як був куплений товар A.

Вона обчислюється як відношення кількості транзакцій, які містять товар А і товар В, до кількості транзакцій, які містять товар А. Визначається у відсотках.

Мінімальна впевненість (min_confidence) - це мінімальне значення впевненості, яке потрібно, щоб вважати асоціативне правило значущим. 
Якщо confidence правила менше min_confidence, то воно не буде виведено як результат аналізу асоціативних правил.

Я рекомендую для min_confidence встановити значення 45, що означає, що друкуватимуться лише правила з рівнем вневненості 45% або вище.

Ви фільтруєте правила асоціації, виводячи тільки ті, які задовольняють мінімальні впевненість та підтримку (які Ви самі задаєте).


П’яте завдання вирішується поетапно:

1) Читання та обробка даних:

 - відкрити для читання файл 'orders.txt';

- читати вміст файлу та розділяти його на рядки на основі подвійних символів нового рядка (\n\n).

- перебрати рядки, видаляючи пробіли на початку та в кінці. Якщо рядок не порожній, розбити його на список, використовуючи «@@@» як роздільник, 
і додати його до списку замовлень.

2) Ініціалізація словників-лічильників:

   словник для зберігання кількості кожного продукту

   словник для зберігання кількості пар продуктів

3) Підрахунок випадків продуктів:

- перебрати кожне замовлення в списку замовлень та кожен елемент у замовленні;

- якщо елемент уже є продуктом у словнику для зберігання продуктів, збільшити кількість продукту; інакше дорівнює 1.

4) Підрахунок пар продуктів:

- перебирати кожне замовлення в списку замовлень;

- перебирати кожен порядок і для кожної пари різних елементів у порядку створити кортеж і сортувати його.

- якщо пара вже є у словнику для зберігання пар, збільшити кількість пари; інакше дорівнює 1.

У цьому пункті ви формуєте пари продуктів, які входять до одного замовлення. Наприклад, 
якщо в замовленні є продукти A, B, C, то ви утворите такі пари: (A, B), (A, C), (B, C). Кожну пару ви представляєте у вигляді кортежу та сортуєте його,
 щоб забезпечити унікальність. Далі ви обчислюєте кількість кожної пари, яка зустрічається у всіх замовленнях.

Ви фільтруєте правила асоціації, виводячи тільки ті, які задовольняють мінімальні впевненість та підтримку (які Ви самі задаєте).

5) Пошук правил асоціації:

- перебрати кожну унікальну пару продуктів і їх кількість;

- обчислити достовірність правила асоціації для обох напрямків (x => y і y => x);

- перевірити, чи впевненість і підтримка відповідають заданим мінімальним значенням;

- друк правил асоціації, які задовольняють умовам.

У цьому пункті ви перебираєте усі унікальні пари продуктів і обчислюєте впевненість та підтримку для обох напрямків (x => y і y => x).

Можливі покращення:

- декомпозиція функцій: розбийте код на менші, більш модульні функції. Це робить код більш читабельним і його простіше підтримувати.

   Наприклад:

1) Перша функція приймає шлях до файлу як вхідні дані та читає вміст файлу.

  Потім вона розбиває вміст на список порядків, використовуючи подвійний символ нового рядка ("\n\n") як роздільник.

  Для кожного замовлення вона додатково розбиває замовлення на список продуктів, використовуючи «@@@» як роздільник.

  Функція повертає список замовлень, де кожне замовлення представлено як список продуктів.

2) Друга функція приймає список замовлень як вхідні дані.

  Вона повторює кожне замовлення та кожен продукт у замовленні.

  Вона підраховує випадки появи кожного продукту та зберігає кількість у словнику.

  Функція повертає словник, де ключами є продукти, а значеннями є кількість кожного продукту.

3) Третя функція відображає підтримку між двома продуктами у списку замовлень.

  Вона підраховує кількість замовлень, де присутні обидва продукти.

  Результат ділиться на загальну кількість замовлень для розрахунку підтримки, яка є співвідношенням замовлень, що містять обидва продукти.

4) Четверта функція приймає список замовлень, мінімальну впевненість і мінімальну підтримку як вхідні дані.

  Вона обчислює кількість окремих продуктів за допомогою другої функції.

  Потім вона повторює кожне замовлення та підраховує випадки появи пар продуктів.

  Для кожної пари вона розраховує впевненість в обох напрямках і підтримку.

  Якщо впевненість і підтримка відповідають мінімальним критеріям, вона друкує правила асоціації.

5) Після створення чотирьох функцій прочитати замовлення з файлу "orders.txt", встановити мінімальні значення впевненості та підтримки, 
викликати останню функцію для пошуку та друку правил асоціації на основі вказаних критеріїв.

 

- замість того, щоб вручну перевіряти, чи є елемент у словнику (якщо елемент у prod_count), 
ви можете використовувати defaultdict Python, щоб спростити код - from collections import defaultdict;

- замість того, щоб вручну оновлювати кількість для кожного продукту та кожної пари продуктів, 
можна використати клас лічильника з модуля колекцій, щоб спростити підрахунок входжень продуктів і пар - from collections import Counter;

- можна використати комбінації для спрощення генерації пар - from itertools import combinations;

- можна використати ланцюжок для підрахунку продуктів: використайте функцію ланцюжка chain з модуля itertools, 
щоб звести список замовлень в єдиний ітерований елемент. Це замінює розуміння вкладеного списку, роблячи код більш компактним - from itertools import chain;

- можна додати логіку завантаження файлу:

def download_document(file_name, document_url):

   if os.path.exists(file_name):

       pass

   else:

       response = requests.get(document_url)

       if response.status_code == 200:

           with open(file_name, 'wb') as f:

               f.write(response.content)

       else:

           print(f'Failed to download the document. Status code: {response.status_code}')

 

file_name = 'orders.txt'

document_url = 'https://drive.google.com/uc?id=1IOPTVq2ooQfZRkF3rAjGkTjRtbotG7FF'

download_document(file_name, document_url)

Цей код виконує:

- перевірку наявності файлу:

if os.path.exists(file_name):

   pass

Він використовує функцію os.path.exists, щоб перевірити, чи вже існує файл із вказаною назвою (file_name).

Якщо файл існує, код нічого не робить (передає).

- завантаження документа:

else:

   response = requests.get(document_url)

   if response.status_code == 200:

       with open(file_name, 'wb') as f:

           f.write(response.content)

   else:

       print(f'Failed to download the document. Status code: {response.status_code}')

Якщо файл не існує, код продовжує завантаження документа з указаної URL-адреси (document_url).

Він використовує функцію requests.get, щоб зробити запит HTTP GET до URL-адреси та зберігає відповідь у змінній відповіді.

Він перевіряє, чи код статусу відповіді дорівнює 200, що вказує на успішний запит.

Якщо запит виконано успішно, він відкриває файл, визначений file_name, у двійковому режимі запису ('wb') і записує вміст відповіді у файл.

Якщо запит завершується невдало або код статусу не дорівнює 200, друкується повідомлення про помилку, включаючи код статусу.

- приклад використання:

file_name = 'orders.txt'

document_url = 'https://drive.google.com/uc?id=1IOPTVq2ooQfZRkF3rAjGkTjRtbotG7FF'

download_document(file_name, document_url)

У прикладі показано, як використовувати функцію download_document, вказавши назву файлу та URL-адресу документа, який потрібно завантажити.

Підсумовуючи, логіка завантаження файлу перевіряє, чи існує файл, і, 
якщо ні, завантажує документ із зазначеної URL-адреси та зберігає його під вказаним ім’ям файлу. Він обробляє випадок, коли файл уже існує, 
і запобігає непотрібним завантаженням. Якщо завантаження невдале, воно надає відгук про помилку, включаючи код стану HTTP.
'''