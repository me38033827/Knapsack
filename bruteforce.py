# import time
import copy

def knapsack_bf(weights, values, W):
    if (len(weights)!=len(values)) or len(weights)==0 or len(values)==0 or W==0:
        # print("Invalid input")
        return []

    S =[]
    
    for x in range(len(weights)):
        S.append(-1)

    # start = time.time()
    result = BruteForce(weights, values, W, S)
    # end = time.time()
    
    # print("\n BruteForce: Max values={}, items={}, duration(seconds)={}".format(result[1], result[0],(end-start)*1000))

    return result[1],result[0]

def BruteForce(weights, values, W, S):
    n = len(weights)
    maxValue = maxWeight = 0
    selectedItems = []

    for i in range (2**n):
        totalWeight = totalValue = 0
        j = n-1
        
        while(S[j] !=0 and j >= 0):
            S[j] = 0
            j = j - 1
        
        S[j] = 1

        for k in range (n):
            if(S[k] == 1):
                totalWeight = totalWeight + weights[k]
                totalValue = totalValue + values[k]

        if ((totalValue > maxValue) and (totalWeight <= W)):
            maxValue = totalValue
            maxWeight = totalWeight
            selectedItems = copy.copy(S)

    return (selectedItems,maxValue,maxWeight)


