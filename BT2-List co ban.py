import math
list = input("Liệt kê 5 bộ phim yêu thích của bạn từ top 1 đến top 5 " \
"\nVui lòng nhập dưới dạng A,B,C,D,E" \
"\nVới A,B,C,D,E lần lượt là tên các phim từ thích nhất đến ít thích nhất ")

usable_list = list.split(",")

print(usable_list)

print("Phim bạn thích nhất là: " + usable_list[0])

print(f"Phim từ top 2 đến top 4 là: {usable_list[1:4]}")

print(f"Phim dưới top 2 là: {usable_list[2:]}")