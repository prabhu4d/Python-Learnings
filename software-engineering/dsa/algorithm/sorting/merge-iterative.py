"""

    array = [1,5,2,8,5,7,8,3]

    n = 8

curr_size = 1,   [1] [5] [2] [8] [5] [7] [4] [3]

curr_size = 2,    [1, 5]  [2, 8]   [5, 7]  [3, 4]

curr_size = 4    [1, 2, 5, 8]      [3, 4, 5, 7]

curr_size = 8       [1, 2, 3, 4, 5, 5, 7, 8]

    Ref:
        https://youtu.be/TQbP8s0MKJA

"""

def mergesort(array, n):
    currSize = 1
    while currSize < n-1:
        leftStart = 0
        while leftStart < n-1:
            middle = min(leftStart+currSize-1, n-1)
            rightEnd = min(leftStart+2*currSize - 1, n-1)
            merge(array, leftStart, middle, rightEnd)
            leftStart += 2*currSize
        currSize = 2*currSize
    return array


def merge(array, left, middle, right):
    n1 = middle - left + 1
    n2 = right - middle
    LeftArray = []
    RightArray = []

    for i in range(n1):
        LeftArray.append(array[left+i])
    for j in range(n2):
        RightArray.append(array[middle+1+j])

    i = j = 0
    k = left
    while i<n1 and j<n2:
        if LeftArray[i] <=RightArray[j]:
            array[k] = LeftArray[i]
            i += 1
        else:
            array[k] = RightArray[j]
            j += 1
        k += 1
    while i<n1:
        array[k] = LeftArray[i]
        i += 1
        k += 1
    while j<n2:
        array[k] = RightArray[j]
        j += 1
        k += 1


a = [6,5,4,10,3,2]
l = len(a)
print(mergesort(a,l))