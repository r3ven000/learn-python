'''
Task: Order Processing System
1. Collect user prices using a 'while' loop until 'stop' is entered.
2. Store the prices in a list.
3. Create a function 'process_orders' to:
   - Iterate through the list using a 'for' loop.
   - Stop calculation if the price is 999 (break).
   - Sum only positive prices (> 0).
4. Print the final total.
'''
def process_orders(orders_list):
    total = 0
    for order in orders_list:
        if order in orders_list:
            if order == 999:
                break
            if order > 0:
                total += order
    return total

my_orders = []
while True:
    list_user = input('enter price(or stop): ')
    if list_user == 'stop':
        break
    price = int(list_user)
    my_orders.append(price)
result = process_orders(my_orders)
print(f'total: {result}')
