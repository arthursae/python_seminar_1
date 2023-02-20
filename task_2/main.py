# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

def calc_sum_of_digits_as_str(number):
    sum = 0
    for digit in str(number):
        sum += int(digit)
    return sum


def calc_sum_of_digits_as_int(number):
    sum = 0
    while number > 0:
        sum += number % 10
        number = number // 10
    return sum


def validate_user_input(data):
    is_valid = True
    try:
        data = int(data)
    except ValueError:
        is_valid = False
    except:
        is_valid = False
    if is_valid and 99 < data < 1000:  # 100-999
        return data
    else:
        print('Некорректный ввод!')
        return validate_user_input(get_user_input(message))


def get_user_input(message):
    num = input(message)
    return num


message = 'Введите трёхзначное число: '
data = get_user_input(message)
number = validate_user_input(data)
result = calc_sum_of_digits_as_int(number)
print(number, '->', result)
result = calc_sum_of_digits_as_str(number)
print(number, '->', result)
