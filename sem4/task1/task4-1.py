#Вычислить число c заданной точностью *d*
#Пример:
#при d = 0.001, π = 3.141
#при d = 0.1, π = 3.1
#при d = 0.00001, π = 3.14154
#d от 0.1 до 0.0000000001

#N = int(float("Введите заданную точность d: "))

k = 1
x = 0

for k in range(1, 1000000):
    x = x+4*((-1)**(k+1))/(2*k-1)
print(x)
print(f'{x:.3}')
print(f'{x:.4}')
print(f'{x:.2}')
print(f'{x:.6}')

