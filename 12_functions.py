def test_func():      # деф-создание функции
    pass              # пасс- ничего
    print("Hello", end="")   # енд чтобы ! был на той же строке
    print("!")

test_func()

def function_one(word):      # передается параметр который указавается при выводе
    print(word, end="")
    print("!")

function_one(999999)
function_one(True)
function_one("любое значение")

def summa(a, b):        # созд функцию с 2 параметрами
    res = a + b         # условие рез = а + б
    print("Result:", res)   # напишет результат: и условие

summa(3, 9.2)
summa("H", "i")

def sum(a, b):
    return a + b

print(sum(1,1))
result = sum(2, 8)    # поместил результат функции в отдельную переменную
print(result)

# !програма, которая находит миним элемент в списке, без использ функции
nums1 = [4.1, 2.2, 1, 0.9, 22]
min = nums1[0]   # предположим что первый элемент минимальный
for el in nums1:  # создаю цикл для намс
    if el < min:   # !если текущий элемент меньше чем "текущий минимальный" элемент тогда
        min = el   # тогда это новый минимальный элемент

print(min)

#создание функции для нахождения мин значения
def minimal(list):
    min_number = list[0]
    for ele in list:
        if ele < min_number:
            min_number = ele     # тоже самое как и без функ

    print(min_number)

minimal(nums1)


funct = lambda x, y: x * y  # сокращенная "анонимная" функция
res = funct(5, 31)
print(res)








