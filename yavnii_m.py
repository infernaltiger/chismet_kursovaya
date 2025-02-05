import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
import math
#параметр a
a=1
#длина отрезка где лежит x [0,l]
l=1
a_x,b_x=0,l
n_x=6
h=b_x/n_x


#длина временного отрезка
a_t,b_t=0,10
t0=0
delta=0.01
n_t=int(b_t/delta)
#print(n_y)
#зааоздывание tau_zap
tau = 1
m=int(tau/delta)
#точное решение
def u(x,t):
     return math.exp(a*t)*math.sin(x)
#явный сеточный алгоритм
def uji(x,t,matr,f_znach,j,i):
     sigma=(a*a*delta)/(h*h)
     res = sigma*matr[i-1][j] + (1-2*sigma)*matr[i][j] + sigma*matr[i+1][j] + delta*f_znach
     return res
def psi(x,t):
     return math.exp(a*t)*math.sin(x)
def fi1(t):
     return 0

def fi2(t):
     return math.exp(a*t)*math.sin(l)
def f(x,t,matr_nach,matr,j,i):
     if j-m<=0:
          return (2*a-(1/math.exp(a)))*math.exp(a*t)*math.sin(x)+matr_nach[i][j]
     else:
          return (2*a-(1/math.exp(a)))*math.exp(a*t)*math.sin(x)+matr[i][j-m]
          





fig1 = plt.figure(1)
fig2 = plt.figure(2)
fig3 = plt.figure(3)
ax1 = fig1.add_subplot(projection='3d')
ax2 = fig2.add_subplot(projection='3d')
ax3 = fig3.add_subplot(projection='3d')

#создание матриц узлов
x=[]
for i in range(n_x+1):
     x.append(i*h)
t=[]
t_nach=[]
for i in range(n_t+1):
     t.append(t0+i*delta)
for i in range(-m,1):
     t_nach.append(i*delta)
  
#создание матрицы значений u точного решениея
z=[]
for i in range(n_x+1):
     z.append([])
#создание матрицы значений uij приближенного решения
#и начальных значений для задержки

z1=[]
z1_nach=[]
for i in range(n_x+1):
     z1.append([])
     z1_nach.append([])

for i in range(n_x+1):
     z1[i].append(psi(x[i],0))

for j in range(m+1):
     #print(t_nach[j])
     for i in range(n_x+1):
          #print(x[i],t_nach[j],psi(x[i],t_nach[j]))
          z1_nach[i].append(psi(x[i],t_nach[j]))
#print(len(z1_nach[1]))    
for j in range(1,n_t+1):
     z1[0].append(fi1(t[j]))
     z1[n_x].append(fi2(t[j]))
#print(len(z1[0]))
#print(len(z1[1]))
#print(len(z1[2]))

for j in range(1,len(t)):
    for i in range(1,len(x)-1):
         f_z=f(x[i],t[j-1],z1_nach,z1,j-1,i)
         #print(z1[i+1])
         #print(i,j,x[i],t[j-1],z1[i][j-1],z1[i-1][j-1],z1[i+1][j-1])
         rez=uji(x[i],t[j-1],z1,f_z,j-1,i)
         z1[i].append(rez)

for i in range(len(x)):
     for j in range(len(t)):
          xij=u(x[i],t[j])
          z[i].append(xij)
          



#print(uji(x[0],y[0],z1,f,1998,8))
#x=x[::-1]
          
x=np.array(x)
t=np.array(t)
     
np.savetxt("x.csv", x, delimiter=',')
np.savetxt("t.csv", t, delimiter=',')

x, t = np.meshgrid(t ,x)
maxm=abs(z[0][0]-z1[0][0])
i1=0
j2=1
for i in range(len(z)):
     for j in range(len(z[i])):
         rez=abs(z[i][j]-z1[i][j])
         if rez>= maxm:
                 maxm=rez
                 i1=i
                 j2=j
print("-"*10)
print(maxm,h,delta,i1,j2)
print("-"*10)
x=np.array(x)
t=np.array(t)
z=np.array(z)
z1=np.array(z1)


np.savetxt("vals_orig_yavnii.csv", z.T, delimiter=',')
np.savetxt("vals_pribl_yavnii.csv", z1.T, delimiter=',')

ax1.plot_wireframe(t, x, z,edgecolor='green', lw=2, rstride=8, cstride=8, alpha=0.3)
ax2.plot_wireframe(t, x, z1,edgecolor='red', lw=2, rstride=8, cstride=8, alpha=0.3)

ax3.plot_surface(t, x, z,edgecolor='green', lw=2, rstride=8, cstride=8, alpha=0.3)
ax3.plot_wireframe(t, x, z1,edgecolor='red', lw=2, rstride=8, cstride=8, alpha=0.3)


ax1.set(title='Точное решение, a='+str(a),xlabel='x', ylabel='t', zlabel='u')
ax2.set(title='Приближенное решение,явная схема, l='+str(l)+', h='+str(h)+', delta='+str(delta),xlabel='x', ylabel='t', zlabel='u')
ax3.set(title='Точное и приближенное решение',xlabel='x', ylabel='t', zlabel='u')
plt.show()
