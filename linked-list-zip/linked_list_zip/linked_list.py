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
    
    def kthFromEnd(self,kth):
        """
        This method return the kth node from linked list
        starting from the end.

        input : kth as integer
        output : the value in position kth from
        the end
        """
        if(self.head == None):
            raise Exception(f"Sorry linked list is empty")
            return
        if kth < 0:
            raise Exception(f", The kth {kth} is negative ")
            return    
        current = self.head
        count = 0
        while(current!=None):
            count+=1
            current = current.next
        kthPosition = count - kth  
        current = self.head
        if kthPosition > 0:
            for i in range(kthPosition -1):
                current = current.next
            return current.value
        else:
            raise Exception(f"Sorry, The kth {kth} is out of linked list")
            return
        raise Exception(f", The kth {kth} is  not an integer ")
        return

    def nodeAtMiddle(self):
        count = 0
        current = self.head
        while(current!=None):
            count+=1
            current = current.next
        return self.kthFromEnd(count//2)
    @staticmethod 
    def zipLists(first,second):
        if first.head == None:
            return second
        currentFirst = first.head
        currentSecond = second.head
        while (currentFirst != None):
            if currentSecond !=None:
                
                if currentFirst.next == None:
                    currentFirst.next = currentSecond
                    break

                temp = currentSecond.next
                currentSecond.next = currentFirst.next
                currentFirst.next = currentSecond
                currentSecond = temp
                currentFirst = currentFirst.next.next
            else:
                break
            
                
        return first
                  


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
    print(f"the fourth node from the end is equal {ll.kthFromEnd(3)}")
    print(ll.__str__())


    first  = LinkedList()
    first.append(1)
    first.append(3)
    first.append(2)
    first.append(10)
    second = LinkedList()
    second.append(5)
    second.append(9)
    second.append(4)
    second.append(2)
    # second.append(10)
    # second.append(20)
    third = LinkedList.zipLists(first, second)
    print(third.__str__())
    # print (ll.getCollection())



