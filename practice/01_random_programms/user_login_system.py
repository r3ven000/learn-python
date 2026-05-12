def welcome_program(text):
    print(f'hello  {text}')

name_list = []

while True:
    name = input('enter your name(or done): ')
    if name == 'done':
        break
    else:
        name_list.append(name)

welcome_program(name_list)
