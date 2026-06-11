a, x, b = input().split()
a = float(a)
b = float(b)

match x:
    case "+": print(f"{a+b:.3f}")
    case "-": print(f"{a-b:.3f}")
    case "*": print(f"{a*b:.3f}")
    case "/":
        if b == 0:
            print("ze")
        if b != 0:
            print(f"{a/b:.3f}")