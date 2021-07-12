#Dynamic Programming approach

dp = [0] * 201  #number of ways to get sum = i
dp[0] = 1 #1 way of getting sum = 0
coins = [1,2,5,10,20,50,100,200] #coin list

for coin in coins:
    for i in range(0,201):
        if i-coin >=0: #stop index error
            dp[i] += dp[i-coin] #add new ways

print(dp[200])
