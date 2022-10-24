from project.e_roxan.degrees_n_fact import * # первый модуль с факт, степ, корень, переовод из 8сс, а также чисел pi,e (они используются в пакете из другого блока)
from project.e_roxan.trans_8 import from_oct
from project.g_palnaref.trans_2 import from_bin
from project.r_joseph.trans_10 import from_dec
from project.l_jotaro.trans_16 import from_hex
from project.l_jotaro.trygonometria1 import *
from arifmetika_main import * # адаптированный из второго модуля (только арифметика), подходящая для главной программы
from commands import commands, commands_item, user_commands
from commands import user_help 
from os import system 
import sys
# Объявления предущей переменной как "пустой", по которой сравнивается были ли предыдущие действия за сессию программы
previous_answer = None
e = 9 # разрядность до 9 знаков

# проверка на ^C и ^Z
def ch(st):
    while True:
        try:
            s = (input(f'{st}' )) # вводится команда
            return s
        except KeyboardInterrupt:
            print('ERROR502:input ^C') # введенный символ ^C
        except EOFError:
            print('ERROR503:input ^Z') # введенный символ ^Z

def wpie(n):
    if n == 'pi':
        return PI
    elif n == 'e':
        return EPS
    else:
        return n

# функции проверки строки, на всё ли элементы в ней цифры
def isnum(s): # конструкция try-except
    try: # пытается привести s к float
        float(s)
        return True # если получается - возвращает True
    except ValueError:
        return False # нет - False


def check_input(n): # убреает необходимые знаки, чтобы цифр в числе было 9
    try:
        n = float(n)
    except ValueError:
        return n
    int_part = str(int(n)) 
    if len(int_part) < e:
        return(int(n) + round((n%1),e-len(int_part)))
    elif len(int_part) > e:
        return((int(n) // 10**(len(int_part) - e)))
    else:
        return(float(n))

def arifmetika_user_input(): # функция для ввода переменных
    num_first = ch('Введите первое число: ')
    num_first = wpie(num_first)
    if isnum(num_first):
        if check_input(num_first) != float(num_first):
            num_first = ('ERROR504: Число больше 9-ти разрядов')
    elif type(check_input(num_first)) == str:
        num_first = check_input(num_first)
    num_second = ch('Введите второе число: ')
    num_second = wpie(num_second)
    if isnum(num_second):
        if check_input(num_second) != float(num_second):
            num_second = ('ERROR504: Число больше 9-ти разрядов')
    elif type(check_input(num_first)) == str:
        num_first = check_input(num_first)
    return num_first,num_second # возвращает введенные значения в tuple


def user_output(func): # функция для вывода результата или ошибки
    result = func # переменная принимает значения функций
    global previous_answer # обращение глобальным данным переменных, которая описана выше
    previous_answer = result 
    if type(result) == str: # если функция возвращает строку (что не должно быть(кроме переводов из систем)) - выдает ошибку
        print('Ошибка:',previous_answer,'\nРезультат обнулен!')
        previous_answer = None # если вышла ошибка переменная снова "пуста"
    else:
        if check_input(result) != result:
            print('Результат = ',check_input(result),'. Ответ был обрезан до 9-ти разрядов.',sep='')
        else:
            print('Результат = ',check_input(result))

        

def user_input_with_pre(): # функция, которая вызывается если переменная предыдущего ответа не пуста
    global previous_answer
    print('Предыдущее значение =',check_input(previous_answer))
    num_second = ch('Введите второе число: ')
    num_second = wpie(num_second)
    if isnum(num_second): # проверка, является ли введенная переменная числом
        if check_input(num_second) != float(num_second):
            num_second = ('ERROR504: Число больше 9-ти разрядов')
            return previous_answer,num_second # возвращает предущий ответ и второе - ошибку
        else:
            return previous_answer,float(num_second) # возвращает предущий ответ и второе float(число) 
    else:
        previous_answer = None
        return 'ERROR501: Введено не число' # ошибка - которая говорит о том, что введено не число


def one_user_input():
    num_first = ch('Введите первое число: ')
    num_first = wpie(num_first)
    if isnum(num_first):
        if check_input(num_first) != float(num_first):
            num_first = ('ERROR504: Число больше 9-ти разрядов')
            return num_first
        else:
            return float(num_first)
    else:
        global previous_answer
        previous_answer = None
        return 'ERROR501: Введено не число' # ошибка - которая говорит о том, что введено не число   


def perevod_user_input():
    num_first = ch('Введите первое число: ')
    if isnum(num_first):
        if len(num_first) < 9:
            return str(int(float(num_first))) # отрабсывание дробной части и перевод в строку
        else:
            print('ERROR504: Число больше 9-ти разрядов')
            return ''
    else:
        global previous_answer
        previous_answer = None
        return '' # ошибка - которая говорит о том, что введено не число


def perevod_user_output(func):
    result = func # переменная принимает значения функций
    global previous_answer # обращение глобальным данным переменных, которая описана выше
    previous_answer = result 
    if 'ERROR' in str(result):
        print('Ошибка: ',result,'. Результат обнулен!' ,sep='') # вывод ошибки
    else:
        if int(check_input(result)) != int(result):
            print('Результат = ',int(check_input(result)),'\nОтвет был обрезан до 9-ти разрядов. Результат обнулен!',sep='')
        else:
            print('Результат = ',int(check_input(result)),'\nРезультат обнулен!',sep='')
    previous_answer = None
  
    
def main():
    system('cls')
    print('Добро пожаловать в приложение калькулятора! \nЧтобы посмотреть какие операции можно провести воспользуйтесь коммандой /help!\nУдачи!' )
    while True: # пока не написана команда /end
        user_com = ch('Введите комманду: ' )
        if len(user_com.split()) > 1 and '/help' in user_com:
            sp = user_com.split()
            if sp[1] in commands():
                if sp[1] == 'Разделы':
                    print(20*'-',*commands_item(sp[1]),sep='\n',end='\n'+20*'-'+'\n')
                    user_com = ch('Введите комманду: ' )
                    for i in commands_item(sp[1]):
                        if user_com in i:
                            print(*commands_item(i[2:]))
                else:
                    print(*commands_item(sp[1]))
           
        else:
            if user_commands(user_com):
                if user_com == '/help': # при вводе '/help' - использует функцию из commands.py user_help()
                    user_help() # проходит по dict l_commands и возвращает ключ и всё его значения 
                if user_com == '/end': # при вводе '/end' - завершает while True
                    system('cls') # после этого очищает терминал
                    break;
                if user_com == '/restart':
                    system('cls & python start.py') # после этого очищает терминал и запускает файл заново
                    sys.exit() # выключает текущую сессию
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
                print('Вы ввели неправильную комманду! Воспользуйтесь /help!' )


main()