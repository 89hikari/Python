print("*" * 10, " Анализатор слова ", "*" * 10)
word = input("Введите слово: ")

vowels = 0
consonants = 0

for i in word:
    letter = i.lower()
    # print(letter)
    if letter == "а" or letter == "о" or \
       letter == "и" or letter == "е" or \
       letter == "ё" or letter == "э" or \
       letter == "ы" or letter == "у" or \
       letter == "ю" or letter == "я":
        vowels += 1
    else:
        consonants += 1
print("Длина слова/текста:", len(word))
print("Гласные %i Согласные %i" % (vowels, consonants))
