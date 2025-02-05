import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
import math
from tempfile import TemporaryFile

#создание графиков
fig1=plt.figure(1)
fig2=plt.figure(2)

ax1 = fig1.subplots()
ax2 = fig2.subplots()
#начальные данные
t0=0
T=5
tau=(math.pi/2)

#параметр m
m1=10000
m2=m1*2
name_file="foo4.csv"
name_file1="foo4_t.csv"
delta1=tau/m1
delta2=tau/m2
#число шагов
N1=round(T/delta1)
N2=round(T/delta2)
#начальная функция
def fi(t):
    return math.exp(t)*math.cos(t)
#функция f
def f(t,u_n,u_n_m):
    return (u_n-math.exp(tau)* u_n_m)

#точное решение
def answ(t):
    return math.exp(t)*math.cos(t)
#-----------Для m1,delta1,N1-------------------------
#наборы значений в узлах
u_i=[] #приблеженное значение
x_i=[] #точное хначение
t_i=[] #узлы для вывода
m=m1
N=N1
delta=delta1
#цикл для точного решения
for i in range(-m, N+1):
    t=t0+delta*i
    x_i.append(answ(t))
    t_i.append(t)
#вывод точного решения

ax1.plot(t_i, x_i,label="Точное решение при m=" +str(m),linewidth=1)


#Явный метод Эйлера
#1 шаг: от -m до 0 начальная функция
for i in range(-m,1):
    t=t0+delta*i
    u_i.append(fi(t-t0))

#2 шаг: от 0 до N-1 метод
for i in range(0,N):
    t=t0+delta*i
    u_n=u_i[-1]
    u_n_m=u_i[-1-m]
    #print(u_n_m)
   
    rez=u_n+delta*f(t,u_n,u_n_m)
    #print(rez, u_n, u_n_m)
    u_i.append(rez)
    #print(rez)

#вывод приближонного решения
ax1.plot(t_i, u_i,label="Метод Эйлера при m=" +str(m),linewidth=4,linestyle = ':')
#print(u_i)
temp1=[]
for i in range(len(u_i)):
    temp1.append(abs(x_i[i]-u_i[i]))
print("-"*10)
print(max(temp1))
print("-"*10)
u_i.append(delta)
x = np.array(u_i)
y=np.array(t_i)
#print(x)
np.savetxt(name_file, x, delimiter=",")
np.savetxt(name_file1, y, delimiter=",")
#-----------------------------

#-----------Для m2,delta2,N2-------------------------
#наборы значений в узлах
u_i=[] #приблеженное значение
x_i=[] #точное хначение
t_i=[] #узлы для вывода
m=m2
N=N2
delta=delta2
#цикл для точного решения
for i in range(-m, N+1):
    t=t0+delta*i
    x_i.append(answ(t))
    t_i.append(t)
#вывод точного решения

ax2.plot(t_i, x_i,label="Точное решение при m=" +str(m),linewidth=1)


#Явный метод Эйлера
#1 шаг: от -m до 0 начальная функция
for i in range(-m,1):
    t=t0+delta*i
    u_i.append(fi(t-t0))

#2 шаг: от 0 до N-1 метод
for i in range(0,N):
    t=t0+delta*i
    u_n=u_i[-1]
    u_n_m=u_i[-1-m]
    #print(u_n_m)
   
    rez=u_n+delta*f(t,u_n,u_n_m)
    #print(rez, u_n, u_n_m)
    u_i.append(rez)
    #print(rez)
temp2=[]
for i in range(len(u_i)):
    temp2.append(abs(x_i[i]-u_i[i]))
print("-"*10)
print(max(temp2))
print("-"*10)
#вывод приближонного решения
ax2.plot(t_i, u_i,label="Метод Эйлера при m=" +str(m),linewidth=4,linestyle = ':')   
#-----------------------------
#print(N2)

print(math.log(max(temp1)/max(temp2), 2))


#----------Графики-------------
ax1.set_xlabel('t')
ax1.set_ylabel('x')

ax1.set_title("Графики решений")
ax1.legend()

ax2.set_xlabel('t')
ax2.set_ylabel('x')

ax2.set_title("Графики решений")
ax2.legend()

plt.show()




