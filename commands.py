from style import color
l_commands = {}
l_commands['Выход'] = ['/end']
l_commands['Вывод всех комманд'] = ['/help']
l_commands['Арифметика'] = ['/summa','/chast','/vich','/umn']
l_commands['Функции для чисел'] = ['/stepen','/koren','/fact']
l_commands['Функции для перевода (отбрасывают дробную часть)'] = ['/from_oct','/from_bin','/from_dec','/from_hex']
l_commands['Тригонометрия'] = ['/mactg','/matg','/macos','/masin','/mctg','/mtg','/mcos','/msin']
l_commands['Сброс предыдущего значения'] = ['/reset']


def user_commands(com):
    res = []
    for i in l_commands:
        for j in l_commands.get(i):
            res.append(j)
    if com in res:
        return True
    else:
        return False

def user_help():
    for i in l_commands:
        ans = ''
        for j in l_commands.get(i):
            ans += j + ' '
        print(color.GREEN + i,': ',ans,sep='',end='\n'+color.END)