def parse_input(user_input: str):

    cmd, *args = user_input.strip().split()

    return cmd.lower(), args