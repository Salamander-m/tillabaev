#Перевод из 16 сс в другие
def check_hex(num): # функции для проверки число в 16 системе или нет
    numbers = [] # объявление пустого списка
    num = str(num).upper() # перевод числа в строку
    for i in num: # проход по элементам строки
        if i in '0123456789ABCDEF': 
            numbers.append(i) # то добавляется в список numbers
    if len(numbers) == len(num): # если длина списка = длине изначального числа
        return True # возвращает True(bool)
    else: # если нет
        return False # возращает False(bool) 

def from_hex(n):
    if n == '':
        return ('ERROR_302') # n - пустое
    else:
        convert_system = (input('Введите желаемую в выводе систему счисления (2,8,10): ')) 
        if check_hex(n):
            if convert_system == '2':
                return hex_to_bi(n)
            if convert_system == '8':
                return hex_to_oct(n)
            if convert_system == '10': 
                return hex_to_dec(n)
            if convert_system == '16':
                return n
            if convert_system not in ['2','8','10','16']:
                return "ERROR_305: Перевод в такую систему не осущетвляетя" # не в нужных системах
        else:
            return "ERROR_304: Введено не число" # не число

def hex_to_bi(x): #перобразование числа 16-ую в 2-ую
    if check_hex(x):
        return(bin(int(str(x), 16))).replace('0b','') #возврат значения двоичного числа
    else:
        return 'ERROR_304: Введено не число'


def hex_to_dec(x): #перобразование числа 16-ую в 10-ую
    if check_hex(x):
        return(int(str(x), 16)) #возврат значения десятиричного числа
    else:
        return 'ERROR_304: Введено не число'


def hex_to_oct(x): #перобразование числа 16-ую в 8-ую
    if check_hex(x):
        return(oct(int(str(x), 16))).replace('0o','') #возврат значения восьмиричного числа
    else:
        return 'ERROR_304: Введено не число'
