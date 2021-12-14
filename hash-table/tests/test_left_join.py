from hash_table.hashmap_left_join.hash_left_join import left_join
from hash_table.hash_table import HashTable
import pytest


def test_left_join(synonym,antonyms):
    assert left_join(synonym,antonyms)  == [['guide', 'usher', 'follow'], ['outift', 'garb', None], ['wrath', 'anger', 'delight'], ['diligent', 'employed', 'idle'], ['fond', 'enamored', 'averse']]

def test_left_join_first_hashmap_none(antonyms):
    synonym = None
    assert left_join(synonym,antonyms)  == []

def test_left_join_all_none(synonym):
    antonyms = HashTable()
    antonyms.add("fon","averse")
    antonyms.add("wrth","delight")
    antonyms.add("diigent","idle")
    antonyms.add("gide","follow")
    antonyms.add("fow","jam")
    
    assert left_join(synonym,antonyms)  == [['guide', 'usher', None], ['outift', 'garb', None], ['wrath', 'anger', None], ['diligent', 'employed', None], ['fond', 'enamored', None]]
    
@pytest.fixture
def synonym():
    synonym = HashTable()
    synonym.add("fond","enamored")
    synonym.add("wrath","anger")
    synonym.add("diligent","employed")
    synonym.add("outift","garb")
    synonym.add("guide","usher")
    
    return synonym

@pytest.fixture
def antonyms():
    antonyms = HashTable()
    antonyms.add("fond","averse")
    antonyms.add("wrath","delight")
    antonyms.add("diligent","idle")
    antonyms.add("guide","follow")
    antonyms.add("flow","jam")


    return antonyms

