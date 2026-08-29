def Giaithua(n):
    if n == 0:
        return 1
    else:
        return n*Giaithua(n-1)
x = int(input())
print(Giaithua(x))