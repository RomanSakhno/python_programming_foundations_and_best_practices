def input_error(func):

    def inner(*args, **kwargs):

        try:
            return func(*args, **kwargs)

        except ValueError as e:
            return str(e)

        except IndexError:
            return "Enter required arguments."

        except KeyError:
            return "Contact not found."

        except Exception as e:
            return f"Unexpected error: {e}"

    return inner