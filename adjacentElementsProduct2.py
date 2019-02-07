def adjacentElementsProduct(inputArray):
     
    tamanho = len(inputArray)
    maior = 0

    for i in range(tamanho - 1):
        num = inputArray[i] * inputArray[i+1]
        if(num > maior):
            maior = num
    
    return maior

array = [1, 2, 3, 0]

print(adjacentElementsProduct(array))