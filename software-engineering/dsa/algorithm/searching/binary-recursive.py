"""
    Binary Search using recursion

"""


def BinarySearch(array, size, key):
    low = 0
    high = size-1

    def recursion(low, high, key):
        if low == high:
            if array[low] == key:
                return low
            else:
                return False
        else:
            middle = (low+high)//2
            if(key == array[middle]):
                return middle
            if(key < array[middle]):
                return recursion(low, middle-1, key)
            else:
                return recursion(middle+1, high, key)

    result = recursion(low, high, key)
    if result != False:
        print("Element found at index ", result)
    else:
        print("Element not found in the array")


array = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50,
         55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
size = len(array)
key = int(input("Enter the Element : "))

BinarySearch(array, size, key)
