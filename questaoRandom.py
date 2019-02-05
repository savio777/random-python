contPeriodos = 0

aux = 0

''' 
    False => periodo vazio
    True  => periodo com gente
'''

periodos = [
    False,
    True,
    True,
    True,
    True 
]

for i in range(0, len(periodos) -1):
    periodos[i] = True
    periodos[i+1] = False
    contPeriodos += 1

periodos[len(periodos)-1] = True
contPeriodos += 1

print(periodos, contPeriodos)