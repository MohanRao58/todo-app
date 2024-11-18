"""we can import functions by
    from functions import get_todos,write_todos
    by using above syntax we can write the name of all functions which were there in functions.py file to access
    this works well when number if functions are less

    import functions
    above syntax is more suitable while working with large code-bases
    but, make sure we have to call functions by accessing function along with method
    like, functions.get_todos()
"""
FILEPATH = 'todos.txt'
def get_todos(filepath = FILEPATH):
    """Read a text file and return the list of
    to-do items."""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg,filepath = FILEPATH):
    """write the to-do items List in the text file."""
    with open(filepath,'w') as file:
        file.writelines(todos_arg)