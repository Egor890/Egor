# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 08:36:04 2021

@author: vias12
"""

N=int(input("Введите кол-свто студентов "))
a=[str(input("Введите имя студентов ")).split() for i in range(N)]
for i in range(len(a)):
    print(a[i])
print("Введите оценки студентов по дисциплинне: ")
b=[]
for i in range(len(a)):
    c=[]
    print(a[i],"=")
    for j in range(4):
        c.append(int(input()))
    b.append(c)
print(b)


            
f=[]#Список фамилий назначенных на повышенную стипендию
h=[]#Список фамилий назначенных на обычную стипендию
z=[]#Список фамилий неуспевающих студентов          
v=0 #счетчик фамилий на повышенную стипендию
o=0 #счетчик фамилий на обычную стипендию 
u=0 #счетчик фамилий неуспевающих студентов   




      
for i in range(N):
    k=[]
    for j in range(4):#разбиваем массив b построчно
        k.append(int(b[i][j]))
    d=sum(k)#находим сумму оценок одного студента
    
    
    def multi(k):#ф-я перемножения строки с оценками(каждая строка массива b это оценки студентов,1 строка= 1 строка оценок одного студента)
        umno=1
        for i in range(len(k)):
            umno=umno*k[i]
        return(umno)

    
    
    if  d==20:
        print("Студент ",a[i]," получит повышенную стипендию")
        f.append(a[i])
        v=v+1

    elif (d>=16) and (d<20) and (d%2==0) and (multi(k)>=256):#проверка студента на оценки(если есть оценка 3 то он не получит стипендию)
        print("Студент ",a[i]," получит среднюю стипендию")
        h.append(a[i])
        o=o+1
    else:
        print("Студент",a[i],"не получит стипендию")
        z.append(a[i])
        u=u+1
        
for i in range(N):
     print(a[i],"Оценки")
     for j in range(4):
         print(b[i][j])
t=[]
for i in range(N):
    summ=0
    k=4
    x=0
    for j in range(4):
        summ=summ+b[i][j]#находим сумму оценок одного студента
    x=summ/k#средняя оценка студента
    t.append(x)
    print("Средний балл студента",a[i],"= ",x)
y=sum(t)/N    
print("Средний балл группы= ",y)
print("Списки фамилий студентов назначенных на повышенную стипендию")
for i in range(v):
    print(f[i])
print("Спискок фамилий студентов назначенных на обычную стипендию")
for i in range(o):
    print(h[i])
print("Список фамилий неуспевающих студентов")
for i in range(u):
    print(z[i])
    