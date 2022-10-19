#Функция проверки является ли переменные числами
def check(x, y): #Принимает x, y- любое значение 
    if (type(x) == int or type(x) == float) and (type(y) == int or type(y) == float): #Если x и y- являются числами
        return True #Возвращает True
    else:
        return False #Возвращает False

#Функция сложения
def summa(a,b): #Принимает a, b- любое значение 
    if check(a,b): #Проверка a и b на то, являются ли они числами
        return a + b #Сумма a и b
    else:
        if type(a) == str:
            if 'error' in a.lower():
                return a
            else:
                return ('ERROR_201: Введено не число') #Если не прошло проверку- возвращает строку
        if type(b) == str:
            if 'error' in b.lower():
                return b
            else:
                return ('ERROR_201: Введено не число') #Если не прошло проверку- возвращает строку
        else:
            return ('ERROR_201: Введено не число') #Если не прошло проверку- возвращает строку

#Функция вычитания
def vich(a,b): #Принимает a, b- любое значение 
    if check(a,b): #Проверка a и b на то, являются ли они числами
        return a - b #Разность a и b
    else:
        if type(a) == str:
            if 'error' in a.lower():
                return a
            else:
                return ('ERROR_201: Введено не число') #Если не прошло проверку- возвращает строку
        if type(b) == str:
            if 'error' in b.lower():
                return b
            else:
                return ('ERROR_201: Введено не число') #Если не прошло проверку- возвращает строку
        else:
            return ('ERROR_201: Введено не число') #Если не прошло проверку- возвращает строку


#Функция умножения
def umn(a,b): #Принимает a, b- любое значение 
    if check(a,b): #Проверка a и b на то, являются ли они числами
        return a * b #Умножение a и b
    else:
        if type(a) == str:
            if 'error' in a.lower():
                return a
            else:
                return ('ERROR_201: Введено не число') #Если не прошло проверку- возвращает строку
        if type(b) == str:
            if 'error' in b.lower():
                return b
            else:
                return ('ERROR_201: Введено не число') #Если не прошло проверку- возвращает строку
        else:
            return ('ERROR_201: Введено не число') #Если не прошло проверку- возвращает строку


#Функция деления
def chast(a,b): #Принимает a, b- любое значение 
    if check(a,b): #Проверка a и b на то, являются ли они числами
        if b == 0: #Проверяеи b (второе число) на ноль
            return('ERROR_202') #Если на b является нулем- возвращает строку
        else: #Если b не ноль, то: 
            return a / b #Деление a и b
    else:
        if type(a) == str:
            if 'error' in a.lower():
                return a
            else:
                return ('ERROR_201: Введено не число') #Если не прошло проверку- возвращает строку
        if type(b) == str:
            if 'error' in b.lower():
                return b
            else:
                return ('ERROR_201: Введено не число') #Если не прошло проверку- возвращает строку
        else:
            return ('ERROR_201: Введено не число') #Если не прошло проверку- возвращает строку