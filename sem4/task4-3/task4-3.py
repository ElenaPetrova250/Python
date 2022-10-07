#Задайте последовательность цифр. Напишите программу, которая выведет список неповторяющихся элементов
#исходной последовательности

from random import randint as rI

List = {}
finalStr = " "

listStr = "".join(list(map(str,[rI(0 , 9) for i in range(20)])))
print (f"Задана последовательность цифр {listStr}")


for z in listStr:
    if List.get(z):
        List[z] = List.get(z)+1
    else:
        List[z] = 1

for i in List.items():
    if i[1] == 1:
        finalStr += str(i[0])
print(f"Уникальные цифры{finalStr}") if finalStr else print ("Уникальных позиций нет")