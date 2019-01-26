# -*- coding: utf-8 -*-

relacao = int(input('(1)inversa, (2)proporcional~> '))

''' 
    x1 => x2
    x3 => x4
'''

print('\n0 se o valor for x')
print('valores da primeira coluna da tabela (valores da esquerda):')

x1 = float(input('primeiro valor~> '))
x2 = float(input('segundo valor~> '))

print('valores da segunda coluna da tabela (valores da direita):')

x3 = float(input('terceiro valor~> '))
x4 = float(input('quarto valor~> '))

x = 0

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
    
print(x)


# fazer relação inversa e testar tudo
#https://www.somatematica.com.br/fundam/regra3s.php