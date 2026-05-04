'''
Task: Shopping Cart Total
1. Create a list of prices: [100, 250, 50, 400, 120]
2. Use a 'for' loop to iterate through the list.
3. Calculate the total sum of all prices.
4. Print the final result.
'''
price_total = 0
prices = [100, 250, 50, 400, 120]
for price in prices:
    price_total += price
print(f'price: {price_total}')
