'''
Task: Expense Tracker with Alert System
- Collect user input until "done".
- Use 'continue' to skip zero values.
- Print an 'Alert' for expenses over 5000.
- Return and display the total sum.
'''
def analyze_expenses(expence_list):
    total_expences = 0
    for expence in expence_list:
        if expence == 0:
            continue
        if expence > 5000:
            print(f'Alert: Large expence found: {expence}')
        total_expences += expence
    return total_expences

full_expence = []

while True:
    value = input('enter expence(or done): ')
    if value == 'done':
        break
    full_expence.append(int(value))

