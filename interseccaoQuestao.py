inputArray = ["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"]
#inputArray = ["1, 3, 4, 7, 13", "2, 15"]

print('input: ', inputArray)

array1 = list(inputArray[0].split(', '))
array2 = list(inputArray[1].split(', '))

for i in range(len(array1)):
    array1[i] = int(array1[i])
    
for j in range(len(array2)):
    array2[j] = int(array2[j])

array1.sort()
array2.sort()

inter = list(set(array1) & set(array2))

for x in range(len(inter)):
    inter[x] = str(inter[x])

if(len(inter) > 0):
    string = ','
    interString = string.join(inter)
    print(interString)
else:
    print('false')
