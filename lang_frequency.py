import argparse
import re
from collections import Counter


def get_console_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'file_path',
        help='path to a text file'
    )
    args = parser.parse_args()
    return args


def load_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as text_file:
        file_content = text_file.read()
    return file_content


def get_most_frequent_words(text, print_length):
    lower_text = text.lower()
    words_list = re.findall(r'\b\w+\b', lower_text)
    frequent_words_with_amount = Counter(words_list).most_common(print_length)
    return frequent_words_with_amount


def print_most_frequent_words(words):
    print('Most frequent words in descending order:')
    words_for_print = ', '.join(words)
    print(words_for_print + '.')


if __name__ == '__main__':
    WORDS_FOR_PRINT_NUMBER = 10
    console_arguments = get_console_arguments()
    user_file_path = console_arguments.file_path
    try:
        file_text = load_data(user_file_path)
    except FileNotFoundError:
        exit('Can not find the text file.')
    frequent_words_amount = get_most_frequent_words(file_text, WORDS_FOR_PRINT_NUMBER)
    frequent_words, words_amount = zip(*frequent_words_amount)
    print_most_frequent_words(frequent_words)
