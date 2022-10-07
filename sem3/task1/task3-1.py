#1. Задайте рандомно список из чисел размером N, где N число с клавиатуры.
#  Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

N = int(input("Размер списка: "))

list = []

for i in range(N):
    list.append(i)

print(list)

even = 0
odd = 0

while N > 0:
    if N % 2 == 0:
        even += 1
    else:
        odd += 1
    N = N // 10
 
print("Even: %d, odd: %d" % (even, odd))

def rec_linear_sum(some_list):
    answ = 0
    for odd in some_list:
        answ += odd
    return answ
print ("Сумма нечетных элементов равна: {odd}")

# В данной задаче не до конца разобралась с выводом общего количества нечетных элементов