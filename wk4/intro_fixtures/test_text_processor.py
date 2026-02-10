# test_text_processor.py
import pytest
from text_processor import (
    count_words, 
    capitalize_words, 
    reverse_text,
    get_word_count,
    contains_word,
    find_longest_word,
    filter_short_words,
    save_text_to_file,
    read_text_from_file,
    count_sentences,
    get_average_word_length,
    remove_punctuation
)

#Part 1
@pytest.fixture
def sample_text():
    """Provide sample text for tests"""
    return "the quick brown fox"

def test_count_words(sample_text):
    # TODO: Use the sample_text fixture parameter
    # Assert that count_words returns 4
    result = count_words(sample_text)
    assert result == 4

def test_capitalize_words(sample_text):
    # TODO: Use the sample_text fixture parameter
    result = capitalize_words(sample_text)
    assert result == "The Quick Brown Fox"

def test_reverse_text(sample_text):
    # TODO: Use the sample_text fixture parameter
    result = reverse_text(sample_text)
    assert result == "xof nworb kciuq eht"

#Part 2

@pytest.fixture
def search_word():
    """Provide a word to search for"""
    return "python"

def test_get_word_count(paragraph):
    result = get_word_count(paragraph)
    assert result == {'python': 3, 'is': 3, 'great.': 1, 'powerful.': 1, 'fun.': 1}

def test_contains_word(paragraph, search_word):
    result = contains_word(paragraph, search_word)
    assert result == True

# Part 4: tmp_path tests
def test_save_text_to_file(tmp_path):
    """Test saving text to a file"""
    file_path = tmp_path / "test.txt"
    save_text_to_file("Hello, World!", file_path)
    content = file_path.read_text()
    assert content == "Hello, World!"

def test_read_text_from_file(tmp_path):
    """Test reading text from a file"""
    file_path = tmp_path / "input.txt"
    file_path.write_text("Test content")
    result = read_text_from_file(file_path)
    assert result == "Test content"

# Part 5: Composed fixtures
@pytest.fixture
def greeting():
    """Provide a greeting"""
    return "Hello"

@pytest.fixture
def name():
    """Provide a name"""
    return "Alice"

@pytest.fixture
def full_greeting(greeting, name):
    """Combine greeting and name"""
    return f"{greeting}, {name}!"

def test_full_greeting(full_greeting):
    assert full_greeting == "Hello, Alice!"

# Part 6: Text analysis
@pytest.fixture
def essay():
    """Provide a multi-sentence essay"""
    return "The cat sat. The dog ran. The bird flew."

@pytest.fixture
def simple_sentence():
    """Provide a simple sentence with punctuation"""
    return "Hello, world! How are you?"

@pytest.fixture
def cleaned_text():
    """Provide text without punctuation"""
    return "Hello world How are you"

def test_count_sentences(essay):
    result = count_sentences(essay)
    assert result == 3

def test_get_average_word_length(essay):
    result = get_average_word_length(essay)
    assert round(result, 2) == 3.56

def test_remove_punctuation(simple_sentence, cleaned_text):
    result = remove_punctuation(simple_sentence)
    assert result == cleaned_text

#Part 3
@pytest.fixture
def word_list():
    """Provide a list of words for testing"""
    # TODO: Return a list: ["cat", "elephant", "dog", "butterfly", "ant"]
    animals = ["cat", "elephant", "dog", "butterfly", "ant"]
    return animals

def test_find_longest_word(word_list):
    result = find_longest_word(word_list)
    assert result == "butterfly"

def test_filter_short_words(word_list):
    result = filter_short_words(word_list, 4)
    assert result == ["elephant", "butterfly"]

@pytest.fixture
def paragraph():
    """Provide a longer paragraph for testing"""
    return "Python is great. Python is powerful. Python is fun."









