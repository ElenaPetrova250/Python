#2. Напишите программу, которая найдёт произведение пар чисел списка (CСписок создаем как в предыдущем задании).
#  Парой считаем первый и последний элемент, второй и предпоследний и т.д.

N = int(input("Размер списка: "))

list = []

for i in range(N):
    list.append(i)

print(list)


for i in range (len(list)):
    if [i] != [-i]:
        [i]+[-i]
print (i)


#print(list[0]+list[-1])
#в этой задаче не смогла кодом написать как перебрать элементы до конца списка и вывести в отдельную строку. Т.е. в голове все сложилось
# а в программе написать толково не смогла