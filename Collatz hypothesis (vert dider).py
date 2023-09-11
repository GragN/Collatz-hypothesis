# гипотеза коллатца

import matplotlib.pyplot as plt
# pip install matplotlib

number = int(input("Введите положительное число "))
number1 = 0
lis = []
lis1 = []

if number >= 1:
    while (number != 1):
        if number % 2 == 0:
            number = number / 2
            print(number)
            number1 += 1
            lis.append(number)
            lis1.append(number1)
        else:
            number = (number * 3) + 1
            print(number)
            number1 += 1
            lis.append(number)
            lis1.append(number1)
    print(f"Количество итераций {number1}")
    print(f"максимальное значение {max(lis)}")
else:
    print("Введено не корректное число")

plt.plot(tuple(lis1), tuple(lis))
plt.show()
