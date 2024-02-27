# ***************************** 27.02.2024 *****************************************
'''Змінна - це область пам'яті'''

'''Python style - "device_mobile" '''
'''Camel style - "deviceMobile" '''
'''Kebab style - "device-mobile" '''

# a = input("Enter your name: ")
# b = input("Enter your name: ")
# c = input("Enter your name: ")

# print(a, b, c, sep='\n', end='*') #sep, end
# print(a, b, c, end='*') #end

'''
прості типи даних (числа, строки)
композитні (collectio) типи даних (списки [1,2,3,4,5])
advens
struct
advan
protocol
'''

# Simple datas

# 1.  NUMBERS

'''integer - цілі числа'''
'''
decimal - розширення для float приблизно до 15 знаків після коми з можливістю вказати кількість знаків після коми # потребує встановлення (імпорт бібліотеки)
float - 7 знаків після коми
'''
# round() - використовується для округлення

# 3. Обчисліть, скільки секунд у добі
print(f"Second in day: {24*60*60}")
# 4. Обчисліть, скільки секунд у році
print(f"Second in year: {365*24*60*60}")

#5. Відкрито нову планету! Введіть назву планети
#і кількість земних днів в одному році на цій планеті (на приклад один рік на новій планеті – 532 земних дні) 
#Обчисліть і надрукуйте, скільки секунд становить рік планети.
#(«В одному році Zork 22118400 секунд»)
planet_name = input("Enter planet name: ")
day_new_planet = int(input("Enter planet day in year: "))
seconds_year = (24*60*60)*365
print("В одному році ", planet_name, day_new_planet * seconds_year, " секунд")
#6. Візьміть як ціле число вік людини в місяцях і виведіть «Істина», якщо особа старше 18 років, інакше «False».
years_monts = int(input("Enter month: "))
month_18years = 12 * 18
print(years_monts>=month_18years)
