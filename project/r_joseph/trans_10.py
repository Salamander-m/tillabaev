def isint(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def from_dec(n):
    convert_system = (input('Введите желаемую в выводе систему счисления (2,8,16): ')) 
    if n == '':
        return ('ERROR_402') # n - пустое
    if isint(n):
        n = int(n)
        if convert_system == '8':
            return to8(n)
        if convert_system == '16':
            return to16(n)
        if convert_system == '2': 
            return to2(n)
        if convert_system == '10':
            return n
        if convert_system not in ['2','8','10','16']:
            return "ERROR_403" # не в нужных системах
    else:
        return "ERROR_401"
    
def to2(n):     # decimal to binary
    if n < 0:
        sign= '-'
    else:
        sign = ''
    n = abs(n)
    if str(n).isdigit() and isint(n):     # input validation
        return(sign + "{0:b}".format(n))
    else:
        return "ERROR_401"

def to8(n):
    if str(n).isdigit() and isint(n):     # input validation
        if n < 0:
            sign= '-'
        else:
            sign = ''
        n = abs(n)
        new_n = ''
        while n > 0:
            new_n = str(n % 8) + new_n
            n //= 8
        return(sign + new_n)
    else:
        return "ERROR_401"

def to16(n):
    if str(n).isdigit() and isint(n):     # input validation
        if n < 0:
            sign= '-'
        else:
            sign = ''
        n = abs(n)
        if not hasattr(to16, 'table'):        
            to16.table = '0123456789ABCDEF'       
        x, y = divmod(n, 16)        
        return sign + to16(x) + to16.table[y] if x else sign + to16.table[y]
    else:
        return "ERROR_401"
