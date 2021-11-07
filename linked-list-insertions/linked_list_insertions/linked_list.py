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

        

    def append(self,value):
        newNode = Node(value)
        current = self.head
        while(current!=None):
            if current.next == None:
                current.next = newNode
                return
            current = current.next
        self.head = newNode

    def insertBefore(self,value,newValue):
        newNode = Node(newValue)
        current = self.head
        while current != None:
            if self.head.value == value:
                self.insert(newValue)
                return
            if current.next.value == value:
                newNode.next = current.next
                current.next = newNode
                return
            current = current.next
        raise  Exception("Sorry, The value you want to insert before is not exist in the linked list")

    def insertAfter(self,value,newValue):
        newNode = Node(newValue)
        current = self.head
        while current != None:
            if current.value == value:
                newNode.next = current.next
                current.next = newNode
                return
            current = current.next
        
        raise  Exception("Sorry, The value you want to insert after is not exist in the linked list")

    def deleteNode(self,value):
        current = self.head
        if self.head.value == value:
            self.head = self.head.next
            return
        while current.next != None:
            previous = current
            if previous.next.value == value:
                node = previous.next
                previous.next = previous.next.next
                node = None
                return
            
            current = current.next
        
        raise  Exception("Sorry, The value you want to delete  is not exist in the linked list")


    def getCollection(self):
        current = self.head
        collection = []
        while current!=None:
            collection.append(current.value)
            current = current.next
        return collection
        

if __name__ == "__main__":
    # ll = LinkedList()
    # ll.insert(5)
    # ll.insert(7)
    # ll.insert(12)
    ll = LinkedList()
    ll.insert(1)
    ll.append(3)
    ll.append(8)
    ll.insert(9) 
    ll.append(5)
    ll.insertBefore(5, 18)
    print(ll.__str__())
    # print (ll.getCollection())



