# Create a simple grahpical task list editor
from FileFunctions import read_todos, write_todos

menu = 'Enter a commnad: View, Edit, Add, Complete, Exit: '
command = ''
task_list = ''

while True:
    command = input(menu).strip('\n')
    match command.upper():
        case 'VIEW' | 'V':
            task_list = read_todos()
            for index, task in enumerate(task_list):
                print(f"{index + 1}:  {task}")
        case 'ADD' | 'A':
            new_task = input("Enter the new task: ")
            task_list = read_todos()
            task_list.append(new_task)
            write_todos(task_list)
        case 'EDIT' | 'E':
            index = int(input("Enter the task number to edit: "))
            edited_task = input(f"Enter the edited task for: \n {task_list[index - 1]}\nNew Task: ")
            task_list[index - 1] = edited_task
            write_todos(task_list)
        case 'COMPLETE' | 'C':
            index = int(input("Enter the task number to complete: "))
            task_list.remove(task_list[index - 1])
            write_todos(task_list)
        case 'EXIT' | 'X':
            break

print("Goodbye")
