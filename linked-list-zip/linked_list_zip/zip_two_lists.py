from  linked_list_zip.linked_list import LinkedList

def zip_Lists(first,second):
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


# if __name__ == "__main__":
#     first  = LinkedList()
#     first.append(1)
#     first.append(3)
#     first.append(2)
#     first.append(10)
#     second = LinkedList()
#     second.append(5)
#     second.append(9)
#     second.append(4)
#     second.append(2)
#     print(first.__str__())
#     print(second.__str__())
#     zip_Lists(first, second)
#     print(first.__str__())

