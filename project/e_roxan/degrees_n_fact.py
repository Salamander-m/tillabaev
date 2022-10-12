#Функция проверки является ли переменные числами
def check_num(num): # принимает любое значение num
    num = str(num)
    k = 0
    for i in num:
        if i in '-.0123456789':
            k += 1
    if len(num) == k: # проверяет является ли num числом
        return True # возвращает True(bool)
    else: 
        return False # возращает False(bool)

#Степень
def stepen(num): # принимает любое значение num
    if check_num(num): # проверяет число, если функция возвращает True -
        st = (input('Введите степень: ')) # вводится степень
        if check_num(st): # проверяется, является ли степень числом
            return (float(num)**float(st)) # возвращает число в степени st
        else:
            return ('ERROR_101') # если нет, выдает строку
    else: 
        return ('ERROR_101') # если нет, выдает строку

#Корень
def koren(num): # принимает любое значение num
    if check_num(num): # проверяет число, если функция возвращает True -
        st = (input('Введите степень: ')) # вводится степень
        if check_num(st): # проверяется, является ли степень числом
            return (float(num)**(1/float(st))) # возвращает число в степени 1/st
        else:
            return ('ERROR_101') # если нет, выдает строку
    else: 
        return ('ERROR_101') # если нет, выдает строку
#Факториал
def fact(num): # принимает любое значение num
    if check_num(num): # проверяет является ли num числом и больше ли оно нуля
        num = int(num)
        if num >= 0:
            from math import factorial # импорт функции factorial из библотеки math
            return(factorial(int(num))) # возращает значение функции factorial(num)
    else:
        return ('ERROR_101') # если нет, выдает строку
    
