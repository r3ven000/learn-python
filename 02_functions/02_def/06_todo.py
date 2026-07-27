#imports
import pyfiglet
import os
import time
welcome = pyfiglet.figlet_format('POMOTRACK')

todo_list = []

#todo function
def manage_tasks(todo):
    while True:
        def get_terminal_width():
            return os.get_terminal_size().columns
        width = get_terminal_width()
        print("""
    Interactive todo list manager.
    
    Commands:
    - task: Add a new task
    - del <index>: Delete task at index
    - edit <index>: Edit task at index
    - exit: Return to main menu
        """.center(width))

        multi_task = input('task / del / edit / exit : '.center(width)).strip()
        
        parts = multi_task.split()
        if not parts:
            continue
        command = parts[0].lower()

        if command == 'exit':
            break

        elif command == 'del':

            if len(parts) > 1:
                try:
                    idx = int(parts[1])
                    if 0 <= idx < len(todo):
                        todo.pop(idx)
                    else:
                        print('invalid index'.center(width))
                except ValueError:
                    print('please enter a valid number'.center(width))

        elif command == 'edit':
            try:
                if len(parts) > 1:
                    idx = int(parts[1])
                    new_text_task = input('enter new text task: ')
                    todo[idx] = new_text_task
                else:
                    print('invalid index'.center(width))
            except IndexError:
                print('please enter a valid number')

        elif command == 'add':
            new_task = input('enter task: ').strip()
            if new_task:
                todo.append(new_task)
            else:
                print('task cannot be empty'.center(width))  
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
    end_time = time.time() + (minutes * 60)
    while time.time() < end_time:
        remaining = end_time - time.time()
        mins, secs = divmod(int(remaining), 60)
        timer_str = f'remaining: {mins:02d}:{secs:02d}'
        print(timer_str.center(width), end='\r')
        time.sleep(0.1)
    print("time's up".center(width))

work_time = 25
break_time = 5
def pomodoro(todo, width):
    print('starting work session...'.center(width))
    timer(work_time, width)
    print('starting break...'.center(get_terminal_width))
    timer(break_time, width)
manager = {
    't': manage_tasks,
    'p': pomodoro
}
width = os.get_terminal_size().columns

for line in welcome.split('\n'):
    if line.strip():
        print(line.center(width))
while True:
    width = os.get_terminal_size().columns
    print(""" 
   pomodoro timer                                        p
   to-do                                                 t
   quit                                                  q
""".center(width))

    manage_inp = input('enter a letter: ').strip()
    if manage_inp == 'q':
        break
    action = manager.get(manage_inp)
    if action:
        action(manage_tasks)
    else:
        print('command not found!'.center(width))
print(welcome)



