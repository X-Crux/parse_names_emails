class ValueError(Exception):
    pass


class NotNameError(Exception):
    pass


class NotEmailError(Exception):
    pass


def check_error(line):
    if len(line) != 3:
        raise ValueError('НЕ присутсвуют все три поля')
    elif not line[0].isalpha():
        raise NotNameError('Поле имени содержит НЕ только буквы')
    elif ('@' or '.') not in line[1]:
        raise NotEmailError('Поле емейл НЕ содержит @ и .(точку)')
    elif int(line[2]) < 10 and int(line[2]) > 99:
        raise ValueError('Поле возраст НЕ является числом от 10 до 99')


def handling_error(exc, line):
    print(f'Поймано исключение {exc}')
    with open('registrations_bad.log', mode='a') as bad_log:
        bad_log.write(line)


with open('registrations.txt', mode='r') as file:
    for line in file:
        line_in_list = line[:-1].split(' ')

        try:
            check_error(line_in_list)
        except ValueError as exc:
            handling_error(exc=exc, line=line)
        except NotNameError as exc:
            handling_error(exc=exc, line=line)
        except NotEmailError as exc:
            handling_error(exc=exc, line=line)
        else:
            print(f'Обработано успешно: {line[:-1]}')
            with open('registrations_good.log', mode='a') as good_log:
                good_log.write(line)
