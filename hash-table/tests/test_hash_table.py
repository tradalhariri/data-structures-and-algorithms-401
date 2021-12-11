from hash_table import __version__


def test_version():
    assert __version__ == '0.1.0'
    
    
    
# from attr import has
from hash_table.hash_table import HashTable
import pytest

@pytest.fixture
def hashtable():
	return HashTable()

def test_hash(hashtable):
	expected = 234
	actual = hashtable._hash("python")
	assert actual == expected
     
def test_get_from_hashtable_when_the_key_dont_exist(hashtable):
	expected = None
	actual =  hashtable.get("tt")
	assert actual == expected

def test_add_key_value():
    hash_table= HashTable()
    hash_table.add('python',401)
    actual=hash_table.get('python')
    expected = 401
    assert actual == expected   
 
def test_get_from_hashtable_when_the_key_exist():
    hash_table= HashTable()
    hash_table.add('python',401)
    actual=hash_table.get('python')
    expected = 401
    assert actual == expected


def test_handle_a_collision_within_the_hashtable():
    hash_table = HashTable()

    hash_table.add('python',401)
    hash_table.add('pyonth',301)
    hash_table.add('thypon',201)
    
    actual = hash_table.get('python')
    expected = 401
    assert actual == expected
    
def test_retrive_value_from_collision_bucket():
    hash_table = HashTable()

    hash_table.add('python',401)
    hash_table.add('pyonth',301)
    hash_table.add('thypon',201)
    
    actual = hash_table.get('python')
    expected = 401
    assert actual == expected
    
    assert hash_table.get('pyonth') == 301
    assert hash_table.get('thypon') == 201
    
    assert hash_table._hash('python') == hash_table._hash('pyonth')
    
def test_result_of_hashing_is_in_range_value():
    hash_table = HashTable()
    
    assert hash_table._hash("asdf") <= len(hash_table.buckets)
    assert hash_table._hash("bnhgytr") <= len(hash_table.buckets)
    assert hash_table._hash("ytrewqaskjhbb") <= len(hash_table.buckets)
    assert hash_table._hash("nnnnnnnnnnnnnnnnnnnn") <= len(hash_table.buckets)





def test_contains():
    hash_table = HashTable()

    hash_table.add('python',401)
    hash_table.add('pyonth',301)
    hash_table.add('thypon',201)
    hash_table.add('java',401)
    hash_table.add('react',301)
    
    assert hash_table.contains('python') == True
    assert hash_table.contains('java') == True
    assert hash_table.contains('c++') == False
    assert hash_table.contains('react') == True
    assert hash_table.contains('c') == False
    
