

user_win = 0
pc_win = 0

while user_win < 3 and pc_win < 3:
    choise_user = input("Выберите камень, ножницы или бумагу: ")
    choise_pc = random.choice(list)
    print(f"Вы выбрали {choise_user}, компьютер выбрал {choise_pc}")
    if choise_user == choise_pc:
        print("Ничья")
    elif (choise_user == "камень" and choise_pc == "ножницы") or (choise_user == "ножницы" and choise_pc == "бумага") or (choise_user == "бумага" and choise_pc == "камень"):
        print("Человек выиграл")
        user_win += 1
    else:
        print("Компьютер выиграл")
        pc_win += 1

if user_win == 3:
    print("Человек выиграл игру")
else:
    print("Компьютер выиграл игру")
