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



