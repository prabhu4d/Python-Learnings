"""
else part only works if break in for loop

"""

nums = [1, 21, 23, 44, 34]

for num in nums:
    if(num % 5 == 0):
        print(num)
        break
else:
    print("Not Found")
