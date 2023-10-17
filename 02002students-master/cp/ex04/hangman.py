"""Exercise 4.12-4.16."""


def is_word_guessed(secret_word: str, letters_guessed: str) -> bool:
    """Determine if the word has been guessed.

    :param secret_word: The word to guess
    :param letters_guessed: A ``str`` containing the letters that have currently been guessed
    :return: True if and only if all letters in ``secret_word`` have been guessed.
    """
    # TODO: Code has been removed from here.
    sword = secret_word
    lg = letters_guessed
    i = 0
    j = len(sword)
    for element in lg:
        for element2 in sword:
            if element == element2:
                i = i + 1
    if i >= j:
        return True
    else:
        return False


def get_available_letters(letters_guessed: str) -> str:
    """
    Return the letters which are available, i.e. have not been guessed so far.

    The input string represents the letters the user have guessed, and the output should then be the lower-case
    letters which are not contained in that string. The function is used to show the user which
    letters are available in each round.

    :param letters_guessed: A `str` representing the letters the user has already guessed
    :return: A `str` containing the letters the user has not guessed at yet.
    """
    # TODO: Code has been removed from here.
    all_letters = "abcdefghijklmnopqrstuvwxyz"
    remaining_letters = ""
    for char in all_letters:
        if char not in letters_guessed:
            remaining_letters += char
    return remaining_letters


def get_guessed_word(secret_word: str, letters_guessed: str) -> str:
    """Format the secret word for the user by removing letters that have not been guessed yet.

    Given a list of the available letters, the function will replace the letters in the secret word with `'_ '`
    (i.e., a lower-case followed by a space). For instance, if the secret word is ``"cat"``, and the
    available letters are ``"ct"``, then the function should return ``"c_ t"``.

    :param secret_word: A ``str``, the word the user is guessing
    :param letters_guessed:  A ``str`` containing which letters have been guessed so far
    :return: A ``str``, comprised of letters, underscores (_), and spaces that
    represents which letters in secret_word have been guessed so far.
    """
    # TODO: Code has been removed from here.
    letters_not_guessed = get_available_letters(letters_guessed)
    shown = secret_word
    for char in secret_word:
        if char in letters_not_guessed:
            shown = shown.replace(char, "_ ")

    return shown


def hangman(secret_word: str, guesses: int):
    """
    Play an interactive game of Hangman.

    This function should launch an interactive game of Hangman. The details of the game is defined in the
    project description available online, and should be read carefully.

    * The game should first display how many letters are in the secret word. You should start by generating this output.
    * Before each round, the user should see how many guesses that are left and which letters are not yet used
    * In each round, the user is prompted to input a letter. Use the ``input('.')`` function for this.
    * The user is given feedback based on whether the letter is in the word or not. The program also performs error
     handling.
    * The game terminates when the user win, has exceeded the number of guesses, or if the user makes an illegal input.
      in this case the user is shown a score.

    :param secret_word: The secret word to guess, for instance ``"cow"``
    :param guesses: The number of available guesses, for instance ``6``
    """
    # TODO: Code has been removed from here.
    t = len(secret_word)
    all_letters = "abcdefghijklmnopqrstuvwxyz"
    guessed_letters = ""
    print(
        f"Hangman! To save Bob, you must guess a {t} letter word within {guesses} attempts."
    )

    # show1 = "_ " * len(secret_word)
    # print(show1)
    guess_points = guesses
    while guesses > 0:
        print("----")
        print(f"You have {guesses} guesses left.")
        current_points = t * guess_points
        available = get_available_letters(guessed_letters)
        # print(f"he available letters are {available}. Guess a letter and press Enter: ")
        # last_guess = input()
        last_guess = input(
            f"The available letters are: {available}. Guess a letter and press Enter: "
        )
        if len(last_guess) > 1 or last_guess not in all_letters:
            print(f"Game over :-(. Your score is 0 points.")
            break
        guessed_letters += last_guess
        show1 = get_guessed_word(secret_word, guessed_letters)
        i = 0
        win = is_word_guessed(secret_word, guessed_letters)
        if last_guess not in secret_word:
            guesses = guesses - 1
            guess_points = guess_points - 1
            print(f"Oh no: {show1}")
            i = i + 1
            if guesses == 0:
                print(f"Game over :-(. Your score is 0 points.")
                break
        elif last_guess in secret_word:
            if win:
                print(f"Success! You guessed '{secret_word}' in {i} tries")
                print(f"Your score is {current_points}")
                break
            print(f"Good guess: {show1}")
            guesses = guesses - 1
            i = i + 1


if __name__ == "__main__":
    # here you can try out your functions
    print("This should return True: ", is_word_guessed("dog", "tdohg"))
    print("This should return False: ", is_word_guessed("dog", "dthk"))

    print("This should be 'c_ w': ", get_guessed_word("apple", ""))

    print(
        "Available letters when we have tried 'abcdefghijk'; this should be about half the alphabet: ",
        get_available_letters("abcdefghijk"),
    )

    print(
        "Lets launch hangman. Try the inputs in the exercise description and see if you get the same"
    )
    hangman("cow", 4)
