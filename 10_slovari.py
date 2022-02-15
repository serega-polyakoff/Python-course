country = {'code': 'RU', 'name': 'Russia', 'population': 144}
print(country['name'])

#country = dict(code='RU', name='Russia')   тоже самое, ток нельзя числа

for el in country:
    print(el)              # выводятся ключи значений

for key, value in country.items():    # выводятся ключ и значение через тире
    print(key, " - ", value)


#country.clear()       очищает словарь
#country.pop(name)         удаляет значение по ключу
#country.popitem()       удаляет последнюю позицию

print(country.keys())     # выводит все ключи
print(country.values())    #выводит все значения
print(country.items())    # выводит и ключи и их значения

country['code'] = 'None'    # обновляет значение в словаре
print(country)


person = {
    'user_1': {
        'first_name': 'John',
        'last_name': 'Marley',
        'age': 45,
        'address': ('г. Москва', 'ул. Юбилейная'),
        'grades': {'math': 5, 'physics': 3}
    },
    'user_2': {}
}

print(person['user_1']['address'][1])

