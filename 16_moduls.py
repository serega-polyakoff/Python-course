import time      # импортировал модуль тайм

time.sleep(3)    # программа выполнится через 3 сек
print("Hello")

import  datetime as d    # импорт дэйтайм переименуя в д
print(d.datetime.now().time().hour)

import sys, os   # можно импортировать несколько модулей
print(os.name)

from math import sqrt as s  # из модуля math импортировать только sqrt под именем s
print(s(25))

import cowsay
cowsay.cow('Hello')