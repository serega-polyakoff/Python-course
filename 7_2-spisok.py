n = int(input("Введите длину: "))       # n это ввод с возможностью ввода только целых чисел(int)

user_list = []            # юзер лист это пустой список

i = 0
while i < n:
    string = "Введите элемент №" + str(i + 1) + ": "
    user_list.append(input(string))
    i += 1

print(user_list)