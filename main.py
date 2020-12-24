"""
Freestyling
Nicholas Johnston
December 23, 2020
"""
import utilities
import random


def freestyle_driver(freestyle_prompts: dict):
    while True:
        word_key = str(random.randint(1, len(freestyle_prompts)))
        prompt = freestyle_prompts[word_key]
        print(prompt)
        input()


def main():
    prompts = utilities.open_prompts()
    freestyle_driver(prompts)


if __name__ == '__main__':
    main()
