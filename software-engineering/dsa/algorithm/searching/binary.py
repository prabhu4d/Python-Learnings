"""

    Binary search
        elements must be sorted in the array

        it finds the mid value and it compare to it key

        l, m, h

        Best Case - O(1)
        Worst Case - O(log(n))

"""

def binarySearch(array, size, key):
    low = 0
    high = size-1
    while(low<=high):
        middle = (low+high)//2
        if(array[middle] == key):
            return middle
        if(array[middle]>key):
            high = middle-1
        else:
            low = middle+1
    return False


array = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
length = len(array)
key = int(input("Enter the Element : "))

result = binarySearch(array, length, key)

if result is False:
    print("Element not found!")
else:
    print("Element found at index ", result)