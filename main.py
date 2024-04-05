
def read_text_from_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()


if __name__ == "__main__":
    input_filename = "input.txt"
    output_filename = "output.txt"
    top_n = 10

    text = read_text_from_file(input_filename)

