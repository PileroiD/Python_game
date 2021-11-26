from Game.Gallows import Gallows
from Game.game_status import GameStatus



def chars_list_to_str(chars):
    return ''.join(chars)


game = Gallows()
word = game.generate_word()

letter_count = len(word)

print(f'The word consists of {letter_count} letters')
print('Try to guess the word letter by letter')

while game.game_status == GameStatus.IN_PROGRESS:
    letter = input('Pick a letter: ')
    state = game.guess_letter(letter)

    print(chars_list_to_str(state))

    print(f'Remaining tries = {game.remaining_tries}')
    print(f'Tried letters: {chars_list_to_str(game.tried_letters)}')


if game.game_status == GameStatus.LOST:
    print('You`re hanged!')
    print(f'The word was: {game.word}')
else:
    print('Congratulations! You won!')

