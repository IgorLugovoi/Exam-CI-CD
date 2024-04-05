import re
from collections import Counter

def read_text_from_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()


def extract_words(text):
    return re.findall(r'\b\w+\b', text.lower())

def count_word_frequency(words):
    return Counter(words)

def find_top_words(word_count, top_n=10):
    return word_count.most_common(top_n)

def write_top_words_to_file(top_words, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        for word, count in top_words:
            file.write(f"{word}-{count}\n")


if __name__ == "__main__":
    input_filename = "input.txt"
    output_filename = "output.txt"
    top_n = 10

    text = read_text_from_file(input_filename)
    words = extract_words(text)
    word_count = count_word_frequency(words)
    top_words = find_top_words(word_count, top_n)
    write_top_words_to_file(top_words, output_filename)
