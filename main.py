import math
escape = False
print("Вас приветствует калькулятор МПТ")
while escape == False:
    print("Выберите дейтвие, которое хотите выполнить: \n1. Сложение \n2. Вычитание \n3. Умножение \n4. Деление\n5. Степень числа\n6. Квадратный корень числа\n7. Факториал\n8. Синус\n9. Косинус\n10. Тангенс\n0. Выход из программы")
    name = int(input("Выберите действие: "))
    if name == 1:
        while True:
            try:
                num_1 = float(input("Введите первое число: "))
                num_2 = float(input("Введите второе число: "))
            except ValueError:
                print("Введите число корректно!")
                continue
            sum = num_1 + num_2
            print("Сумма: ", sum)
            break
    elif name == 2:
        while True:
            try:
                num_1 = float(input("Введите первое число: "))
                num_2 = float(input("Введите второе число: "))
            except ValueError:
                print("Введите число корректно!")
                continue
            sum = num_1 - num_2
            print("Разность: ", sum)
            break
    elif name == 3:
        while True:
            try:
                num_1 = float(input("Введите первое число: "))
                num_2 = float(input("Введите второе число: "))
            except ValueError:
                print("Введите число корректно!")
                continue
            sum = num_1 * num_2
            print("Произведение: ", sum)
            break
    elif name == 4:
        while True:
            try:
                num_1 = float(input("Введите первое число: "))
                num_2 = float(input("Введите второе число: "))
            except ValueError:
                print("Введите число корректно!")
                continue
            if num_2 == 0:
                print("Ошибка, делить на 0 нельзя!")
                continue
            sum = num_1 / num_2
            print("Частное: ", sum)
            break
    elif name == 5:
        while True:
            try:
                num_1 = float(input("Введите число: "))
                num_2 = float(input("Введите степень, в которую хотите возвести число: "))
            except ValueError:
                print("Введите число корректно!")
                continue
            sum = math.pow(num_1, num_2)
            print(num_1, " в степени ", num_2, " = ", sum)
            break
    elif name == 6:
        while True:
            try:
                num_1 = float(input("Введите число: "))
            except ValueError:
                print("Введите число корректно!")
                continue
            if num_1 < 0:
                print("Ошибка, квадратный корень не может быть отрицательным без мнимой части!")
                continue
            sum = math.sqrt(num_1)
            print("Корень ", num_1, " = ", sum)
            break
    elif name == 7:
        while True:
            try:
                num_1 = int(input("Введите число: "))
            except ValueError:
                print("Введите число корректно!")
                continue
            if num_1 < 0 or num_1 != int(num_1):
                print("Ошибка, факториал применяется только к положительным, целым числам")
                continue
            num = num_1
            sum = 1
            while num_1 > 1:
                sum = sum * num_1
                num_1 = num_1 - 1
            print("Факториал", " = ", sum)
            break
    elif name == 8:
        while True:
            try:
                num_1 = float(input("Введите число: "))
            except ValueError:
                print("Введите число корректно!")
                continue
            sum = math.sin(num_1)
            print("Синус ", num_1, " = ", sum)
            break
    elif name == 9:
        while True:
            try:
                num_1 = float(input("Введите число: "))
            except ValueError:
                print("Введите число корректно!")
                continue
            sum = math.cos(num_1)
            print("Косинус ", num_1, " = ", sum)
            break
    elif name == 10:
        while True:
            try:
                num_1 = float(input("Введите число: "))
            except ValueError:
                print("Введите число корректно!")
                continue
            sum = math.tan(num_1)
            print("Тангенс ", num_1, " = ", sum)
            break
    elif name == 0:
        print("Всего хорошего!")
        escape = True
    elif name != 0 or 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9 or 10:
        print("Ошибка, такого действия не существует")



