#imports
import pyfiglet
import os
import time
welcome = pyfiglet.figlet_format('POMITRACK')

todo_list = [0]

#todo function
def create_list(todo):
    while True:
        width = os.get_terminal_size().columns #setting

        multi_task = input('task / del / edit / exit : '.center(width)).strip()
        
        parts = multi_task.split()
        if not parts:
            continue
        command = parts[0].lower()

        if command == 'exit':
            break

        elif command == 'del':

            if len(parts) > 1:

                idx = int(parts[1])
                todo.pop(idx)

        elif command == 'edit':
            if len(parts) > 1:
                idx = int(parts[1])
                new_text_task = input('enter new text task: ')
                todo[idx] = new_text_task
            else:
                todo.append(name_task)
                print("\n" + " TASKS ".center(width, "="))
                has_tasks = False
                for index, task in enumerate(todo):
                    if task != 0:
                        task_str = f'{index}. {task}'
                        print(task_str.center(width))
                        has_tasks = True
                if not has_tasks:
                    print('there are no tasks yet'.center(width))
                print('=' * width + '\n')


def timer(minutes):
    seconds = minutes * 60
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        timer_str = f"Remaining: {mins:02d}:{secs:02d}"
        print(timer_str.center(width), end='\r')
        time.sleep(1)
        seconds -= 1
    print("Time's up".center(width))
def pomidoro(todo):
    timer(25)
    timer(5)
manager = {
    't': create_list,
    'p': pomidoro
}
width = os.get_terminal_size().columns

for line in welcome.split('\n'):
    if line.strip():
        print(line.center(width))
while True:
    width = os.get_terminal_size().columns
    print(""" 
   pomidoro timer                                        p
   to-do                                                 t
""".center(width))

    manage_inp = input('enter your task: ').strip()
    if manage_inp == 'exit':
        break
    action = manager.get(manage_inp)
    if action:
        action(todo_list)
    else:
        print('command not found!'.center(width))
print(welcome)




