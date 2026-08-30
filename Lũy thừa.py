def Pow(a,b):
    result = 1
    for i in range(b):
        result = result * a
    return result
a,b = map(int, input().split())
print(Pow(a,b))