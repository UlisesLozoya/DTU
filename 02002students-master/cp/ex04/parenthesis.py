"""Exercise 4.6-4.9."""
def matching(expression :str) -> bool:
    """Tell if the parenthesis match in a mathematical expression.

    For instance, the parenthesis match in ``"3x(y-1)(3y+(x-1))"`` but not in ``"3x(y-4))"``

    :param expression: An expression containing zero or more parenthesis.
    :return: ``True`` if the number of open/close parenthesis match, otherwise ``False``
    """
    # TODO: Code has been removed from here. 

def find_innermost_part(s : str) -> str:
    """Find the innermost part of a mathematical expression.

    The innermost part is a substring enclosed in parenthessis but not containing parenthesis.
    For instance, given ``"3(x+(4-y^2))"``, then ``"4-y^2"`` is an inner-most part.
    The parenthesis can be assumed to match.

    :param s: The mathematical expression as a ``str``
    :return: The innermost part as a ``str``
    """
    # TODO: Code has been removed from here. 


def find_index_of_equality(expression : str) -> int:
    """Find an index ``i`` which split the expression into two balanced parts.

    Given an expression containing opening and closing parenthesis, for instance ``"(()())"``, this function should
    return an index ``i``, such that when the string is split at ``i``, the
    number of opening parenthesis ``(`` in the left-hand part equal the number of closing parenthesis ``)`` in the
    right-hand part. For instance, if ``i=2``, the expression is split into the right, left hand parts:

    - ``"(()"``
    - ``"())"``

    In this case the left-hand part contains ``2`` opening parenthesis and the right-hand part ``2`` closing parenthesis so ``i`` is the right index.
    Similarly, for ``"()"``, the answer would be ``1``.

    :param expression: An expression only consisting of opening and closing parenthesis.
    :return: The index ``i`` as an int.
    """
    # TODO: Code has been removed from here. 


def print_the_dialogue(s : str):
    """Print all dialogue in a manuscript.

    Given a manuscript (as a ``str``), this function will find all lines of dialogue to the console, one line of
    dialogue per printed line. Dialogue is enclosed by double ticks, i.e. this ``str`` contains two pieces of dialogue:
    ``"''My dear Mr. Bennet,'' said his lady to him one day, ''have you heard that Netherfield Park is let at last?''"``

    :param s: The manuscript as a ``str``.
    """
    # TODO: Code has been removed from here. 



if __name__ == "__main__":
    # here you can try out your functions
    print("Does the parenthesis match?", matching("2x(x+2)"))
    print("Does the parenthesis match?", matching("2x(x+(2-y)^2)"))
    print("Does the parenthesis match?", matching("4x"))

    print("Does the parenthesis match?", matching("2x(x+2"))
    print("Does the parenthesis match?", matching("2x)(x"))
    print("Does the parenthesis match?", matching("4x()(()))"))

    s = "(())))("

    print("Index of equality for", s, "is", find_index_of_equality(s))
    dialogue = "He said: ''How are you old wife''? She answered, perplexed, ''I am not your wife''"
    print_the_dialogue(dialogue)
