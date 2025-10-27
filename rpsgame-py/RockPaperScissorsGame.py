# Игра Камень, Ножницы, Бумага

import random

print("Камень, Ножницы, Бумага")

# доступные варианты
options = ["камень", "ножницы", "бумага"]

while True:
    print("Выберите вариант:\n1 - камень\n2 - ножницы\n3 - бумага\n0 - выход")
    
    # выбор игрока
    choice = int(input("Ваш ход: "))
    
    # выход из игры если игрок вводит 0
    if choice == 0:
        print("До свидания!")
        break
    elif choice > 3:
        print("Неверный ввод. Попробуйте снова.")
        continue

    # выбор компьютера
    comp_choice = random.choice(options)
    print("Компьютер выбрал: ", comp_choice)

    # определение победителя
    player_choice_name = ""
    if choice == 1:
        player_choice_name = "камень"
    elif choice == 2:
        player_choice_name = "ножницы"
    elif choice == 3:
        player_choice_name = "бумага"
    
    print("Вы выбрали: ", player_choice_name)
    
    if player_choice_name == comp_choice:
        print("Ничья!")
    elif (player_choice_name == "камень" and comp_choice == "ножницы") or \
         (player_choice_name == "ножницы" and comp_choice == "бумага") or \
         (player_choice_name == "бумага" and comp_choice == "камень"):
        print("Вы выиграли! ", player_choice_name, " побеждает ", comp_choice)
    else:
        print("Вы проиграли! ", comp_choice, " побеждает ", player_choice_name)
