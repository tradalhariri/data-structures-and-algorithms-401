from stack_and_queue.queue import Queue

def duck_duck_goose(k,*args):
    queue = Queue()
    for person in args:
        queue.enqueue(person)
    while queue.front.next:
        print(queue)
        for i in range(k):
            temp = queue.front.value
            if i == k-1:
                queue.dequeue()
            else :
                queue.dequeue()
          
                queue.enqueue(temp)
    return queue.front.value


if __name__ == "__main__":
    print(duck_duck_goose(3,))