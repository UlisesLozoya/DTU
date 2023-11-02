"""Exercise 8.8: Guessing the language of a text."""


def convert(string):
    text_list = list(string.split(" "))
    text2 = "".join(text_list)
    text3 = text2.replace(".", "")
    text3 = text3.replace(",", "")
    text3 = text3.replace("?", "")
    text3 = text3.replace("!", "")
    # text3 = text3.replace("'", "")
    # text3 = text3.replace("\n", "")
    return text3


def frequency_letter(filename: str, letter: str) -> float:
    """Calculate the frequency of a letter in a text file.
    
    This function takes a text file and a letter as input and calculates the frequency of
    the letter in the text file in percent.
    
    :param filename: A string representing the name of the text file.
    :param letter: A string representing the letter to be searched for.
    :return: A float representing the frequency of the letter in the text file in percent.
    """
    f = open(filename, "r")
    text_as_str = convert(str(f.read()))
    length = len(text_as_str)
    times = text_as_str.lower().count(letter)
    frequency = (times / length) * 100
    f.close()
    return frequency


def language_guess(filename: str) -> str:
    """Guess the language of a text file.

    This function takes a text file as input and guesses the language of the text file
    based on the frequency of the letters 'a' and 'e' in the text file.

    :param filename: A string representing the name of the text file.
    :return: A string representing the guessed language.
    """
    freq_a = round(frequency_letter(filename, "a"), 1)
    freq_e = round(frequency_letter(filename, "e"), 1)
    print
    if (7.2 <= freq_a <= 9.2) and (11.7 <= freq_e <= 13.7):
        return "English"
    elif (5.5 <= freq_a <= 7.5) and (15.1 <= freq_e <= 17.3):
        return "German"
    elif (6.6 <= freq_a <= 8.6) and (13.7 <= freq_e <= 15.7):
        return "French"
    else:
        return "Unknown"


if __name__ == "__main__":
    print(frequency_letter("files/text2.txt", "a"))
    print(frequency_letter("files/text2.txt", "e"))
    print(frequency_letter("files/hamlet.txt", "a"))
    print(language_guess("files/text2.txt"))
