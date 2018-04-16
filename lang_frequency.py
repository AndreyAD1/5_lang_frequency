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


def get_most_frequent_words(text, words_count):
    lowered_text = text.lower()
    words_list = re.findall(r'\b\w+\b', lowered_text)
    frequent_words_with_amount = Counter(words_list).most_common(words_count)
    return frequent_words_with_amount


def print_most_frequent_words(words):
    words_for_print = ', '.join(words)
    print(
        'Most frequent words in descending order:\n'
        '{}.'.format(words_for_print)
    )


if __name__ == '__main__':
    number_of_words_for_print = 10
    console_arguments = get_console_arguments()
    user_file_path = console_arguments.file_path
    try:
        file_text = load_data(user_file_path)
    except FileNotFoundError:
        exit('Can not find the text file.')
    frequent_words_amount = get_most_frequent_words(
        file_text,
        number_of_words_for_print
    )
    frequent_words, words_amount = zip(*frequent_words_amount)
    print_most_frequent_words(frequent_words)
