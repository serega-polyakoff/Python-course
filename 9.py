data = (4, 5, 5, 88, 21, False, 'Hello')
# data[0] = 11      картежи нельзя изменять в отличае от списка
print(data[1])
print(data[2:-2])
print(len(data))

#for el in data:
#   print(el)

nums = [2, 3, 10]
new_data = tuple(nums)    #функция тапл преобразует список в кортеж
print(new_data)

word = tuple('Hello')
print(word)
