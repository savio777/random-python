# -*- coding: utf-8 -*-
# https://www.somatematica.com.br/fundam/regra3s.php

print('identifique se a relação da regra de 3 simples é inversa ou proporcional, e monte a tabela com os valores')
relacao = int(input('(1)inversa, (2)proporcional~> '))

''' 
    x1 => x2
    x3 => x4
'''

print('\n0 se o valor for x\n')


print('valores da parte de cima da tabela:')

x1 = float(input('primeiro valor~> '))
x2 = float(input('segundo valor~> '))

print('\nvalores da parte de baixo da tabela:')

x3 = float(input('terceiro valor~> '))
x4 = float(input('quarto valor~> '))

x = 0.0

# relação proporcional

if(relacao == 2):
    if(x1 == 0.0):
        x = (x2 * x3) / x4
    elif(x2 == 0.0):
        x = (x1 * x4) / x3
    elif(x3 == 0.0):
        x = (x1 * x4) / x2
    elif(x4 == 0.0):
        x = (x3 * x2) / x1
    

# fazer relação inversa 



if(relacao == 1):
    if(x1 == 0.0):
        x = (x3 * x4) / x2
    elif(x2 == 0.0):
        x = (x3 * x4) / x1
    elif(x3 == 0.0):
        x = (x1 * x2) / x4
    elif(x4 == 0.0):
        x = (x1 * x2) / x3 


print(x)