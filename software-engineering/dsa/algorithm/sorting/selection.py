"""

    40, 30, 20, 10

length = 4


    Ref:
        Telusko
"""

def selection(arr):
    l = len(arr)
    for i in range(l-1):
        minpos = i
        for j in range(i+1,l):
            if arr[minpos] > arr[j]:
                minpos = j
        arr[i], arr[minpos] = arr[minpos], arr[i]
    return arr

a = [80, 45, 12, 6, 78, 34, 88]
print(selection(a))