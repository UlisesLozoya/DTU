"""Exercise 3.5: Compare numbers."""

def compare_numbers(first_number:int, second_number:int) -> str:
    """Return a string based on which number has the greatest numerical value.

    :param first_number: first number.
    :param second_number: second number.
    :return: string stating which number is the greatest.
    """
    # TODO: Code has been removed from here.
    a = first_number
    b = second_number
    if a > b:
        return "the first number is greater"
    if b > a:
        return "the second number is greater"
    if a == b:
        return "the numbers are equal"


if __name__ == "__main__":
    x = int(input("Enter the first number: "))
    y = int(input("Enter the second number: "))
    print(compare_numbers(x, y))

