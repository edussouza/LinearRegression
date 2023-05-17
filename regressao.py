import statistics
import numpy

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
    uxy += x[i] * y[i]
    sux += x[i]
    suy += y[i]

uxy = uxy/len(x)
sux = sux/len(x)
suy = suy/len(x)
uxuy = sux*suy
cov = uxy - uxuy

print(sux)
print(suy)
print(uxuy)
print(cov)

r = statistics.correlation(x, y)
rquad = r^2

decimais = int(input("Insira numero de casas decimais: "))

print(round(r, decimais))

xp = []
yp = []

for i in range(len(x)):
    xp = []


       