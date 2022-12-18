# 4. Задана натуральная степень k. Сформировать 
# случайным образом список коэффициентов (значения от 0 до 100) 
# многочлена и записать в файл многочлен степени k.
# *Пример:* 
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
# Не понятно условие Степень будем записывать как x**y
import random

y = int(input('Введите степень многочлена: '))
li = random.sample(range(10),y)
s=''
x=y
for i in range (y):
    if li[i]!=0:
        if len(s)>0:
            s+='+'
        if x==2:
            if li[1]==1:
                s+='X'
            else:
                s+=str(li[i])+ 'X'
        elif x==1:
            s+=str(li[i])
        else:
            if li[i]==1:
                s+='X**'+str(x)
            else:
                s+=str(li[i])+ 'X**'+str(x)
    x-=1
s+='=0'
print(s)
f=open('file.txt','w')
f.write(s)
f.close()