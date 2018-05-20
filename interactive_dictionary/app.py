from interactive_dictionary import DICTIONARY
from difflib import get_close_matches


def check_word(word):
    closest_match = get_close_matches(word, DICTIONARY.keys(), 1)
    if len(closest_match):
        return closest_match[0]


def explain(word):
    """
    provides an explanation for a given word from the DICTIONARY.
    :param word: string of the word
    :return: explanation
    """

    word = word.strip().lower()

    explanation = DICTIONARY.get(word, DICTIONARY.get(word.capitalize(), DICTIONARY.get(word.upper())))

    if explanation:
        return "\n".join(explanation)

    else:
        suggestion = check_word(word)
        if suggestion:
            user_is_ok = input("do you mean {} ? (y/n) ".format(suggestion))
            if user_is_ok.lower() == "y":
                return explain(suggestion)
        return "The word you entered does not exist, please check it!"


def main():
    continu = True
    while continu:
        word = input("Enter a word: ")
        print(explain(word))

        if input("do you want to proceed ? y/n ") is "n":
            print("see you next time, bye!")
            continu = False


if __name__ == '__main__':
    main()
