from TRUE_OR_FALSE.game import Game
from TRUE_OR_FALSE.game_result import GameResult
from TRUE_OR_FALSE.game_status import GameStatus


def end_of_game_handler(result: GameResult):
    print(f'Question asked: {result.question_passed}. Mistakes made: {result.mistakes_made}')
    print(f'You won!' if result.won else 'You lost!')


game = Game('data\\Questions.csv', end_of_game_handler, allowed_mistakes=3)

while game.game_status == GameStatus.IN_PROGRESS:

    # if game.is_last_question():
    #     print('no more question')
    #     break

    q = game.get_next_question()
    print('Do you believe in the next statement or question ? Enter "y" or "n" ')

    print(q.text)

    answer = input() == 'y'

    if q.is_true == answer:
        print('Good job! You`re right!')
    else:
        print('Oops, actually you`re mistaken. Here is the explanation:')
        print(q.explanation)

    game.give_answer(answer)
