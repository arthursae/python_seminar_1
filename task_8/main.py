# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
#
# *Пример:*
#
# 3 2 4 -> yes
# 3 2 1 -> no


def check_if_data_is_in_range(data):
    k = data['k']
    sq = data['m'] * data['n']

    r1 = range(data['n'], sq + 1, data['n'])
    r2 = range(data['m'], sq + 1, data['m'])

    return k in r1 or k in r2


def validate_user_input(data, char):
    is_valid = True
    try:
        data = int(data)
    except ValueError:
        is_valid = False
    except:
        is_valid = False
    if is_valid:
        return data
    else:
        print('Некорректный ввод!')
        return validate_user_input(get_user_input('Введите число ' + char + ': '), char)


def get_user_input(message):
    num = input(message)
    return num


i = 0
data = {'n': int,
        'm': int,
        'k': int}
for key in data:
    raw_input = get_user_input('Введите число ' + key + ': ')
    valid_input = validate_user_input(raw_input, key)
    data[key] = int(valid_input)
    i += 1


for key in data:
    print(data[key], end=" ")
print('-> yes') if check_if_data_is_in_range(data) else print('-> no')
