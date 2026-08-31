#Import
import math

#Input
a = float(input("Enter the first number: "))

toan_tu = input("Vui lòng chọn toán tử: \nViết '+','-','x' hoặc ':' ")

b = float(input("Enter the second number: "))

def tinh_toan(a,b):
    if toan_tu == "+":
        return a + b
    elif toan_tu == "-":
        return a - b
    elif toan_tu == "x":
        return a * b
    elif toan_tu == ":": 
        return a/b
    else: return print("Toán tử không hợp lệ")

result = tinh_toan(a,b)
print(f"Kết quả: {result}")