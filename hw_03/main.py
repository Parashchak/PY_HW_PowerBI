'''
У класі професора Грубла щойно був іспит. Він почав перевіряти роботи, але
оцінював їх не дуже уважно.
Напишіть програму, яка
приймає як вхідні дані оцінку кожного учня і те, чи здав він
іспит.
Потім програмі необхідно надрукувати дві речі:
a. Чи був професор Грубл послідовним у проставленні позначки
"Passed" для студентів.
b. Якщо професор Грубл був послідовним, виведіть діапазон у
якому знаходиться поріг для складання іспиту.
Приклади:
Припустимо, ми отримуємо такі дані, як вхідні дані:

У цьому випадку професор, на жаль, непослідовний, тому що
Student 6 має позначку “Passed” з оцінкою 75, а Student 1 має позначку
"Failed" при вищій оцінці - 78.

Тепер припустимо, що ми отримали такі значення:

#3 2

В цьому випадку професор послідовний, а поріг складання іспиту
знаходиться в
діапазоні 73 – 78 балів.
'''

import random

# Отримання кількості студентів від користувача
def get_valid_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                raise ValueError("Введіть позитивне ціле число.")
            return value
        except ValueError as e:
            print(f"Помилка: {e}")
            continue

# Генерування балів та результатів студентів
def generate_student_scores(num_students):
    student_scores = []
    for _ in range(num_students):
        score = random.randint(60, 100)
        result = random.choice(["Failed", "Passed"])
        student_scores.append((score, result))
    return student_scores

# Виведення результатів студентів
def print_student_results(student_scores):
    print("Результати студентів:")
    for i, (score, result) in enumerate(student_scores, start=1):
        print(f"Студент {i}: Бал - {score}, Результат - {result}")

# Перевірка послідовності професора
def check_professor_consistency(student_scores):
    passing_scores = [score for score, result in student_scores if result == "Passed"]
    failing_scores = [score for score, result in student_scores if result == "Failed"]

    min_passing_score = min(passing_scores) if passing_scores else 100
    max_failing_score = max(failing_scores) if failing_scores else 50

    if min_passing_score <= max_failing_score:
        print("Професор Грубл не був послідовним у проставленні позначок 'Passed'.")
    else:
        print(f"Професор Грубл був послідовним.")
        print(f"Діапазон проходження іспиту: [{max_failing_score + 1}, {min_passing_score - 1}].")


num_students = get_valid_input("Введіть кількість студентів: ")

student_scores = generate_student_scores(num_students)

print_student_results(student_scores)

check_professor_consistency(student_scores)
