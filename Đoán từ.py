secret_word = "Python"
guess = ""
guess_count = 0
guess_limit = 3
print("Gợi ý: Một ngôn ngữ lập trình đơn giản và dễ học")

while guess != secret_word:
    if guess_count < guess_limit:
        guess = input("Từ của bạn là gì?")
        guess_count += 1
    else:
        print("Rất tiếc bạn đã hết cơ hội")
        break
if guess == secret_word: print("Chúc mừng, bạn đã đoán đúng")