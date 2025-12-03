def get_input_file(filename: str) -> str:
    """
    Reads the content of the specified file and returns it as a string.

    :param filename: The name or path of the file to be read.
    :type filename: str
    :return: The contents of the file as a string.
    :rtype: str
    """
    with open(file=filename, mode="r") as file:
        result = file.read()

    return result
