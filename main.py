# Create a simple grahpical task list editor
from FileFunctions import read_todos, write_todos
import FreeSimpleGUI as gui
import time
import os

if not(os.path.exists('todos.txt')):
    with open('todos.txt','w') as file:
        pass

gui.theme('Purple')
task_label = gui.Text('Type in a task')
task_text = gui.InputText(tooltip="Enter Task", key='task')
add_button = gui.Button( 'Add')
task_list = gui.Listbox(read_todos(), key='task_list', enable_events=True,size=[45,10])
edit_button = gui.Button('Edit')
complete_button = gui.Button('Complete')
exit_button = gui.Button('Exit')
time_label = gui.Text(time.strftime('%A %B %d, %Y %I:%M:%S %p'), key='clock')

window = gui.Window('My Task List',
                    layout= [[time_label],
                             [task_label],
                             [task_text, add_button],
                             [task_list, edit_button,complete_button],
                             [exit_button]],
                    font=('Helvetica', 20))

while True:
    event, values = window.read( timeout=500)
    #print(1,event)
    #print(2, values)
    #print(3, values['task_list'])
    window['clock'].update(value = time.strftime('%A %B %d, %Y %I:%M:%S %p'))
    match event:
        case 'Add':
            list = read_todos()
            list.append(values['task'] + '\n')
            write_todos(list)
            window['task_list'].update(values=list)
        case 'Complete':
            try:
                list = read_todos()
                list.remove(values['task_list'][0])
                write_todos(list)
                window['task_list'].update(values=list)
                window['task'].update('')
            except IndexError:
                gui.popup('Pleae select a task', title='Error', font=('Helvetica', 20))
        case 'Edit':
            try:
                list = read_todos()
                new_task = values['task']
                index = list.index(values['task_list'][0])
                list[index] = new_task +'\n'
                write_todos(list)
                window['task'].update('')
                window['task_list'].update(values=list)
            except IndexError:
                gui.popup('Pleae select a task', title='Error', font=('Helvetica', 20))
        case 'task_list':
            window['task'].update(value=values['task_list'][0])
        case 'Exit':
            break


'''
while True:

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
'''
print("Goodbye")
