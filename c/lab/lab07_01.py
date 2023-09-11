#OPT(i): the smallest number of coins to make i
#OPT(0) = 0
#OPT(i) = min(OPT(i-d) + 1) for all d in denoms  
#OPT_soln(i):
import numpy as np

def opt_list(coins, target):
    list = np.inf * np.ones(target + 1)
    list[0] = 0
    list[1] = 1
    OPT_soln = {}
    OPT_soln[0] = []
    OPT_soln[1] = [1]
    for i in range(2, target + 1):
        for j in range (len(coins)):
                if list[i] > list[i - coins[j]] + 1:
                    list[i] = list[i - coins[j]] + 1              
                    OPT_soln[i] = OPT_soln[i - coins[j]] + [coins[j]]
    return OPT_soln

# \|/  \|/  \|/
# t-1  t-4  t-5

# At most t+1 calls that don't produce a recursive call
# At most 3(t+1) calls that do produce a recursive call
# Because the functions a recursive call sometimes make calls 
# that don't produce a recursive call, and in total make at most 3(t+1) recursive calles
# so there are <=3(t+1) calles that do not produce a recursive call
# At most 4(t+1) calls in total
# Each call takes 0(len(denom))
# Complexity is O(len(denom) * target)

def make_change(denom, target, memo = {}, solns = {}):
    if target in memo:
        return memo[target]
    if target == 0:
        memo[0] = 0
        solns[0] = []
        return 0
    if target < 0:
        memo[target] = None
        return None
    min_coins = np.inf
    min_soln = None
    for d in denom:
        if target - d >= 0:
            cur_min = make_change(denom, target - d, memo, solns) + 1
        if cur_min < min_coins:
            min_coins = cur_min
            min_soln = solns[target - d] + [d]
    memo[target] = min_coins
    solns[target] = min_soln
    return min_coins

# How many times does the function get called?  
    
if __name__ == '__main__':
    coins = [1 ,4, 5]
    print(opt_list(coins, 11))
    print(make_change(coins, 11))
        