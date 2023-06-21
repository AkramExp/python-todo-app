def get_todos():
    """ Read a text file and return a list of to-do items. """
    with open('todos', 'r') as local_file:
        return local_file.readlines()

def write_todos(edited_todos):
    """ Take list of items as parameter and add it to the to-do items. """
    with open('todos', 'w') as local_file:
        local_file.writelines(edited_todos)
