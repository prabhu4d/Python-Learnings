def findReciprocal(value):
    try:
        print("value ",value)
        r = 1/value
        print("reciprocal of",value,"is",r)

    except ValueError:
        print("You got value error")
    except ZeroDivisionError:
        print("You got zero division error")
    except:
        print("Handling all other errors")

findReciprocal(10)