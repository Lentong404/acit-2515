# test_text_processor.py
from text_processor import count_words, capitalize_words, reverse_text

def test_count_words():
    # Setup - repeated in every test!
    sample_text = "the quick brown fox"
    
    result = count_words(sample_text)
    assert result == 4

def test_capitalize_words():
    # Same setup repeated!
    sample_text = "the quick brown fox"
    
    result = capitalize_words(sample_text)
    assert result == "The Quick Brown Fox"

def test_reverse_text():
    # Same setup again!
    sample_text = "the quick brown fox"
    
    result = reverse_text(sample_text)
    assert result == "xof nworb kciuq eht"