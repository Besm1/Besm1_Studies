def check_email(address):
    # Функция  проверяет правильность адреса eMail
    address_ok = False
    address = address.lower().strip(' ')  # удалим начальные и конечные пробелы
    if ' ' not in address:  # В адресе нет пробелов
        if address.count('@') == 1:  # ровно один амперсанд
            if address.endswith(tuple(right_tails)): # address[tail_pos:] in right_tails:  # Это окончание стоит в самом конце адреса
                amp_pos = address.find('@')
                tail_pos = max(list(map(address.rfind, right_tails)))
                if amp_pos > 0 and tail_pos - amp_pos > 1:  # @ - не первый символ в строке и между @ и окончанием хотя бы один знак
                    address_ok = True
    return address_ok


def send_email(message, recipient, sender='university.help@gmail.com'):
    # Функция пытается "отправить" письмо и сообщает  результат попытки
    if (check_email(recipient) and check_email(sender)):        # Оба адреса правильны
        if recipient != sender:         # адреса различаются
            if sender == 'university.help@gmail.com':
                print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
            else:
                print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")
        else: # "Адреса одинаковы"
            print("Нельзя отправить письмо самому себе!")
    else:
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}.")

    return


right_tails = [".com", ".ru", ".net"]

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.COM')
send_email('Это сообщение для проверки связи', 'vasyok1337@.COM')
send_email('Это сообщение для проверки связи', '@gmail.COM')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
