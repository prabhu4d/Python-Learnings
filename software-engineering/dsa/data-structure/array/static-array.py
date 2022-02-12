# basically python has dynamic array. there is no static array.

array = [1, 2, 3, 4, 5]


# printing the length of the array
print("\nThe Length of the array is "+str(len(array)))

# printing each array
for i in range(5):
    print("Array at index of "+str(i)+" is "+str(array[i]))


# modifying elements
for i in range(5):
    print("Array at "+str(i)+" is : "+str(array[i]))
    modify = input("Do you want to modify (y/n) : ")

    if(modify == 'y' or modify == 'Y'):
        element = int(input("Enter the number : "))
        array[i] = element

print(array)
