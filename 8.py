word = 'geodesia'
print(word.count('i'))   # количество i в word
print((word.upper()))    # word заглавными
print(word.isupper())    #
print(word.capitalize())  # с заглавной
print(word.find('odes'))  # найти по порядковому номеру начиная с 1 символа

list = 'football, basketball, skate'
print(list.split(','))      # делит на список по символу

hobby = list.split(', ')
print(hobby[2])


for el in range(len(hobby)):          # цикл el по всей длине списка hobby
    hobby[el] = hobby[el].upper()     # список заглавными

result = ", ".join(hobby)          # соединяет список в строку по указ. элементу

print(result)

slovo = 'Football'
print(slovo[0:4])              #
print(slovo[4:])
print(slovo[2:-2])
print(slovo[1:-1:2])           # добавляет шаг через одну