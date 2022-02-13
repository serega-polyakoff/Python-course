nums = [9, 3, 8, True, "Hello", 2.3, [2, 1, 7]]

nums[0] = 50
nums[4] = 1

print(nums[0])          # список начинается с 0
print(nums[2])          #
print(nums[-1][0])      # вывод из списка в списке


numbers = [2, 5, 24]
# numbers[3] = 100         # не существует такой позиции в списке

numbers.append(90)         # добавляет в конец списка значение
numbers.insert(0, True)    # ставит перед указанным значением новое
numbers.extend([6, 1, 8])   # добавляет в конец списка

b = [1000, 888]
numbers.extend(b)       # добавл b в конец списка

print(numbers)

spisok = [4, 6, 88, 21, 100, 0, True]

spisok.sort()      # сортирует список по возраст(True = 1 F=0)
spisok.reverse()   # переворачивает список наоборот
spisok.pop()      # удаляет последний элемент
spisok.pop(0)     # удаляет первый элемент
spisok.remove(88)  # удаляет конкретное значение
#spisok.clear()    # полностью очищает список

print(spisok)
print(spisok.count(True))  # указывает колисество указанных значений в списке
print(len(spisok))        # указывает длину списка

#for el in spisok:
#    print(el)       # цикл выводит все элементы из списка

for el in  spisok:  # цикл выводит все элем умнож на 2
    el *= 2
    print(el)
