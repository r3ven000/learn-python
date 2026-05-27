print(r"""              _                            _                        
"__      _____| | ___ ___  _ __ ___   ___  (_)_ __"                   
"\ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | | '_ \ "                  
 "\ V  V /  __/ | (_| (_) | | | | | |  __/ | | | | |"                 
 "_\_/\_/ \___|_|\___\___/|_| |_| |_|\___| |_|_|_|_|_ "             _ 
"|  _ \  ___  _ __ ___ (_)_ __   ___ ( )___  |  _ \(_)__________ _| | "
"| | | |/ _ \| '_ ` _ \| | '_ \ / _ \|// __| | |_) | |_  /_  / _` | | "
"| |_| | (_) | | | | | | | | | | (_) | \__ \ |  __/| |/ / / / (_| |_| "
"|____/ \___/|_| |_| |_|_|_| |_|\___/  |___/ |_|   |_/___/___\__,_(_)
""")


print(r"""--.._"
"|  (_)  _ -._"
"|    _ (_)    '-."
"|   (_)   __..-'"
"\\__..--"
""")

pizzas = {
    "Margherita": 3,
    "Pepperoni": 4,
    "Hawaiian": 5,
    "Meat Fest": 4,
    "BBQ Chicken": 4,
    "Vegetarian": 3,
    "Mushroom": 3,
    "Four Seasons": 4
      }
print(pizzas)
print('Hello!')
total_price = 0
while True:
    user_order = input('What exactly do you want to receive from the list above?(or exit) ')
    if user_order == 'exit':
        break
    elif user_order in pizzas:
        result = pizzas[user_order]
        total_price += result
        print(f'price: {total_price}')
    else:
        print('Mistake! Try again')


def free_gift(order):
    if order >= 5:
        print("they will give you free gift!")
    elif order < 5:
        remainder = 5 - order
        print(f"Pay an extra {remainder} to get a free gift!")
        extras = input('will you pay extra remainder? ').upper()
        if extras == 'YES' or extras == 'Y':
            print('Thank you! They will give you free gift !) ')
        elif extras == 'NO' or extras == 'N' :
            print('Okayy...')

free_gift(total_price)
random_number = 3321
import time
def timer(minutes):
    seconds = minutes * 60
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        print(f'remaind: {mins:02d}:{secs:02d}', end='/r')
        time.sleep(1)
        seconds -= 1
        print(random_number)
dog = timer(1)
print(f'your order number: {random_number}, and it will be ready in {dog}')

