myArray = [1, 2, 3, 4]

lengthArray = len(myArray)
isSorted = True

for i in range(lengthArray - 1):
    if myArray[i] > myArray[i + 1]:
        isSorted = False
        break

if isSorted:
    print("The array is sorted in ascending order.")
else:
    print("The array is not sorted in ascending order.")