"""


"""

def fractionalKnapSack(Capacity, profit, weight):

    l = len(profit)
    index = list(range(l))
    ratio = [p/w for p, w in zip(profit, weight)]
    index.sort(key=lambda i: ratio[i], reverse=True)
    fractions = [0]*l
    maxProfit = 0

    for i in index:
        if weight[i]<=Capacity:
            fractions[i] = 1
            maxProfit += profit[i]
            Capacity -= weight[i]
        else:
            fractions[i] = Capacity/weight[i]
            maxProfit += profit[i]*(Capacity/weight[i])
            break

    return maxProfit, fractions



if __name__ == "__main__":
    N = int(input("Number of Items : "))
    profit = []
    weight = []
    for i in range(N):
        values = input("Enter {} item profit and weight : ".format(i+1)).split()
        profit.append(int(values[0]))
        weight.append(int(values[1]))
    Capacity = int(input("Enter the Max Capacity : "))
    maxProfit, fractions =  fractionalKnapSack(Capacity, profit, weight)
    print("Max Profit : {}\nFractions : {}".format(maxProfit, fractions))