"""Exercise 4.4-4.5: Let the world know you have written your last bug."""

def last_bug():
    """Write a nice message enclosed by lines and pipes that clearly indicate you have written your last bug.

    The function should print out the following three lines in the console:

    .. code-block:: console

        ------------------------------
        | I have written my last bug |
        ------------------------------
    """
    # TODO: Code has been removed from here. 


def nice_sign(msg : str):
    """Print the input string as a nice sign by enclosing it with pipes.

    Note that the input message can vary in length.

    .. code-block:: console

        ---------------
        | {input msg} |
        ---------------

    :param msg: The message to enclose.
    """
    # You can use len(msg) to get the number of characters and "-"*10 to repeat a character (try in the console!)
    # TODO: Code has been removed from here. 


if __name__ == "__main__":
    # here you can try out your functions
    last_bug()  # Done with the bugs
    nice_sign("Hello world")
