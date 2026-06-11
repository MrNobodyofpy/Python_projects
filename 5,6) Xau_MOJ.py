a,b,c = map(float,input().split())
if a < b + c and b < a + c and c < a + b:
    print("YES")
else: print("NO")