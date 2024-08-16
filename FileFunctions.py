# Code require to read / write the TODOs

# Open file and fetch the todo list
TODO_FILE = 'todos.txt'


def read_todos():
    contents = []
    with open(TODO_FILE, 'r') as my_file:
        file_contents = my_file.read().split('\n')
        for line in file_contents:
            if len(line) > 0:
                contents.append(line)

    return contents


def write_todos(todo_list):
    with open(TODO_FILE, 'w') as my_file:
        new_list = []
        for item in todo_list:
            new_list.append(item + '\n')
        my_file.writelines(new_list)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    write_todos(['HELLO!'])
    print(read_todos())
