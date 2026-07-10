def system_edits_documents(user, file, lock):
    if (user == 'is_author'and not lock) or user == 'is_admin':
        return True
    else:
        return False

user_1 = 'guest'
user_2 = 'is_admin'
user_3 = 'is_author'

lock_no = False
lock_yes = True

file = 'sample'

print(system_edits_documents(user_2, file, lock_yes))
