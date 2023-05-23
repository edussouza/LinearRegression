import statistics
import numpy as np
from sympy import Eq
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

c = True

x = [6, 5, 8, 8, 7, 6, 10, 4, 9, 7]
y = [8, 7, 7, 10, 5, 8, 10, 6, 8, 6]

# while c:
#     x.append(float(input("Insira X: ")))
#     y.append(float(input("Insira Y: ")))
#     controle = (input("Desja sair? (S/N)".upper()))
    
#     if controle == "S":
#         c = False

print(x)
print(y)

soma_uxy = 0
soma_ux = 0
soma_uy = 0

i = 0

for i in range(len(x)):
    soma_uxy += x[i] * y[i]         #soma produto X e Y                 
    
soma_ux = sum(x)                    #soma valores X
soma_uy = sum(y)                    #soma valores Y

uxy = soma_uxy/len(x)               #media do produto das duas variaveis
ux = soma_ux/len(x)                 #media das variaveis de X
uy = soma_uy/len(x)                 #media das variaveis de Y
uxuy = ux*uy                        #produto das medias das duas variaveis 
cov = uxy - uxuy                    #covariancia 
xquad = pow(soma_ux, 2)             #soma X elevado ao quadrado
npares = len(x)                     #numero de pares 

r = statistics.correlation(x, y)    #correlação de pearson 
rquad = pow(r, 2)                   #correlação de pearson^2

decimais = int(input("Insira numero de casas decimais: "))

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

xp = np.array(x)
yp = np.array(y)

A = np.vstack([xp, np.ones(len(x))]).T
a, b = np.linalg.lstsq(A, yp, rcond=None)[0]

print("A:", round(a, decimais))
print("B:", round(b, decimais))

print("Equacao da reta: y = {0}x + {1}".format(round(a, decimais), round(b, decimais)))

_ = plt.plot(xp, yp, 'o', label = "Dados Originarios", markersize = 10)
_ = plt.plot(x, a*xp + b, 'r', label = "Reta de Regressão")
_ = plt.legend()
plt.show()