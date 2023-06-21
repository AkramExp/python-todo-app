import streamlit as st
from functions import get_todos, write_todos

todos = get_todos()


def add_todo():
    todo = st.session_state["new_item"] + '\n'
    todos.append(todo)
    write_todos(todos)


st.title("My Todo App")
st.write('This is an app to remind you of pending works')

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label='', on_change=add_todo, key="new_item")
