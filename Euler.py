# -*- coding: utf-8 -*-

import numpy as np
from scipy.optimize import fsolve

def implicit_euler(f, y0, t): # Версия функции, использующая fsolve при решении, для сравнения 

    h = t[1] - t[0]
    n = len(y0)

    y = np.zeros((n, len(t)))
    y[:, 0] = y0

    for i in range(1, len(t)):
        # Определяем неизвестное значение y_i+1
        def fun(y_i1):
            return y_i1 - y[:, i-1] - h * f(t[i], y_i1)
        # Решаем нелинейное уравнение методом Ньютона
        y[:, i] = fsolve(fun, y[:, i-1])
    
    return y


import numpy as np

def implicit_euler1(f, y0, t, accuracy, h):
    # f - функция правых частей системы ОДУ
    # y0 - начальные условия
    # t - массив точек времени
    if h is None: h=0.01

    n = int((t[1] - t[0])/h) #len(t)
    m = len(y0)
    y = np.zeros((n, m))
    y[0,:] = y0
    for i in range(1, n):
        dt = h
        # Решаем уравнение с помощью метода Ньютона
        #y[i,:] = y[i-1,:] + dt*f(t[i-1], y[i-1,:])
        y[i,:] = y[i-1,:] + dt*f(t[0] + i*h, y[i-1,:])# y[i,:] = 0 изначально (n=1)
        for j in range(30):
            y_new = y[i-1,:] + dt*(f(t[0]+ i*h, y[i,:]) + f(t[0] +(i-1)*h, y[i-1,:]))/2 # Приближаем y[i,:] 
            if np.linalg.norm(y_new - y[i,:]) < accuracy:
                break
            y[i,:] = y_new
    return y



def f(t, y):
    dy1_dt = -2*y[0] + y[1] + 4*t
    dy2_dt = y[0] - y[1] + 1
    return np.array([dy1_dt, dy2_dt])

# Начальные условия и массив точек для решения
y0 = np.array([0, 1])
t_lin = np.linspace(0, 1, 1000)
t = [0, 1]

y = implicit_euler1(f, y0, t, 0.00001, 0.001)

print(y)

from scipy.integrate import solve_ivp
solution = solve_ivp(f, [0, 1], y0, t_eval=t_lin)
print('\n True solution: \n', solution)



true_accuracy = np.linalg.norm(y - solution.y.T)
print(true_accuracy)
steps = [0.2, 0.1, 0.05, 0.02, 0.01, 0.005, 0.002, 0.001, 0.0005, 0.0002, 0.0001] # Набор различных шагов
acc_func = np.linalg.norm(y - solution.y.T) #Получаем точность метода как норму разницы нашего и библиотечного метода
acc = []
for i in range(11):
    true_sol = solve_ivp(f, [0, 1], y0, t_eval=np.linspace(0, 1, int(1/steps[i])))
    sol = implicit_euler1(f, y0, t, 0.00001, steps[i])
    acc.append(np.linalg.norm(sol - true_sol.y.T))

finY1 = []
finY2 = []
true_finY = []
for i in range(11):
    true_sol = solve_ivp(f, [0, 1], y0, t_eval=np.linspace(0, 1, int(1/steps[i])))
    sol = implicit_euler1(f, y0, t, 0.00001, steps[i])
    finY1.append(sol[int(1/steps[i])-1, 0])
    finY2.append(sol[int(1/steps[i])-1, 1])
    #true_finY.append(true_sol)

print(acc)
import matplotlib.pyplot as plt
plt.plot(steps, acc)
plt.xscale('log')
plt.xlabel('length of step')
plt.ylabel('Error value (linalg.norm)')

from matplotlib import axes as ax

#ax.plot(steps, finY1, label = 'y1')
#ax.plot(steps, finY2, label = 'y2')
#plt.plot(steps, finY2)
#plt.xscale('log')
#plt.xlabel('length of step')
#plt.ylabel('Y(t)')

plt.gca().invert_xaxis()
plt.show()


