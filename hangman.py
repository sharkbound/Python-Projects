from random import choice


def random_word(words):
    word = choice(words).lower()
    return frozenset(word), word


HANGMAN = '''
 /--------\\
 |        |
 {}        |
{}{}{}       |
 {}{}       |
          |
============

{}
'''

BODY_PART_COUNT = 6


def main():
    while True:
        play()
        if input('play again? [y/n]: ').lower() != 'y':
            break


def play():
    words = ('game', 'smash', 'python')
    body_parts = ['\\', '/', '\\', '|', '/', 'o']
    body = []
    chars, word = random_word(words)
    guessed = set()
    fails = 0

    while True:
        print_game(guessed, body, word)

        guess = input('\nguess: ')

        if guess in guessed:
            print(f'you already guessed "{guess}"')
        elif guess not in chars:
            print('that letter is not in the word')
            body.append(body_parts.pop())
            fails += 1
        else:
            guessed.add(guess)

        if fails == BODY_PART_COUNT:
            print_game(guessed, body, word)
            print('GAMEOVER\n')
            break

        if guessed == chars:
            print_game(guessed, body, word)
            print('YOU WIN')
            break


def print_game(guessed, body, word):
    if len(body) < BODY_PART_COUNT:
        body = body + [' '] * (BODY_PART_COUNT - len(body))
    print(HANGMAN.format(*body, ' '.join(c if c in guessed else '_' for c in word)))


if __name__ == '__main__':
    main()
