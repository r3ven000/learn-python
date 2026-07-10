'''
Task: "Robust Habit Score"
Goal: Improve your function and handle different input types.

    Input: Get a value from the user.
    Validation:
        Check if the input is a digit (use .isdigit()).
        If not a digit, return "Error: Please enter a whole number".
    Function Logic (calculate_score):
        tasks >= 3 — "Perfect!"
        tasks == 1 or 2 — "Good!"
        tasks == 0 — "Orange day!" (use elif for this).
Any other numeric case (like negative numbers) — "Wrong number".
'''
def calculate_score(tasks):
    if tasks >= 3: 
        return 'Perfect day!'
    elif tasks == 1 or tasks == 2:
        return 'good job!'
    else:
        return "bad. Don't break the chain tomorrow! "
    
track = int(input('enter num do tasks: '))

print(calculate_score(track))
