"""
    Merge Sort - Divide and Conquer

"""

from typing import Counter


def mergesort(arr):
    length = len(arr)
    if length>1:
        middle = length//2
        left = arr[:middle]
        right = arr[middle:]

        mergesort(left)
        mergesort(right)

        i = j = k =0
        left_len = len(left)
        right_len = len(right)

        while i<left_len and j<right_len:
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        
        while i<left_len:
            arr[k] = left[i]
            i += 1
            k += 1
        
        while j<right_len:
            arr[k] = right[j]
            j += 1
            k += 1
    return arr


def explain():
    def mergesort(arr, l,h):
        if(l<h):
            mid = (l+h)//2
            print("\nlow : "+str(l)+" mid :"+str(mid)+" high : "+str(h))
            print("1. calling left mergesort({}, {})".format(l,mid))
            print(arr[l:mid+1])
            mergesort(arr, l, mid)
            print("2. calling right mergesort({}, {})".format(mid+1,h))
            print(arr[mid+1:h+1])
            mergesort(arr, mid+1, h)

    array = [20,18,16,35,45,56,78,99]
    print("array : ", array)
    mergesort(array,0,len(array)-1)



def mergesortExplain(arr):
    def mergesort(arr, count):
        print("\n\n - - - - - - Call Stack {} - - - - - - - ".format(count))
        print("arr = {}".format(arr))
        length = len(arr)
        print("Length : {}".format(length))
        if length == 1:
            print("   . . . returning to last Call Stack {}".format(count-1))
        if length>1:
            middle = length//2
            left = arr[:middle]
            right = arr[middle:]
            print("Middle : {}\nLeft : {}\nRight : {}".format(middle, left, right))
            
            count += 1
            print(" < < < - - -  Left Merge Sort")
            left_mergeSort = mergesort(left, count)
            print(" returning... [left_mergeSort] : ",left_mergeSort)
            
            count += 1
            print("Right Merge Sort - - - > > >")
            right_mergeSort = mergesort(right,count)
            print("returning... [right_mergeSort] : ",right_mergeSort)

            i = j = k =0
            left_len = len(left)
            right_len = len(right)
            print("\n\n\n + + + + + + + +  MERGING  + + + + + + + + \n")
            print("left({}) : {}  ||  right({}) : {}".format(left_len,left,right_len ,right))

            while i<left_len and j<right_len:
                print("i = {}, j = {}, k = {}".format(i,j,k))
                print("arr -> ",arr)
                if left[i] < right[j]:
                    print("\nleft[{}] < right[{}] --> so arr[{}] = {}".format(i,j,k,left[i]))
                    arr[k] = left[i]
                    i += 1
                else:
                    print("\nright[{}] < left[{}] --> so arr[{}] = {}".format(j,i,k,right[j]))
                    arr[k] = right[j]
                    j += 1
                k += 1
            
            while i<left_len:
                print("i = {}, j = {}, k = {}".format(i,j,k))
                print("Remaining Left : arr[{}] = {}".format(i, left[i]))
                arr[k] = left[i]
                i += 1
                k += 1
            
            while j<right_len:
                print("i = {}, j = {}, k = {}".format(i,j,k))
                print("Remaining Right : arr[{}] = {}".format(j, right[j]))
                arr[k] = right[j]
                j += 1
                k += 1
            print("sorted array : {}".format(arr))
        return arr
    mergesort(arr, 0)


if __name__ == "__main__":
    arr = [3,1,0,5,8,7]
    print(arr)
    print(mergesort(arr))
    #mergesortExplain(arr)
