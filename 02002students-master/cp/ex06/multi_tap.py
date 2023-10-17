"""Exercise 6.9: Multi-tap."""


def multi_tap(keys: list, times: list) -> str:
    """Return the string corresponding to the multi-tap key presses.

    :param keys: The list of keys pressed.
    :param times: The list of times of when the keys were pressed.
    :return: The string corresponding to the key presses.
    """
    # TODO: Code has been removed from here.
    i = 0
    word_list = {
        0: [" "],
        2: ["A", "B", "C"],
        3: ["D", "E", "F"],
        4: ["G", "H", "I"],
        5: ["J", "K", "L"],
        6: ["M", "N", "O"],
        7: ["P", "Q", "R", "S"],
        8: ["T", "U", "V"],
        9: ["W", "X", "Y", "Z"],
    }
    word = []
    x = 0
    while i < len(times):
        x = 0
        if i == len(keys) - 1:
            key_pressed = keys[i]
            list_letters = word_list[key_pressed]
            word.append(list_letters[0])
            i = i + 1
            continue
        if times[i + 1] - times[i] >= 0.5:
            i = i + 1
            key_pressed = keys[i]
            list_letters = word_list[key_pressed]
            word.append(list_letters[0])
            continue
        elif keys[i] == keys[i + 1]:
            t = i
            while True:
                if t == len(keys) - 1:
                    break
                elif times[t + 1] - times[t] >= 0.5:
                    break
                elif keys[t] == keys[t + 1]:
                    x += 1
                    t += 1
                else:
                    break
        while i < len(keys):
            # for index, data in enumerate(keys):
            data = keys[i]
            for key, value in word_list.items():
                if key == data:
                    # key_pressed = data
                    # list_letters = word_list[data]
                    j = value[x]
                    word.append(j)
                    # index = index + x
                    i = i + x + 1
                    break
            break
    word = "".join(word)
    return word


if __name__ == "__main__":
    keys = [4, 4, 4, 0, 2, 6, 0, 4, 4, 2, 7, 7, 9, 9, 9]
    times = (
        [
            0.1,
            0.3,
            0.6,
            1.0,
            1.2,
            1.4,
            1.7,
            2.0,
            2.2,
            2.5,
            2.9,
            3.9,
            4.3,
            4.4,
            4.8,
        ],
    )

    print(
        multi_tap(
            [7, 7, 7, 7, 7, 7, 7, 7, 6, 6, 6, 8, 8, 3],
            [0.1, 0.5, 0.8, 1.2, 2.6, 3.7, 4.1, 4.2, 4.5, 4.9, 5.1, 5.4, 5.6, 5.9],
        ),
    )
