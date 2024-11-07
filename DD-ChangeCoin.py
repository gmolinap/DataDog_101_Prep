def coinChange(self, coins, amount):
    """
    :type coins: List[int]
    :type amount: int
    :rtype: int
    """

    # Top Down DP (Memorization)

    memo = {0:0} #Set our dic with base case 0

    def min_coins(amt):
        if amt in memo: 
            print("memo", memo)
            return memo[amt] # every single memo, we don't want recursive if we know the min # is
            
        minn = float('inf')
        for coin in coins:
            print("coin", coin)
            diff = amt - coin #making our amnt - our coin
            print("diff", diff)
            if diff < 0: #getting more negative if we dont break
                break
            minn = min(minn, 1+ min_coins(diff)) #1 bc using a coin + min # coins to make the diff
        memo[amt] = minn
        return minn
        

    
    result = min_coins(amount) #min amount in targ amount

    if result < float('inf'):  #result can b inf, this explains the condition
        return result
    else:
        return -1


# Ejemplo de uso
coins = [1, 2, 5]
amount = 11

print(coinChange(coins, amount)) # Output 3
