x = int(input())
dp = [-1]*(x+1)
dp[0] = 0
def F(n):
    if (n==1 or n == 2): 
        dp[n] = 1
        return 1
    if dp[n] != -1:
        return dp[n] 
    else: dp[n] = F(n-1) + F(n-2)
    return dp[n]

print(F(x))
print(*dp)