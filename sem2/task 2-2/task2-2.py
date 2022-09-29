# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
#Пример:
#пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

N = int(input("Введите число N: "))

def N (n):
    if n == 1:
        return 1
    else:
        return n*N(n-1)

list = []
for e in range(1, N + 1):
    list.append(N(e))

print(f"Произведения чисел от 1 до {N}:  {list}")