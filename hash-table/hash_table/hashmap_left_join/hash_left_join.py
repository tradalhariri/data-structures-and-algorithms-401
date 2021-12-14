from hash_table.hash_table import HashTable

def left_join(synonym ,antonyms):
    if not synonym:
        return [] 
    result = []
    for i in range(len(synonym.buckets)):
        if synonym.buckets[i]:
            synonym_ls = synonym.buckets[i]
            curr = synonym_ls.head
            while curr :
                antonyms_value = None
                if antonyms.contains(curr.value[0]):
                    antonyms_value = antonyms.get(curr.value[0])
                    
                result.append([curr.value[0],curr.value[1],antonyms_value])
                curr = curr.next
    return result


if __name__ == "__main__":
    
    synonym = HashTable()
    synonym.add("fond","enamored")
    synonym.add("wrath","anger")
    synonym.add("diligent","employed")
    synonym.add("outift","garb")
    synonym.add("guide","usher")
    
    antonyms = HashTable()
    antonyms.add("fond","averse")
    antonyms.add("wrath","delight")
    antonyms.add("diligent","idle")
    antonyms.add("guide","follow")
    antonyms.add("flow","jam")
    
    print(left_join(synonym,antonyms))



    


                
                
            
            
            
    
    