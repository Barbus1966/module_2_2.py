number_list = input("Привет, укажите три числа через пробел: ").split()
number_ = ''.join(number_list)                                          #слияние символов в строке
number_2 = number_.isdigit()                                            #проверка на цифры в строке
if len(number_list) != 3 or number_2 == False:
    print("Ошибка")
else:
    first = (number_list[0])
    second = (number_list[1])
    third = (number_list[2])
    if first == second and second == third:
        print("Количество совпадений: 3")
    elif first == second or second == third or first == third:
        print("Количество совпадений: 2")
    else:
        print("Количество совпадений: 0")


