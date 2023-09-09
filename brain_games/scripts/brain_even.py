#!/usr/bin/env python3
import random
from .game import runGame


title = "Answer 'yes' if the number is even, otherwise answer 'no'"


def is_even(num):
    return num % 2 == 0


def get_round_data():
    number = random.randint(0, 22)
    question = str(number)
    answer = 'yes' if is_even(number) else 'no'

    return (
      question,
      answer,
    )


def main():
    runGame(title, get_round_data)


if __name__ == '__main__':
    main()
