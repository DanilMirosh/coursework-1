import random

encrypted_word = ["code", "bit", "list", "soul", "next"]

morse_code = {
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "!": "-.-.--",
    "-": "-....-",
    "/": "-..-.",
    "@": ".--.-.",
    "(": "-.--.",
    ")": "-.--.-"
}

answers = []


def morse_encode(word):
    """
    Функция, переводит слова на английском языке в последовательность тире и точек.
    :param word:
    :return:
    """
    result = []
    for letter in word:
        result.append(morse_code[letter])
    return ' '.join(result)


# проверим что функция работает
# print(morse_encode('letter'))

def get_word():
    """
    Функцию, которая получает случайное слово из списка
    :return:
    """
    return random.choice(encrypted_word)


# проверим что функция работает
# print(get_word())
# print(get_word())
# print(get_word())

def print_statistics():
    print(f'Всего задачек: {len(answers)}')
    print(f'Отвечено верно: {answers.count(True)}')
    print(f'Отвечено неверно: {answers.count(False)}')


def main():
    input('Сегодня мы потренируемся расшифровывать морзянку.\n'
          'Нажмите Enter и начнем')

    for round in range(1, 6):
        word = get_word()

        is_correct = word == input(f'Слово {round} {morse_encode(word)}\n').lower()
        if is_correct:
            print(f'Верно, {word.title()}')
        else:
            print(f'Неверно, {word.title()}')

        answers.append(is_correct)

    print_statistics()


main()
