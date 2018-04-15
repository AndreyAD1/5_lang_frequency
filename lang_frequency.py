import argparse
import re

def load_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as text_file:
        file_content = text_file.read()
    return file_content


def get_most_frequent_words(text):
    lower_text = text.lower()
    words_list = re.findall(r'\b\w{1,}\b', lower_text)
    words_dict = {}
    for word in words_list:
        if word in words_dict.keys():
            words_dict[word] += 1
            continue
        words_dict[word] = 1
    return words_dict


def get_console_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'file_path',
        help='путь к файлу с текстом'
    )
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    console_arguments = get_console_arguments()
    user_file_path = console_arguments.file_path
    try:
        file_text = load_data(user_file_path)
    except FileNotFoundError:
        exit('Не удалось найти файл с текстом.')
    most_frequent_word = get_most_frequent_words(file_text)
    print(most_frequent_word)
