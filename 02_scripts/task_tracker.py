tasks = []
while True:
    choise = input("добавь задачу (добавить) либо выйти (выйти): ")
    if choise == 'выйти':
        break
    elif choise == 'добавить':
        task = input('напиши имя задачи: ')
        tasks.append(task)
        for dask, item in enumerate(tasks):
            print(f"{dask}: {item}")
    else:
        print("ошибка! команда не найдена, попробуй еще раз!")

