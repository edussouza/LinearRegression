import statistics
import numpy as np
from sympy import Eq
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

c = True

n = int(input("Quantos pares de dados serão usados? "))

x = []
y = []
c = 0

while c!=n:
    x.append(float(input("Insira X: ")))
    y.append(float(input("Insira Y: ")))
    c = c + 1

print(x)
print(y)

decimais = int(input("Insira numero de casas decimais: "))

soma_uxy = 0
soma_ux = 0
soma_uy = 0

i = 0

for i in range(len(x)):
    soma_uxy += x[i] * y[i]                         #soma produto X e Y                 
    
soma_ux = round(sum(x), decimais)                   #soma valores X
soma_uy = round(sum(y), decimais)                   #soma valores Y

uxy = round(soma_uxy/len(x), decimais)              #media do produto das duas variaveis
ux = round(soma_ux/len(x),decimais)                 #media das variaveis de X
uy = round(soma_uy/len(x), decimais)                #media das variaveis de Y
uxuy = ux*uy                                        #produto das medias das duas variaveis 
cov = uxy - uxuy                                    #covariancia 
xquad = pow(soma_ux, 2)                             #soma X elevado ao quadrado
npares = len(x)                                     #numero de pares 

r = round(statistics.correlation(x, y), decimais)    #correlação de pearson 
rquad = pow(r, 2)                                    #correlação de pearson^2

xp = np.array(x)
yp = np.array(y)                    

print("Soma X:", soma_ux)
print("Soma Y:", soma_uy)
print("Soma XY:", soma_uxy)
print("Soma X^2:", xquad)
print("N (numero de pares):", npares)
print("Coeficiente de correlação de Pearson:", round(r, decimais))
print("Coeficiente de determinação de Pearson:", round(rquad, decimais))
print("-----------------------")
print("Media X:",ux)
print("Media Y:", uy)
print("Media XY:", uxuy)
print("Covariancia:", cov)
print("-----------------------")

A = np.vstack([xp, np.ones(len(x))]).T
a, b = np.linalg.lstsq(A, yp, rcond=None)[0]

print("A:", round(a, decimais))
print("B:", round(b, decimais))

print("Equacao da reta: y = {0}x + {1}".format(round(a, decimais), round(b, decimais)))

_ = plt.plot(xp, yp, 'o', label = "Dados Originarios", markersize = 10)
_ = plt.plot(x, a*xp + b, 'r', label = "Reta de Regressão")
_ = plt.legend()
plt.show()