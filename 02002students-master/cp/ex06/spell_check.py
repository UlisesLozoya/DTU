"""Exercise 6.8: Spell check."""


def convert(string):
    text_list = list(string.split(" "))
    return text_list


def spell_check(text: str, corrections: dict) -> str:
    """Return the corrected text for spelling errors according to a set of rules.

    :param text: The sentence to check for spelling.
    :param corrections: The dictionary of wrongly spelled words and their equivalent corrected version.
    :return: The correctly spelled sentence.
    """
    # TODO: Code has been removed from here.
    text_list = convert(text)
    for index, data in enumerate(text_list):
        for key, value in corrections.items():
            if key in data:
                text_list[index] = data.replace(key, corrections[key])
    corrected_text = " ".join(text_list)
    return corrected_text


if __name__ == "__main__":
    # here you can try out your functions
    corrections = {
        "apsolute": "absolute",
        "teh": "the",
        "acess": "access",
        "occured": "occurred",
        "exampel": "example",
        "Teh": "The",
    }
    text = "The apsolute acess to teh, data occured in this exampel."

    print(spell_check(text, corrections))
