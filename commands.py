from style import color
l_commands = {}
l_commands['Выход'] = ['/end']
l_commands['Вывод всех комманд'] = ['/help']
l_commands['Сброс предыдущего значения'] = ['/reset']
l_commands['Перезапуск'] = ['/restart']
l_commands['Арифметика'] = ['/summa','/chast','/vich','/umn']
l_commands['Функции для чисел'] = ['/stepen','/koren','/fact']
l_commands['Функции для перевода'] = ['/from_oct','/from_bin','/from_dec','/from_hex']
l_commands['Тригонометрия'] = ['/mactg','/matg','/macos','/masin','/mctg','/mtg','/mcos','/msin']
l_commands['Общие сведения'] = ['Принимаются числа пи и е - pi и e. Чтобы их использовать достаточно при вводе значения (также степени) ввести pi или e.\nДля получения большей информации воспользуйтесь /help+[имя раздела].\nЧтобы узнать по каким разделам есть информация - "/help Разделы"']

help_commands = {}
help_commands['Арифметика'] = ['Команды запрашивают 2 значения на ввод после ввода команды. Могут вернуть число или ошибку. \nПосле их выполнения, результат команды записывается и может быть в дальнейших вычислениях.\nКомманды:','/summa','/chast','/vich','/umn']
help_commands['Функции для чисел'] = ['Команды запрашивают 1 значение на ввод после ввода команды. Могут вернуть число или ошибку. \nКоманда /fact принимает любое число (до 1558), но будет откинута его дробная часть.\nПосле их выполнения, результат команды записывается и может быть использован в дальнейших вычислениях.\nКомманды:','/stepen','/koren','/fact']
help_commands['Функции для перевода'] = ['Команды запрашивают 2 значения на ввод после ввода команды - число и основание для перевода. Могут вернуть результат или ошибку. \nПосле их выполнения, результат команды НЕ записывается.\nКомманды:','/from_oct','/from_bin','/from_dec','/from_hex']
help_commands['Тригонометрия'] = ['Команды запрашивают 1 значение на ввод после ввода команды. Могут вернуть число или ошибку. \nКоманды принимают значение как радианы.\nПосле их выполнения, результат команды записывается и может быть в дальнейших вычислениях.\n/masin и /macos имеют ограничение [-1,1]\n/mtg и /mctg не принимают значение 0\nКомманды:','/mactg','/matg','/macos','/masin','/mctg','/mtg','/mcos','/msin']
help_commands['Разделы'] = ['1.Арифметика','2.Функции для чисел','3.Функции для перевода','4.Тригонометрия']

def commands():
    return help_commands.keys()

def commands_item(s):
    return help_commands.get(s,'Такого раздела нет')

def user_commands(com):
    res = []
    for i in l_commands:
        for j in l_commands.get(i):
            res.append(j)
    if com in res:
        return True
    else:
        return False

def user_help_color():
    for i in l_commands:
        ans = ''
        for j in l_commands.get(i):
            ans += j + ' '
        print(color.GREEN + i,': ',ans,sep='',end='\n'+color.END)


def user_help():
    for i in l_commands:
        ans = ''
        for j in l_commands.get(i):
            ans += j + ' '
        print(i,': ',ans,sep='',end='\n')

