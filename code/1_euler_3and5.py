# 1) Найдите сумму всех чисел меньше 1000, кратных 3 или 5
count = 0
for i in range(1, 1000):
    if i % 5 == 0 or i % 3 == 0:
        count += i
print(count)
