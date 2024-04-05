import pytest

from main import *


# Фікстура для підрахунку частоти слів
@pytest.fixture
def sample_words():
    return ['this', 'is', 'a', 'sample', 'text', 'it', 'contains', 'some', 'words', 'sample', 'text', 'for', 'testing']

# Фікстура для Counter об'єкта
@pytest.fixture
def sample_word_count(sample_words):
    return Counter(sample_words)


# Тест для функції count_word_frequency
def test_count_word_frequency(sample_words, sample_word_count):
    assert count_word_frequency(sample_words) == sample_word_count


# Параметризований тест для функції extract_words
@pytest.mark.parametrize("text, expected", [
    ("This is a test text.", ['this', 'is', 'a', 'test', 'text']),
    ("Another example; with punctuation!", ['another', 'example', 'with', 'punctuation']),
])
def test_extract_words(text, expected):
    assert extract_words(text) == expected

# Параметризований тест для функції find_top_words
@pytest.mark.parametrize("word_count, top_n, expected", [
    (Counter(['this', 'is', 'a', 'sample', 'text']), 3, [('this', 1), ('is', 1), ('a', 1)]),
    (Counter(['sample', 'text', 'for', 'testing']), 2, [('sample', 1), ('text', 1)]),
])
def test_find_top_words(word_count, top_n, expected):
    assert find_top_words(word_count, top_n) == expected

# Тест для функції write_top_words_to_file
def test_write_top_words_to_file(tmp_path):
    output_file = tmp_path / "output.txt"
    top_words = [('this', 1), ('is', 1), ('a', 1)]
    write_top_words_to_file(top_words, output_file)

    assert output_file.read_text() == "this-1\nis-1\na-1\n"

