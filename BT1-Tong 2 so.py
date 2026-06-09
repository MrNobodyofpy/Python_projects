#Import
import math

#Input
a = float(input("Enter the first number: "))

toan_tu = input("Vui lòng chọn toán tử: \nViết không dấu, viết hoa chữ đầu tiên ")

b = float(input("Enter the second number: "))

def tinh_toan(a,b):
    if toan_tu == "Cong":
        return a + b
    elif toan_tu == "Tru":
        return a - b
    elif toan_tu == "Nhan":
        return a * b
    elif toan_tu == "Chia": 
        return a/b
    else: return print("Toán tử không hợp lệ")

result = tinh_toan(a,b)
print(f"Kết quả: {result}")