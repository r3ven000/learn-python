uniq_users = set()

while True:
    manager = input("""
добавить - добавить нового уникального пользователя
конец - выйти из программы

: """)
    if manager == 'конец':
        print(uniq_users)
        break

    elif manager == 'добавить':
        name_user = input('введите как зовут пользователя: ')
        uniq_users.add(name_user)
        set(uniq_users)
        print(uniq_users)

    elif manager != 'добавить' or 'конец':
        print('ошибка, такой команды нет! попробуй еще')


