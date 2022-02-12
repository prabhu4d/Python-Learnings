"""
    Bubble Sort
        checking current and current+1 element
        larger element go to last index

    Ref:
        Telusko > https://youtu.be/Vca808JTbI8
"""

def bubble(arr):
    l = len(arr)
    for i in range(l-1,0,-1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


def printArray(arr):
    result = '  '
    for i in range(len(arr)):
        result += str(arr[i])+"  "
    print(result)

def printArrow(arr, i,j):
    keySpace = '  '
    currentSpace = '  '
    for k in range(j):
        keySpace += str(arr[k])+"  "
    for k in range(i):
        currentSpace += str(arr[k])+"  "

    currentSpace = len(currentSpace)
    keySpace = len(keySpace) - currentSpace
    print(" "*currentSpace+"\u2B06"+" "*keySpace+"\u2B06")
    print(" "*currentSpace+"C"+" "*keySpace+"K")

def printTitle(arr, l):
    print("\n"+"*"*100+"\n"+"*"+" "*98+"*")
    print("*"+" "*44+"BUBBLE SORT"+" "*43+"*")
    print("*"+" "*98+"*")
    print("*"+"  DETAILS"+" "*89+"*")
    print("*"+"  "+"-"*26+" "*70+"*")
    arr_string = ''
    for i in arr:
        arr_string += str(i)
    blank = 100 - (14 + len(arr_string) + (l-1)*2)
    print("*  Array = {}".format(arr)+" "*blank+"*")
    blank = 100 - (13 + len(str(l)))
    print("*  Length = {}".format(l)+" "*blank+"*")
    print("*"+" "*98+"*"+"\n"+"*"*100)

def bubbleExplain(arr):
    l = len(arr)
    printTitle(arr, l)
    for i in range(l-1,0,-1):
        print("\n\n\n\n ========================== ITERATION {} ===========================".format(l-i))
        for j in range(i):
            printArray(arr)
            printArrow(arr,j,j+1)
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
        print("\nResult : \n", arr)
    return arr


a = [60, 10, 15, 80, 30, 25]
#print(bubble(a))
print(bubbleExplain(a))