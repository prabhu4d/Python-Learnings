"""
    Quick Sort


    Ref:
        Abdul Bari

"""

def partition(array, start, end):
    pivot = array[start]
    low = start+1
    high = end

    while low <= high:
        while low <=high and array[low] <= pivot:
            low += 1
        while low <=high and array[high] >=pivot:
            high -= 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
    array[start], array[high] = array[high], array[start]
    print(array)
    return high


def quickSort(array, start, end):
    if start >= end:
        return
    
    p = partition(array, start, end)
    quickSort(array, start, p)
    quickSort(array, p+1, end)



"""
    * - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - *
    |              VISUALIZATION IN TERMINAL                      |
    * - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - *
 

"""
def Explain(array, start, end):
    array =array
    start = start
    end = end
    def partition(array, start, end):
        pivot = array[start]
        low = start+1
        high = end

        while low <= high:
            while low <=high and array[low] <= pivot:
                low += 1
            while low <=high and array[high] >=pivot:
                high -= 1
            if low <= high:
                array[low], array[high] = array[high], array[low]
        array[start], array[high] = array[high], array[start]
        print(array)
        return high


    def quickSort(array, start, end):
        if start >= end:
            return
        
        p = partition(array, start, end)
        quickSort(array, start, p)
        quickSort(array, p+1, end)



if __name__ == "__main__":
    a = [10,5,0,-100,100,110,90]
    l = len(a)
    quickSort(a,0, l-1)
