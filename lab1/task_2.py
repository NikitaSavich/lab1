password = input('Введите пароль: ')
if len(password) < 16:
    print('Пароль слишком короткий')
elif password.isalpha() or password.isdigit():
    print('Содержит только буквы или только цифры')
else:
    print('Надёжный пароль')