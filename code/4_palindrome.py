# 4) Найдите самый большой палиндром, полученный умножением двух трехзначных чисел
a = 0
c = 0
for i in range(100, 1000):
    for j in range(100, 1000):
        a = i * j
        b = str(a)
        fl = 0
        s = int(len(b))
        qwe = s - 1
        for letter in range(0, s):
            if b[letter] == b[qwe]:
                fl += 1
            qwe -= 1
        if fl == s and int(b) > c:
            c = int(b)
print(c)
print(c)
