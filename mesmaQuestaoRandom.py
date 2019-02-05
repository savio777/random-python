contPeriodos = 0

''' 
    False => periodo vazio
    True  => periodo com gente
'''

periodos = {
    0: False,
    1: True,
    2: True,
    3: True,
    4: True 
}

for i in range(0, len(periodos)):
    if periodos[i] == True:
        contPeriodos += 1

contPeriodos += 1

print(contPeriodos)
