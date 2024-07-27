def check_email(address):
    address_ok = False
    address.lower().strip(' ')  # удалим начальные и конечные пробелы
    if address.find(' ') < 0:  # В адресе нет пробелов
        if address.count('@') == 1:  # ровно один амперсанд
            amp_pos = address.find('@')
                    # Найдём самое последнее вхождение какого-нибудь провильного окончания адреса
            tail_pos = max(list(map(address.rfind, right_tails)))
            if address[tail_pos:] in right_tails:  # Это окончание стоит в самом конце адреса
                if amp_pos > 0 and tail_pos - amp_pos > 1:  # @ - не первый символ в строке и между @ и окончанием хотя бы один знак
                    address_ok = True
    return address_ok


def send_email(message, recipient, sender='university.help@gmail.com'):
    if (check_email(recipient) and check_email(sender)):        # Оба адреса правильны
        if recipient != sender:         # адреса различаются
            if sender == 'university.help@gmail.com':
                print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
            else:   # "Адреса одинаковы"
                print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")
        else:
            print("Нельзя отправить письмо самому себе!")
    else:
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}.")

    return


right_tails = [".com", ".ru", ".net"]

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')

