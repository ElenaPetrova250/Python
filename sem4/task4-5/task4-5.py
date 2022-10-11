#Даны два файла, в каждом из которых находится запись многочлена.
#Задача - сформировать файл, содержащий сумму многочленов.

from random import randint as rI

degree = int(input("Введите максимальную степень многочлена: "))
equation = " "
equa1 = {}
equa2 = {}
final = {}

for d in range(degree, -1, -1):
    coef = rI(-20,20)
    if d == degree:
        if coef > 0:
            equation += str(coef) + 'x^' + str(d)
        if coef < 0:
             equation += ' - ' + str(abs(coef)) + 'x^' + str(d)
    else:
        if coef > 0:
                equation += ' + ' + str(coef) + 'x^' + str(d)
        if coef < 0:
                equation += ' - ' + str(abs(coef)) + 'x^' + str(d)
print(equation)

with open ('sem4/task4-5/file1.txt', 'w') as data:
    data.write(equation)

degree = int(input("Введите максимальную степень многочлена: "))
equation2 = " "

for d in range(degree, -1, -1):
    coef = rI(-20,20)
    if d == degree:
        if coef > 0:
            equation2 += str(coef) + 'x^' + str(d)
        if coef < 0:
             equation2 += ' - ' + str(abs(coef)) + 'x^' + str(d)
    else:
        if coef > 0:
                equation2 += ' + ' + str(coef) + 'x^' + str(d)
        if coef < 0:
                equation2 += ' - ' + str(abs(coef)) + 'x^' + str(d)
print(equation2)

with open ('sem4/task4-5/file2.txt', 'w') as data:
    data.write(equation)

equation = equation.replace(" + ", " +").replace(" - ", ' -').split()
equation2 = equation2.replace(" + ", " +").replace(" - ", ' -').split()

for i in range(len(equation)):
    equation[i] = equation[i].replace(" + ", "").split("x^")
    equa1[int(equation[i][1])] = [int(equation[i][0])]

for i in range(len(equation2)):
    equation2[i] = equation2[i].replace(" + ", "").split("x^")
    equa2[int(equation2[i][1])] = [int(equation2[i][0])]

print(equation)
print(equation2)
print(equa1)
print(equa2)

for i in range(max(len(equa1), len(equa2)), -1, -1):
    first = equa1.get(i)
    second = equa2.get(i)
    if first != None or second != None:
        final[i] = (first if first != None else 0) + (second if second != None else 0)
print()
print(final)

with open (r"sem4/task4-5/fileresult.txt", 'w') as data:
    file = data.read().split(" ")

