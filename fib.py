limite = int(input('number limit~> '))

n = 1
t = 0
s = 0

lista = []

while(n<=limite):
    t = n
    n = n + s
    s = t
    
    lista.append(t)

print(lista)