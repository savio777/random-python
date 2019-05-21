num = int(input('numero limite~> '))

i = 0

lista = []

while(i <= num):
    if((i!=1)and((i==2)or(i==3)or(i==5)or(i==7)or(i==11))):
        lista.append(i)
    if((i!=1)and((i%2<i)and(i%2!=0))and((i%3<i)and(i%3!=0))and((i%5<i)and(i%5!=0))
        and((i%7<i)and(i%7!=0))and((i%11<i)and(i%11!=0))):
        lista.append(i)
    i += 1

print(lista)