# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
#
# *Пример:*
#
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10
# если получается некорректное разделение - напечатать "Неверное S"


def validate_user_input(data):
    is_valid = True
    try:
        data = int(data)
    except ValueError:
        is_valid = False
    except:
        is_valid = False
    if is_valid:
        return int(data)
    else:
        print('Некорректный ввод!')
        return validate_user_input(get_user_input(message))


def get_user_input(message):
    data = input(message)
    return data


message = 'Введите общее количество S: '
data = get_user_input(message)
number = validate_user_input(data)
if number % 6 == 0:
    a = int(number / 6)
    b = int(4 * a)
    print(number, '->', a, b, a)
else:
    print('Неверное S')