contPeriodos = 0

''' 
    Como não teve o primeiro período a partir do semestre passado, 
    supondo que todos os outros primeiros períodos sejam formados, 
    em quantos semestres todos os 5 períodos de ads terão turmas formadas?
'''

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
