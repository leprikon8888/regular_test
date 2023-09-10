import re

# Напишіть регулярний вираз, який знаходитиме в тексті фрагменти, що складаються з однієї літери R, за якою слідує одна або більше літер b, за якою одна r. Враховувати верхній та нижній регістр.
txt = ' jkhwfkwRl jkeq brjbc oi hwd KJGHE Wn vdcoskhiskaghdf n Rbr kl;msdfnkph Rbbbbr do;sfjkhcnds as E '
pattern = r'Rb+r'
matches = re.findall(pattern, txt)
print(matches)

# Task 2
# Напишіть функцію, яка виконує валідацію номера банківської картки (9999-9999-9999-9999).
def validation(cart):
    pattern = r'^\d{4}-\d{4}-\d{4}-\d{4}$'
    if re.match(pattern, cart):
        return True
    else:
        return False

cart = input('input cart number: ')
if validation(cart):
    print('validaciya uspeshna')
else:
    print('4to-to poshlo ne tak')


# Task 3
# Напишіть функцію, яка приймає рядкові дані та виконує перевірку на їхню відповідність мейлу.
# Вимоги:
# -Цифри (0-9).
# -лише латинські літери у великому (A-Z) та малому (a-z) регістрах.
# -у тілі мейла допустимі лише символи "_" і "-". Але вони не можуть бути першим символом мейлу.
# -Символ "-" не може повторюватися.
def email_validate(your_mail):
    pattern = r'^[A-Za-z0-9_]+[-]?[A-Za-z0-9_]*@[A-Za-z0-9]+\.[A-Za-z]{2,4}$'

    if re.match(pattern, your_mail):
        return True
    else:
        return False


your_mail = input('enter your email: ')
if email_validate(your_mail):
    print(f"{your_mail} - good email")
else:
    print(f"{your_mail} - bad email")


# Task 4
# Напишіть функцію, яка перевіряє правильність логіну. Правильний логін – рядок від 2 до 10 символів, що містить лише літери та цифри.
def login_validate(login):
    pattern = r'^[A-Za-z0-9]{2,10}$'
    if re.match(pattern, login):
        return True
    else:
        return False


login = input('enter your login: ')
if login_validate(login):
    print(f"{login} - norm login")
else:
    print(f"{login} - bad login")
