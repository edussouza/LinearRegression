import statistics
import numpy as np

c = True

x = [6, 5, 8, 8, 7, 6, 10, 4, 9, 7]
y = [8, 7, 7, 10, 5, 8, 10, 6, 8, 6]

# while c:
#     x.append(float(input("Insira X: ")))
#     y.append(float(input("Insira Y: ")))
#     controle = (input("Desja sair? (S/N)".upper()))
    
#     if controle == "S":
#         c = False

uxy = 0
sux = 0
suy = 0
i = 0

print(x)
print(y)

for i in range(len(x)):
    uxy += x[i] * y[i]          #soma produto X e Y                 
    sux += x[i]                 #soma valores X
    suy += y[i]                 #soma valores Y

duxy = uxy/len(x)                #media do produto das duas variaveis
dsux = sux/len(x)               #media das variaveis de X
dsuy = suy/len(x)               #media das variaveis de Y
uxuy = dsux*dsuy                #produto das medias das duas variaveis 
cov = duxy - uxuy                #covariancia 

print(sux)
print(suy)
print(duxy)
print(uxy)
print(dsux)
print(dsuy)
print(uxuy)
print(cov)

r = statistics.correlation(x, y)
rquad = pow(r, 2)

decimais = int(input("Insira numero de casas decimais: "))

print(round(r, decimais))

xp = []
yp = []

sisop1 = [[suy, len(x), sux], [uxy, sux, pow(sux, 2)]]
A = np.array(sisop1)

B = np.zeros(2)
X = np.linalg.lstsq(A, B, rcond=None)

solution = X[0]
residual = X[1]

print(solution)






       