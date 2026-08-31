while True:
    a = float(input())
    if 0 <= a <= 10:
        break

if a >= 9.0: print("VERY TOXIC")
elif a < 5.0: print("SAFE")
else: print("TOXIC")