#data = input("Введите текст ")
#file = open('data/text.txt', 'a')
#открыл файл (если нет то создаст) и указал что для добавления инф
# 'w'-иинф будет переписываться 'a'- инф будет добавляться
#file.write(data + "\n")   # внутри напишет и чтобы !!! с новой строки
#file.close()  # файл нужно закрывать чтобы не было утечки памяти


file = open('data/text.txt', 'r')   # открыть только для чтения
print(file.read())
file.close()