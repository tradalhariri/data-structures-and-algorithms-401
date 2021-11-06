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
            if current.value==value:
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
        

if __name__ == "__main__":
    ll = LinkedList()
    ll.insert(5)
    ll.insert(7)
    ll.insert(12)

    print (ll.getCollection())



