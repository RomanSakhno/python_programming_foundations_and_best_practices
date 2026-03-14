"""Reusable decorators for wrapping handler functions."""


def input_error(func):
    """Convert common handler exceptions into user-friendly messages."""

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