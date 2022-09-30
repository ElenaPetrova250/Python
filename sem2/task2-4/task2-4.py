#Реализуйте алгоритм перемешивания списка.

number = int(input("Размер списка: "))

listA = []

for i in range(number):
    listA.append(i)

print(listA)

list_shuffled = []

for i in range(0, len(list)):
    j = random.randomrange(0, len(number))
    list_shuffled.append(number[j])
    list.remowe(number[j])
print(list_shuffled)