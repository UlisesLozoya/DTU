"""Exercise 7.8: Morse code."""


def morse_to_text(morse_code: str) -> str:
    """Return the extracted message from its Morse code.

    :param morse_code: String with the initial message encoded in Morse.
    :return: The decoded message.
    """
    morse_code_dict = {
        ".-": "A",
        "-...": "B",
        "-.-.": "C",
        "-..": "D",
        ".": "E",
        "..-.": "F",
        "--.": "G",
        "....": "H",
        "..": "I",
        ".---": "J",
        "-.-": "K",
        ".-..": "L",
        "--": "M",
        "-.": "N",
        "---": "O",
        ".--.": "P",
        "--.-": "Q",
        ".-.": "R",
        "...": "S",
        "-": "T",
        "..-": "U",
        "...-": "V",
        ".--": "W",
        "-..-": "X",
        "-.--": "Y",
        "--..": "Z",
    }
    morse_to_words = tuple(morse_code.split("  "))
    length_morse = len(morse_to_words)
    i = 0
    phrase = []
    trans_phrase = []
    while i < length_morse:
        word = morse_to_words[i]
        word_list = list(word.split(" "))
        for index, data in enumerate(word_list):
            for key, value in morse_code_dict.items():
                if key == data:
                    word_list[index] = data.replace(key, morse_code_dict[key])
        i = i + 1
        phrase.append(word_list)
    len_phrase = len(phrase)
    t = 0
    while t < len_phrase:
        trans_phrase.append(phrase[t])
        trans_phrase[t] = "".join(trans_phrase[t])
        t += 1
    trans_phrase = " ".join(trans_phrase)
    return str(trans_phrase)


if __name__ == "__main__":
    print(
        morse_to_text(
            "-.. --- - ...  .- -. -..  -.. .- ... .... . ...  - . .-.. .-..  .- -. -.-. .. . -. -  - .- .-.. . ..."
        )
    )
