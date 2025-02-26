def maximum_wealth(accounts):
    newArr = []
    for i in range(len(accounts)):
        newArr.append(sum(accounts[i]))
    return max(newArr)


accounts = [[2,8,7],[7,1,3],[1,9,5]]
print(maximum_wealth(accounts))
