#!/usr/bin/env python3
import prompt


def get_user_name():
    user_name = prompt.string('May I have your name? ', True)
    return 'User' if user_name is None else user_name


def main():
    print("Welcome to the Brain Games!")
    user_name = get_user_name()
    print(f'Hello, {user_name}!')


if __name__ == '__main__':
    main()
