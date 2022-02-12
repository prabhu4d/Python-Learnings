"""
exit the loop

"""

x = int(input("How many candies you want? "))

avb = 10
i = 1

while i <= x:

    if(i > avb):
        print("\nSorry, Candies are out of stock")
        break

    print("Candy")
    i += 1

print("Thank You")