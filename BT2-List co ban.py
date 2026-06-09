#Lấy input
hoc_sinh = input("Liệt kê 5 học sinh trong lớp của bạn \nVui lòng nhập dưới dạng A,B,C,D,E ").split(",")

diem_so = input("Nhập lần lượt điểm của 5 học sinh đó với cú pháp tương tự: ").split(",")

hoc_sinh_changeable = hoc_sinh.copy()

hoc_sinh.extend(diem_so)
print(f"Các học sinh bạn nhập là: {hoc_sinh}, với phần sau là điểm tương ứng")

list_moi = input("Nhập thêm 1 học sinh nữa: ")
hoc_sinh_changeable.append(list_moi)

print(hoc_sinh_changeable)

print(f"Số điểm 8 trong list điểm là: {diem_so.count("8")}")