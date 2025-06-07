user_number = 9  # Допустим, программа хранит цифру 9

while x := int(input()):
    if x == user_number:
        print("Поздравляю! Вы угадали!")
        break
    else:
        print("попробуйте снова")
