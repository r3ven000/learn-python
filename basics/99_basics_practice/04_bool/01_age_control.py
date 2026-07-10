def age_control(age):

    if age <= 1:
        return 'ERROR'

    elif age < 18:
        return False
    else:
        return True


contol = int(input('enter your age: '))

age_control(contol)

print(age_control(contol))

