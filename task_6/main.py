# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

# *Пример:*

# 385916 -> yes
# 123456 -> no

def calc_sum_of_digits_in_number(data):
    data = int(data)
    sum = 0
    while data > 0:
        n = data % 10
        sum += n
        data = data // 10
    return sum


def check_ticket_is_lucky_as_int(data, length):
    data = int(data)
    dec = 1
    for _ in range(length // 2):
        dec *= 10
    right = data % dec
    left = data // dec % dec
    r = calc_sum_of_digits_in_number(right)
    l = calc_sum_of_digits_in_number(left)
    return r == l


def check_ticket_is_lucky_as_str(data):
    data_len = len(data)
    mid = data_len // 2
    sum_mid = 0
    count = 0
    sum = 0
    for n in data:
        n = int(n)
        sum += n
        if count == mid - 1:
            sum_mid = sum
            sum = 0
        count += 1
    return sum_mid == sum


def validate_user_input(data, length):
    data_len = len(data)
    if data_len == length:
        is_valid = True
        for char in data:
            try:
                char = int(char)
            except ValueError:
                is_valid = False
            except:
                is_valid = False
        if is_valid:
            return data
        else:
            print('Некорректный ввод!')
            return validate_user_input(get_user_input(message), length)
    else:
        print('Некорректный ввод, введите', length, 'цифр!')
        return validate_user_input(get_user_input(message), length)


def get_user_input(message):
    num = input(message)
    return num


length = 6  # NB: set the even number
message = 'Введите ' + str(length) + '-значное число: '
data = get_user_input(message)
number = validate_user_input(data, length)
print(number, '-> yes') if check_ticket_is_lucky_as_str(number) else print(number, '-> no')
print(number, '-> yes') if check_ticket_is_lucky_as_int(number, length) else print(number, '-> no')
