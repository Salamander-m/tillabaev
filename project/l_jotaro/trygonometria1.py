#Модуль тригонометрии
from math import *

def isint(s):   #проверка на целое число
    try:
        int(s)
        return True
    except ValueError: 
        return False

# Функции тригонометрии

def msin(x):
    if not isint(x): # проверка на ввод
        return "ERROR_302" # код ошибки ввода
    else:
        return (sin(int(x))) #возрат значения синуса

def mcos(x):
    if not isint(x): # проверка на ввод
        return "ERROR_302" # код ошибки ввода
    else:
        return (cos(int(x))) #возврат значения косинуса

def mtg(x):
    if not isint(x): # проверка на ввод
        return "ERROR_302" # код ошибки ввода
    else:
        if cos(int(x)) == 0:
            return "ERROR_301" #ошибка деления на ноль
        else:
            return (sin(int(x))/cos(int(x))) #возврат значения тангенса

def mctg(x):
    if not isint(x): # проверка на ввод
        return "ERROR_302" # код ошибки ввода
    else:
        if sin(int(x)) == 0:
            return "ERROR_301" #ошибка деления на ноль
        else:
            return (cos(int(x))/sin(int(x))) #возврат значения котангенса

def masin(x):
    if not isint(x): # проверка на ввод
        return "ERROR_302" # код ошибки ввода
    else:
        if int(x) < -1 or int(x) > 1:
            return "ERROR_303" #ошибка области определения
        else:
            return (asin(int(x))) #возврат значения арксинуса

def macos(x):
    if not isint(x): # проверка на ввод
        return "ERROR_302" # код ошибки ввода
    else:
        if int(x) < -1 or int(x) > 1:
            return "ERROR_303" #ошибка области определения
        else:
            return (acos(int(x)))  #возврат значения аркосинуса

def matg(x):
    if not isint(x): # проверка на ввод
        return "ERROR_302" # код ошибки ввода
    else:
        return (atan(int(x))) #возврат значения арктангенса

def mactg(x):
    if not isint(x): # проверка на ввод
        return "ERROR_302" # код ошибки ввода
    else:
        return ((cos(int(x))/sin(int(x)))**-1) #возврат значения аркатангенса 

