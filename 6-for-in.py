for i in range(1, 6, 2):       # вывожу i из диапазона (от,до,шаг)
    print(i)

count = 0                      # выставляю значение count равен 0
word = "Hello World!"
for i in word:                 # вывожу i из word
    if i == "l":               # если i это l
        count += 1             # то счетчик (count) прибавляет 1

print("Count:", count)         # выводится счетчик


for a in range(1, 11):         # найду а из диапазона(от,до)
    if a == 8:                 # если а равно 4
        break                  # то цикл останавливается
    if a % 2 == 0:             # если а делится на 2 без остатка
        continue               # переменная пропускается
    print(a)


found = None                # присваиваю пустое значение found
for z in "Hello":           # нуйду z из Hello
    if z == "e":            # если z равен "e"
        found = True        # тогда  found выводит True
        break               # !!! цикл останавливается, иначе он продолжается и присваивает следующее значение ( False)
else:                       # Иначе ( "e" не найден)
    found = False           #
print(found)
