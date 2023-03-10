'''Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
Пример:
- 6782 -> 23
- 0,56 -> 11'''

number = input('Введите число > ')  # Приглашение ко вводу числа number

# Если число с дробной частью, и написано через , - то убираем знак , из строки stroka1
stroka1 = number.replace('.', '')
# Если число с дробной частью, и написано через . - то убираем знак . из строки stroka2
stroka2 = stroka1.replace(',', '')

chislo = int(stroka2)  # Преобразуем строку в число (тип - integer)

summa_znak = 0
while chislo > 0:  # Цикл по нахождению суммы цифр в числе
    summa_znak += chislo % 10
    chislo //= 10
print('Сумма цифр в числе', number, 'равна', summa_znak)
