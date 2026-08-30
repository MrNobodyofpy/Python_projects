# Giai thừa bằng quy nạp
def Re_fac(a):
    if a == 0: return 1
    for i in range(a):
        return a*Re_fac(a-1)

x = int(input("Nhập số: "))
print(f"Giai thừa quy nạp: {Re_fac(x)}")