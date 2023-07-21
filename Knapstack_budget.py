
def max_profit(weight,profit,capacity,idx=0):
    if idx == len(weight):
        return 0
    
    elif weight[idx] > capacity:
        return max_profit(weight,profit,capacity,idx+1)
    
    else:
        option1 = max_profit(weight,profit,capacity,idx+1)
        option2 = profit[idx] + max_profit(weight,profit,capacity-weight[idx],idx+1)
        print(option2,end=' ')
        return max(option1,option2)

capacity= 165
weight= [23,31,29,44,53,38,63,85,89,82]
profit= [92,57,49,68,60,43,67,84,87,72]
result = max_profit(weight,profit,capacity)
print(result)
# output= 309

