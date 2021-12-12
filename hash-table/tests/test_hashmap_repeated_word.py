from hash_table.hashmap_repeated_word.hashmap_repeated_word import repeated_word

def test_hashmap_repeated_word():
    sentence = "Once upon a time, there was a brave princess who..."
    
    assert repeated_word(sentence) == 'a'

def test_hashmap_repeated_word_empty_sentence():
    sentence = ""
    assert repeated_word(sentence) == ''
    
def test_hashmap_repeated_word_upper_and_lower():
    sentence = "Once upon A time, there was a brave princess who..."
    assert repeated_word(sentence) == 'a'











