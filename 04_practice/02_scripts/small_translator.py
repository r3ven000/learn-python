words = {
    'hello':'привет',
    'bye':'пока',
    'apple':'яблоко',
    'pear':'груша'
}

while True:
    manager = input("""
перевести - перевести слово с английского языка
конец - выйти из программы

: """)
    if manager == 'конец':
        break

    elif manager == 'перевести':
        eng_word = input('введите слово: ') 
        ru_word = words.get(eng_word)
        print(f'{eng_word} - {ru_word}')

    elif manager != 'перевести' or 'конец':
        print('ошибка, такой команды нет! попробуй еще')


