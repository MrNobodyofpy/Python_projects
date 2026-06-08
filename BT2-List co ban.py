import math
list = input("Liệt kê 5 học sinh trong lớp của bạn " \
"\nVui lòng nhập dưới dạng A,B,C,D,E ")

hoc_sinh = list.split(",")

list2 = input("Nhập lần lượt điểm của 5 học sinh đó với cú pháp tương tự: ")
diem_so = list2.split(",")

hoc_sinh.extend(diem_so)
print(f"Các học sinh bạn nhập là: {hoc_sinh}, với phần sau là điểm tương ứng")

list_moi = input("Nhập thêm 1 học sinh nữa:")
hoc_sinh.append(list_moi)

print(hoc_sinh)

print(f"Số điểm 8 trong list điểm là: {diem_so.count("8")}")