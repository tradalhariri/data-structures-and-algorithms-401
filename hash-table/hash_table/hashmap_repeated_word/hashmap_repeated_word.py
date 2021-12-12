from hash_table.hash_table import HashTable
import re


def repeated_word(sentence):
    if sentence == "":
        return ""
    
    words = re.findall(r'\w+', sentence)
    hash_table = HashTable()
    
    for word in words:
        word  = word.lower()
        if hash_table.contains(word):
            hash_table.add(word,hash_table.get(word)+1)
            return word
        else:
            hash_table.add(word,1)
            
    return ""

if __name__ == "__main__":
    sentence = "Once upon a time, there was a brave princess who..."
    sentence2 = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only..."
    sentence3 = "It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York..."
    
    print(repeated_word(sentence))
    print(repeated_word(sentence2))
    print(repeated_word(sentence3))


            
             
            
    