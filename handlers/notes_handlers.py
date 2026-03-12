from utils.decorators import input_error


@input_error
def add_note(args, manager):
    text = " ".join(args)
    manager.add(text)

    return "Note added."