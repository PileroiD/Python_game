import random
from typing import Iterable, List

from Game.game_status import GameStatus


class InvalidOperationError(Exception):
    pass


class Gallows:

    def __init__(self, allowed_misses: int = 7):
        if allowed_misses < 5 or allowed_misses > 8:
            raise ValueError('Number of allowed misses should be between 5 and 8.')

        self.__allowed_misses = allowed_misses  # Количество введеных попыток
        self.__tries_counter = 0  # Счетчик попыток
        self.__tried_letters = []  # Возвращает все уже попробованые буквы
        self.__open_indexes = []  # еще не введеные буквы
        self.__game_status = GameStatus.NOT_STARTED  # Показывает статус игры
        self.__word = ''  # Рандомное слово которое выбрал компьютер

    def generate_word(self) -> str:  # Генерация слова
        filename = 'C:\\Python\\Просто для практики\\WordsStockRus.txt'

        words = []

        with open(filename, encoding='utf8') as file:
            for line in file:
                words.append(line.strip('\n'))

        rand_index = random.randint(0, len(words) - 1)
        self.__word = words[rand_index]

        self.__open_indexes = [False for _ in self.__word]
        self.__game_status = GameStatus.IN_PROGRESS

        return self.__word

    def guess_letter(self, letter: str) -> Iterable[str]:
        if self.tries_counter == self.allowed_misses:
            raise InvalidOperationError(f'Exceeded the max misses number. Allowed {self.allowed_misses}')

        if self.game_status != GameStatus.IN_PROGRESS:
            raise IOError(f'inappropriate status of game: {self.game_status}')

        open_any = False
        result: List[str] = []

        for i in range(len(self.word)):
            cur_letter = self.word[i]
            if cur_letter == letter:
                self.__open_indexes[i] = True
                open_any = True

            if self.__open_indexes[i]:
                result.append(cur_letter)
            else:
                result.append('-')

        if not open_any:
            self.__tries_counter += 1

        self.__tried_letters.append(letter)

        if self.__is_winning():
            self.__game_status = GameStatus.WON
        elif self.tries_counter == self.allowed_misses:
            self.__game_status = GameStatus.LOST

        return result

    def __is_winning(self):
        for cur in self.__open_indexes:
            if not cur:
                return False
        return True

    @property
    def game_status(self) -> GameStatus:
        return self.__game_status

    @property
    def word(self):
        return self.__word

    @property
    def allowed_misses(self) -> int:
        return self.__allowed_misses

    @property
    def tries_counter(self) -> int:
        return self.__tries_counter

    @property
    def tried_letters(self) -> Iterable[str]:
        return self.__tried_letters

    @property
    def remaining_tries(self) -> int:
        return self.allowed_misses - self.tries_counter
