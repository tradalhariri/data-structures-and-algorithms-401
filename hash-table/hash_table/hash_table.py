class Node:
    def __init__(self,value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self,value):
        newNode = Node(value)
        newNode.next = self.head
        self.head = newNode
        
    def __str__(self):
        current = self.head
        ll_str = ""
        while current!=None:
            ll_str+=f"{{{current.value}}} -> "
            current = current.next
        ll_str+="NULL"
        return ll_str
    
    def include(self,value):
        current = self.head
        while current!=None:
            if current.value == value:
                return True
            current = current.next
        return False

    def getCollection(self):
        current = self.head
        collection = []
        while current!=None:
            collection.append(current.value)
            current = current.next
        return collection
        



class HashTable:
    def __init__(self, size=1024):
        self.size = size
        self.buckets = [None] * size

    def _hash(self, key):
        return sum([ord(char) for char in key]) * 997 % self.size

    def add(self, key, value):
        index = self._hash(key)
        if not self.buckets[index]:
          self.buckets[index] = LinkedList()
          self.buckets[index].insert([key,value])
        else:
            if  self.contains(key):
                linked_list = self.buckets[index]
                current = linked_list.head
                while current:
                    if current.value[0] == key:
                        current.value = [key,value]
                    current = current.next
            else:
                self.buckets[index].insert([key,value])
                    
    def get(self, key):
      index = self._hash(key)
      if self.contains(key):
        linked_list = self.buckets[index]
        current = linked_list.head
        while current:
          if current.value[0] == key:
            return current.value[1]
          current = current.next
      return None
  
    def contains(self,key):
        index = self._hash(key)
        if self.buckets[index]:
            linked_list = self.buckets[index]
            current = linked_list.head
            while current:
                if current.value[0] == key:
                    return True
                current = current.next
        return False


if __name__ == '__main__':
    hash_table = HashTable()
    index = hash_table._hash('python')
    print(index)
    index = hash_table._hash('pyonth')
    print(index)
    
    hash_table.add('python',44)
    hash_table.add('python',55)
    print(hash_table.buckets[hash_table._hash('python')])





