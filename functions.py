FILEPATH = "../todos.txt"

def get_todos(filepath = "todos.txt"):
    """
    Help file define...
    :param filepath:
    :return:
    """
    with open(filepath) as file:
        todos = file.readlines()
    return todos


def write_todos(todos_arg, filepath = "todos.txt"):
    """
    Help file define...
    :param filepath:
    :return:
    """
    with open(filepath, "w") as file:
        file.writelines(todos_arg)