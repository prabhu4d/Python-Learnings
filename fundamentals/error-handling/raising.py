a = int(input("Enter a positive number : "))

try:
    if(a<=0):
        raise ValueError("Not a positive number")

    print("You Entered ",a)

except ValueError as ve:
    print(ve)