"""
    Insertion sort
        the array is seperated as unsorted and sorted

        4,1,5,0,2,7

        -> 4 || 1, 5, 0, 2, 7
        -> 1, 4 || 5, 0, 2, 7
        -> 1, 4, 5 || 0, 2, 7
        -> 0, 1, 4, 5 || 2, 7
        -> 0, 1, 2, 4, 5 || 7
        -> 0, 1, 2, 4, 5, 7

        time complexity O(n^2)
        space complexity O(1) 

    Ref:
        https://youtu.be/i-SKeOcBwko

"""

### ------------------INSERTION SORT IMPLEMENTATION -------------------- ###

def insertion(arr):
    l = len(arr)
    for i in range(1,l):
        for j in range(i-1,-1,-1):
            if arr[j] > arr[i]:
                temp = arr[j]
                arr[j] = arr[i]
                arr[i] = temp
                i -= 1
            else:
                break
    return arr


### ---------------- PRINTING WORKING OF INSERTION SORT ------------------ ###

def printArray(arr):
    result = '  '
    for i in range(len(arr)):
        result += str(arr[i])+"  "
    print(result)

def printArrow(arr, i,j):
    keySpace = '  '
    currentSpace = '  '
    for k in range(i):
        keySpace += str(arr[k])+"  "
    for k in range(j):
        currentSpace += str(arr[k])+"  "

    currentSpace = len(currentSpace)
    keySpace = len(keySpace) - currentSpace
    print(" "*currentSpace+"\u2B06"+" "*keySpace+"\u2B06")
    print(" "*currentSpace+"C"+" "*keySpace+"K")

def printTitle(arr, l):
    print("\n"+"*"*100+"\n"+"*"+" "*98+"*")
    print("*"+" "*42+"INSERTION SORT"+" "*42+"*")
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


def insertionExplain(arr):
    l = len(arr)
    printTitle(arr, l)
    for i in range(1,l):
        print("\n\n\n\n ========================== ITERATION {} ===========================".format(i))
        print("\n   KEY --> {}\n".format(arr[i]))
        for j in range(i-1,-1,-1):
            if arr[j] > arr[i]:
                printArray(arr)
                printArrow(arr,i,j)
                temp = arr[j]
                arr[j] = arr[i]
                arr[i] = temp
                i -= 1
            else:
                break
        print("\n >>>> Result : ")
        printArray(arr)
        
    print("\n\nCompleted <..."+"\n")
    return arr


a = [100,90,80,70,60,50,-1,1000,500,-100,100]
#print(insertion(a))
print("\t",insertionExplain(a))