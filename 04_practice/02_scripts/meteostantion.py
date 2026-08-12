week_t = (10, 11, 12, 13, 14, 15, 17)

for t in week_t:
    formul_medium_t = sum(week_t) / len(week_t) 
print(f'средняя температура: {int(formul_medium_t)}')
print(f'максимальная температура: {max(week_t)}')
print(f'минимальная температура: {min(week_t)}')
    
