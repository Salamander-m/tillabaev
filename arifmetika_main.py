from project.g_palnaref import * # второй модуль с арифметикой и перевод из 2сс
def isnum(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
# блок арифметики
def summa(a,b):
    if isnum(a) and isnum(b): # если переменная - число
        return (arifmetika.summa(float(a),float(b))) # преобразовывает их во float и высчитывает значение функции
    else:
        return arifmetika.summa(a,b) # если не число - возвращает ошибку, которая указана в функции

def chast(a,b):
    if isnum(a) and isnum(b): # если переменная - число
        return (arifmetika.chast(float(a),float(b))) # преобразовывает их во float и высчитывает значение функции
    else:
        return arifmetika.chast(a,b) # если не число - возвращает ошибку, которая указана в функции

def umn(a,b):
    if isnum(a) and isnum(b): # если переменная - число
        return (arifmetika.umn(float(a),float(b))) # преобразовывает их во float и высчитывает значение функции
    else:
        return arifmetika.umn(a,b) # если не число - возвращает ошибку, которая указана в функции

def vich(a,b):
    if isnum(a) and isnum(b): # если переменная - число
        return (arifmetika.vich(float(a),float(b))) # преобразовывает их во float и высчитывает значение функции
    else:
        return arifmetika.vich(a,b) # если не число - возвращает ошибку, которая указана в функции