import argparse
import re


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


def get_all_words_frequency(text):
    lower_text = text.lower()
    words_list = re.findall(r'\b\w+\b', lower_text)
    all_words_frequency = {}
    for word in words_list:
        if word in all_words_frequency.keys():
            all_words_frequency[word] += 1
            continue
        all_words_frequency[word] = 1
    return all_words_frequency


def get_words_sorted_by_frequency(words_dict):
    frequent_words_list = list(words_dict.keys())
    frequent_words_list.sort(
        key=lambda x: words_dict[x],
        reverse=True
    )
    return frequent_words_list


def print_most_frequent_words(frequent_words, print_length):
    print('Most frequent words in descending order:')
    words_for_print = ', '.join(frequent_words[:print_length])
    print(words_for_print + '.')


if __name__ == '__main__':
    WORDS_FOR_PRINT_NUMBER = 10
    console_arguments = get_console_arguments()
    user_file_path = console_arguments.file_path
    try:
        file_text = load_data(user_file_path)
    except FileNotFoundError:
        exit('Can not find the text file.')
    all_words = get_all_words_frequency(file_text)
    sorted_words = get_words_sorted_by_frequency(all_words)
    print_most_frequent_words(sorted_words, WORDS_FOR_PRINT_NUMBER)
