import random
import string
from collections import Counter
from typing import List, Tuple, Dict

alphabets = string.ascii_uppercase
randomized_alpabets = random.sample(alphabets, k=len(alphabets))
mapping: Dict[str, str] = {key: value for (
    key, value) in zip(alphabets, randomized_alpabets)}
hint_words = 5  # reveal the most common words as hint


def convert(value: str) -> str:
    return mapping[value.capitalize()] if value.isalpha() else value


def add_hints(word_count: Counter) -> str:
    word_count.pop(' ')  # removing the space count
    hints: List[Tuple[str, int]] = word_count.most_common()[:hint_words]
    return ','.join([f'{hint[0].capitalize()}->{mapping[hint[0].capitalize()]}' for hint in hints])


with open("orgi.txt") as src:
    text = src.read()
    word_count = Counter(text)
    with open('encrpt.txt', 'w') as dest:
        dest.truncate()
        dest.seek(0)
        for value in text:
            dest.write(convert(value))
        dest.write('\n\n')
        dest.write('-'*50)
        dest.write('\nHINTS:\n')
        dest.write(add_hints(word_count))
