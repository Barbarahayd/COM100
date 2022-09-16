
array = [9, 5, 7, 4, 2, 8, 1, 10, 6, 3]

def mergeSort(array):
    if len(array) < 2:
        return array

middle = len(array) // 2 

left = mergeSort(array[:middle])
right = mergeSort(array[middle:])

def merge(left, right):
    if not len(left):
        return left
    if not len(right):
        return right

    result = []
    leftIndex = 0
    rightIndex = 0
    totalLen = len(left) + len(right)


    while (len(result) < totalLen):

        if left[leftIndex] < right[rightIndex]:
            result.append(left[leftIndex])
            leftIndex += 1
        else:
            result.append(right[rightIndex])
            rightIndex += 1

        if leftIndex == len(left) or \
            rightIndex == len(right):
            result.extend(left[leftIndex:] or right[rightIndex:])

            break

    return result

mergeSort(array)
print(array)

