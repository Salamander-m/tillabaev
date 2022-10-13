from project.e_roxan.degrees_n_fact import * # первый модуль с факт, степ, корень, переовод из 8сс
from project.e_roxan.trans_8 import from_oct
from project.g_palnaref.trans_2 import from_bin
from project.r_joseph.trans_10 import from_dec
from project.l_jotaro.trans_16 import from_hex
from project.l_jotaro.trygonometria1 import *
from arifmetika_main import * # адаптированный из второго модуля (только арифметика), подходящая для главной программы
from commands import user_commands
from commands import user_help 
from style import color # импортирует класс color, атрибуты которого являются строками ANSI последовательности


# Объявления предущей переменной как "пустой", по которой сравнивается были ли предыдущие действия за сессию программы
previous_answer = None
eps = 6 # точность до шести знаков


# функции проверки строки, на всё ли элементы в ней цифры
def isnum(s): # конструкция try-except
    try: # пытается привести s к float
        float(s)
        return True # если получается - возвращает True
    except ValueError:
        return False # нет - False


def arifmetika_user_input(): # функция для ввода переменных
    num_first = (input(color.PURPLE + 'Введите первое значение: ' + color.END)) # вводится первое число str
    num_second = (input(color.PURPLE + 'Введите второе значение: ' + color.END)) # вводится второе число str
    return num_first,num_second # возвращает введенные значения в tuple


def user_output(func): # функция для вывода результата или ошибки
    result = func # переменная принимает значения функций
    global previous_answer # обращение глобальным данным переменных, которая описана выше
    previous_answer = result 
    if type(result) == str: # если функция возвращает строку (что не должно быть(кроме переводов из систем)) - выдает ошибку
        print(color.RED + 'Ошибка:',previous_answer,'\nРезультат обнулен! ٩(ఠ益ఠ)۶' + color.END)
        previous_answer = None # если вышла ошибка переменная снова "пуста"
    else:
        print(color.YELLOW + color.BOLD + 'Результат =' + color.YELLOW,round(result,eps), '( -_・)') # вывод результата
        

def user_input_with_pre(): # функция, которая вызывается если переменная предыдущего ответа не пуста
    global previous_answer
    print(color.PURPLE + 'Предыдущее значение =',round(previous_answer,eps),end='. '+ color.END)
    num_second = (input(color.PURPLE + 'Введите второе значение: ' + color.END)) # ввод второго числа
    if isnum(num_second): # проверка, является ли введенная переменная числом
        return previous_answer,float(num_second) # возвращает предущий ответ и второе float(число) 
    if type(num_second) == str:
        previous_answer = None
        return 'ERROR501' # ошибка - которая говорит о том, что введено не число


def one_user_input():
    num_first = (input(color.CYAN + 'Введите первое число: ' + color.END)) # вводится первое число str
    if isnum(num_first):
        return float(num_first)
    else:
        global previous_answer
        previous_answer = None
        return 'ERROR501' # ошибка - которая говорит о том, что введено не число   


def perevod_user_input():
    num_first = (input(color.CYAN + color.UNDERLINE + 'Введите первое число: ' + color.END)) # вводится первое число str
    if isnum(num_first):
        return str(int(float(num_first))) # отрабсывание дробной части и перевод в строку
    else:
        global previous_answer
        previous_answer = None
        return '' # ошибка - которая говорит о том, что введено не число


def perevod_user_output(func):
    result = func # переменная принимает значения функций
    global previous_answer # обращение глобальным данным переменных, которая описана выше
    previous_answer = result 
    if 'ERROR' in str(result):
        print(color.RED +'Ошибка: ',result,'. Результат обнулен! ٩(ఠ益ఠ)۶' + color.END,sep='') # вывод ошибки
    else:
        print(color.BLUE + 'Результат = ',result,'. Результат обнулен \(￣▽￣)/' + color.END,sep='') # вывод результата
    previous_answer = None
  
    
def main():
    print(color.YELLOW  + 'Добро пожаловать в приложение калькулятора! \nЧтобы посмотреть какие операции можно провести воспользуйтесь коммандой /help!\nУдачи!' + color.END)
    while True: # пока не написана команда /end
        user_com = str(input(color.DARKCYAN + 'Введите комманду: ' + color.END)) # вводится команда
        if user_commands(user_com):
            if user_com == '/help': # при вводе '/help' - использует функцию из commands.py user_help()
                user_help() # проходит по dict l_commands и возвращает ключ и всё его значения 
            if user_com == '/end': # при вводе '/end' - завершает while True
                break;
            if user_com == '/reset': # при вводе '/reset' делает previous_answer "пустым"
                global previous_answer # обращается к глобальной переменной previous_answer
                previous_answer = None
                print('Успешно сброшено!')
            if user_com in ['/summa','/chast','/vich','/umn']: # при вводе команды из списка
                if previous_answer == None: # если результат был не получен ранее
                    numbers = arifmetika_user_input() # переменная принимает значения из функции user_input() - tuple
                    user_output(globals()[user_com[1:]](numbers[0],numbers[1])) # обращается к функции global() - которая является словарем переменных 
                    # достает из словаря user_com[1:] и передает значения из tuple - по итогу получается так, 
                    # что строка введнная в переменную user_com - становится функцией 
                else: # если результат был получен ранее
                    numbers = user_input_with_pre()
                    user_output(globals()[user_com[1:]](numbers[0],numbers[1])) # такая же история как и выше
            if user_com in ['/stepen','/koren','/fact'] or user_com in ['/mactg','/matg','/macos','/masin','/mctg','/mtg','/mcos','/msin']: # при вводе команды из списка
                if previous_answer == None: # если результат был не получен ранее
                    numbers = one_user_input() # переменная принимает значения из функции user_input() - tuple
                    user_output(globals()[user_com[1:]](numbers)) 
                else: # если результат был получен ранее
                    numbers = previous_answer
                    user_output(globals()[user_com[1:]](numbers)) # такая же история как и выше
            if user_com in ['/from_oct','/from_bin','/from_dec']: # при вводе команды из списка
                if previous_answer == None: # если результат был не получен ранее
                    numbers = perevod_user_input() # переменная принимает значения из функции user_input() - tuple
                    perevod_user_output(globals()[user_com[1:]](numbers)) 
                else: # если результат был получен ранее
                    numbers = str(int(previous_answer)) # уберает дробную часть и переводит в строку
                    perevod_user_output(globals()[user_com[1:]](numbers)) # такая же история как и выше
        else:
            print(color.BOLD + color.RED + 'Вы ввели неправильную комманду! Воспользуйтесь /help!' + color.END)


main()