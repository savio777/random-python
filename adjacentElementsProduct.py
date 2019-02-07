def adjacentElementsProduct(inputArray):
    tamanho = len(inputArray)
    cont = 0
    i = tamanho - 1
    maior = 0
    aux = 0
    
    while(i >= 0):
        while(cont <= tamanho - 1):
            aux = inputArray[cont]
            if((inputArray[i] * inputArray[cont]) > maior):
                maior = inputArray[i] * inputArray[cont]
            cont += 1
        i -= 1
    return maior
            
array = [3, 6, -2, -5, 7, 3]

print(adjacentElementsProduct(array))