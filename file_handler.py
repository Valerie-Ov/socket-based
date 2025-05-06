def get_file_contents():
    """
    Func reads and returns text (traceroute log) from the file to the server
    :return: traceroute log (text)
    """
    try:
        with open("traceroute.log", 'r') as f:
            return f.read()
    except FileNotFoundError:
        raise FileNotFoundError("File can't be found.")
    except PermissionError:
        raise PermissionError("You don't have the permissions to read its content")
