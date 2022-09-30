#Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.

a = int(input("Задайте число N: "))

def arr (n):
    m = []
    for i in range (1,n+1):
        m.append((1+1/i)**i)
    return m

print(arr(a))
print(sum(arr(a)))
