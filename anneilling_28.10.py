print("Hello world")
from random import *
print("Давай сыграем в игру выбери: Камень , ножницы или бумагу.")
a = 0
while (a == 0):
        c = int(input("1 - камень, 2 - ножницы, 3 - бумага. "))
        if (c == 1 or c == 2 or c == 3):
            a = 1    
if c == 1:
        print("Вы выбрали камень.")  
elif c == 2:
        print("Вы выбрали ножницы.") 
elif c == 3:
        print("Вы выбрали бумагу.")  
b = randint(1,3)

if b == 1:
        print("Бот выбрал камень.") 
elif b == 2:
        print("Бот выбрал ножницы.")
elif b == 3:
        print("Бот выбрал бумагу.")
if c == 1 and b == 1:
        win = 0
elif c== 1 and b == 2:
        win = 1
elif c== 1 and b == 3:
        win = 2
elif c== 2 and b == 1:
        win= 2
elif c== 2 and b == 2:
        win= 0
elif c== 2 and b == 3:
        win= 1
elif c== 3 and b == 1:
        win=1
elif c== 3 and b == 2:
        win=2
elif c== 3 and b == 3:
        win=0
if win == 0:
        print("Ничья!")
elif win == 1:
        print("Победил. Красавчик!")
elif win == 2:
        print("Победил бот!")
