Word = ['C', 'R', 'A', 'N', 'E']
Guess = str(input("Nhập dự đoán của bạn: ")).upper()
Guess_f = list(Guess)

for i, char in enumerate(Guess_f):
    if char in Word:
        if i < len(Word) and Word[i] == char:
            print("\033[32m" + char + "\033[0m", end="")  # Màu xanh lá (đúng vị trí)
        else:
            print("\033[33m" + char + "\033[0m", end="")  # Màu vàng (sai vị trí)
    else:
        print(char, end="")