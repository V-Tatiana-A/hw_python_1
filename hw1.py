# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

print("Задача 2")
number=input("Введите трехзначное число:  ")
if number.isdigit() == False or len(number)!=3:
    print('Ошибка ввода')
else:
    number=int(number)
    dig_sum=0
    while number>0:
        dig_sum+=int(number%10)
        number=number/10
    print(dig_sum)



# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# *Пример:*
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10

print("Задача 4")
number=int(input("Введите количество журавликов:  "))
ps=int(number/3/2)
kat=int(number/3*2)
print(f'Петя и Сережа сделали по {ps} журавлика(ов). Катя сделала {kat}.')
if number%3!=0 or number/3%2!=0: print(f'{number} журавлика(ов) на троих не поделили, так что {number-ps*2-kat} они сделали вместе')



# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет
# счастливость билета.
# *Пример:*
# 385916 -> yes
# 123456 -> no

print("Задача 6")
number=input("Введите шестизначное число:  ")
if number.isdigit() == False or len(number)!=6:
    print('Ошибка ввода')
else:
    num1=list(map(int, number[:3]))
    num2=list(map(int, number[3:]))
    if sum(num1)==sum(num2):
        print("Билет счастливый")
    else:
        print("Билет не счастливый")



# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать
# один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# 3 2 4 -> yes
# 3 2 1 -> no

x, y, z = map(int, input("Введите размер шоколадки, а также нужное количество долек через пробел: ").split())
if z%x==0 or z%y==0:
    print(f"Да, так отломить можно")
else: print(f"Нет, столько отломить ровно не получится")