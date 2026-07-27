numbers = []
while True:
    uniq_num = input('enter uniq num(or exit): ')
    if uniq_num == 'exit':
        break
    if uniq_num not in numbers:
        numbers.append(uniq_num)
        print(f'num uniq and add! list: {numbers}')
    else:
        print('num no uniq!')
