from typing import Callable

from TRUE_OR_FALSE.game_result import GameResult
from TRUE_OR_FALSE.game_status import GameStatus
from TRUE_OR_FALSE.question import Question


class Game:

    def __init__(self, file_path: str, end_of_game_event: Callable, allowed_mistakes: int):

        if allowed_mistakes > 5 or allowed_mistakes < 1:
            raise ValueError(f'Allowed mistakes should be between 1 and 5. You passed: {allowed_mistakes}')

        self.__file_path = file_path
        self.__allowed_mistakes = allowed_mistakes
        self.__end_of_game_event = end_of_game_event
        self.__mistakes = 0
        self.__question = []
        self.__counter = 0
        self.__game_status = GameStatus.IN_PROGRESS

        self.__fill_in_questions(file_path, self.__question)

    @property
    def game_status(self):
        return self.__game_status

    def get_next_question(self):
        return self.__question[self.__counter]

    def is_last_question(self):
        return self.__counter == len(self.__question) - 1

    def give_answer(self, answer):
        pass

        def exceeded_allowed_mistakes():
            return self.__mistakes > self.__allowed_mistakes

        if self.__question[self.__counter].is_true != answer:
            self.__mistakes += 1

        if self.is_last_question() or exceeded_allowed_mistakes():
            self.__game_status = GameStatus.GAME_IS_OVER

            result = GameResult(self.__counter, self.__mistakes, self.__mistakes <= self.__allowed_mistakes)
            self.__end_of_game_event(result)

        self.__counter += 1

    def __fill_in_questions(self, file_path, question):
        with open(file_path, encoding='utf8') as file:
            for line in file:
                q = self.__parse_line(line)
                question.append(q)

    @staticmethod
    def __parse_line(line) -> Question:
        parts = line.split(';')
        text = parts[0]
        is_correct = parts[1] == 'Yes'
        explanation = parts[2]

        return Question(text, is_correct, explanation)
