# CLI calculator program

def addition(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return num1 * num2

def division(num1, num2):
    return num1 / num2

print("Выбирите операцию.")
print("1. Сложение")
print("2. Вычитание")
print("3. Умножение")
print("4. Деление")

choice = int(input("Выбирите вариант(1/2/3/4): "))

num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))

if choice == 1:
    print(num1, "+", num2, "=", addition(num1, num2))

elif choice == 2:
    print(num1, "-", num2, "=", subtraction(num1, num2))

elif choice == 3:
    print(num1, "*", num2, "=", multiplication(num1, num2))

elif choice == 4:
    print(num1, "/", num2, "=", division(num1, num2))
else:
    print("Invalid input")