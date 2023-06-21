from functions import get_todos, write_todos
import time

now = time.strftime("%b %d, %Y")
print(f"Today is {now}")
while True:
    user_action = input("type add, show, edit, complete or exit: ")
    user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]
        with open('todos', 'a') as file:
            file.write(todo + "\n")

    elif user_action.startswith("show"):
        todos = get_todos()
        for index, item in enumerate(todos):
            print(f'{index+1}--{item}', end='')

    elif user_action.startswith("edit"):
        try:
            edit_index = int(user_action[5:])
            new_todo = input("Enter a new todo: ")
            todos = get_todos()
            todos[edit_index-1] = new_todo + "\n"
            write_todos(todos)
        except ValueError:
            print("enter a valid command. For Example -> edit 5 or edit 1")
            continue

    elif user_action.startswith("completed"):
        try:
            completed = int(user_action[10:])
            todos = get_todos()
            todos.pop(completed-1)
            write_todos(todos)
        except ValueError:
            print("enter a valid command. For Example -> completed 5 or completed 1")
            continue
        except IndexError:
            print(f'no item at index {user_action[10:]}')
            continue

    elif user_action.startswith("exit"):
        break
