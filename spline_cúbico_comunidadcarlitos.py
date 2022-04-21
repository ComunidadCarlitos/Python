# -*- coding: utf-8 -*-
"""spline_Cúbico_ComunidadCarlitos.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JnfCrzRocE3ST0RxjZ7nYZW4beKrA7ft
"""

############# Script creado por Comunidad Carlitos #################
####################################################################

############## librerias ##################
from sympy import solve, symbols, diff, sqrt, S, Interval, symbols
from sympy.parsing.sympy_parser import parse_expr
from numpy import matrix, linspace, zeros, array
from numpy.linalg import solve, det
import pylab as pl

x = symbols("x")
n= ## Numero de puntos que se tengan
p= ## Arreglo de puntos(cada punto es una fila)


A = zeros((4*(n-1),4*(n-1))) 
B = zeros(4*(n-1))

################### ecuaciones de continuidad #######################

h = 0
for i in range(n-1): # n-1 es la cantidad de ecuaciones
    for j in range(2): # se evalua por ambos extremos cada función
        i += j
        for k in range(4): # ecuaciones de grado 3 con 4 coeficientes
            A[i+h,k+(i-j)*4] = p[i,0]**(3-k)
            B[i+h] = p[i,1]
    h+=1

################ ecuaciones de primera derivada #####################

h = 0
for i,l in enumerate(range(2*(n-1),2*(n-1)+n-2)): #2*(n-1) es la cantidad de ecuaciones de continuidad --- n-2 es la cantidad de ecs de primera derivada
    for j in range(2):
        for k in range(3): # ecuaciones de grado 2 tienen 3 coeficientes
            A[l,k+(j+h)*4] = (-1)**(j)*(3-k)*p[1+i,0]**(2-k)
    h+=1

################ ecuaciones de segunda derivada ####################

h = 0
for i,l in enumerate(range(2*(n-1)+n-2, 2*(n-1)+2*(n-2))):
    for j in range(2):
        for k in range(2): # ecuaciones de grado 1 tienen 2 coeficientes
            A[l,k+(j+h)*4] = (-1)**(j)*(2-k)*(3-k)*p[1+i,0]**(1-k)/2
    h+=1

############## ecuaciones de condiciones iniciales #################

h = 0
i = 0

for j in range(2): # 2 puntos extremos de la ecuación
    for k in range(2): # ecuaciones de grado 1 tienen 2 coeficientes
        A[4*(n-1)-2+j,i+k] = (2-k)*(3-k)*p[h,0]**(1-k)/2
    i += 4*(n-2)
    h += n-1

########### Solución del sistema de ecuaciones lineal ##############

if det(A) == 0: ## verifica si la matriz es invertible
    print("""
      
No existe aproximación por el metodo ya que el sistema no tiene solución
Intente con otros puntos.
""")
else:
    C = solve(A,B) ## metodo de Gauss con la libreria Numpy

########################### Gráfica ################################
    
    splines = zeros((n-1,100)) 
    
       
    pl.figure(figsize=(8,8))
    ax = pl.gca()  # se definen los ejes de la grafica
    
    #### se ponen los ejes centrados 
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.spines['bottom'].set_position(('data',0))
    ax.yaxis.set_ticks_position('left')
    ax.spines['left'].set_position(('data',0))    
    
    # gráfica de los puntos

    
    pl.plot(p[:,0],p[:,1],"ro",label="Aproximación por metodo")

    for i in range(n-1): # n-1 cantidad de ecuaciones 
        lim = linspace(p[i,0],p[i+1,0],100)
        
        eccs.append(form)
        for j,k in enumerate(lim):
            
            for l in range(4): # 4 coeficientes
                splines[i,j] += C[(i*4)+l]*k**(3-l) 
                
            
        pl.plot(lim,splines[i],"r-")
        
    pl.legend()
    pl.show()