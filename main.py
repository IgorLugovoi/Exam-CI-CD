import re

def read_text_from_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()


def extract_words(text):
    return re.findall(r'\b\w+\b', text.lower())


if __name__ == "__main__":
    input_filename = "input.txt"
    output_filename = "output.txt"
    top_n = 10

    text = read_text_from_file(input_filename)
    words = extract_words(text)

