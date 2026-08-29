def F(n):
    if n ==0: 
        return 0
    elif (n==1 or n == 2):
        return 1
    else:
        return F(n-1)+F(n-2)

n = int(input())
for i in range(0, n+1,1):
    print(F(i),end=" ")
print(F(n))