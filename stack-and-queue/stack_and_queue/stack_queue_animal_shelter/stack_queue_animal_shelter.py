from stack_and_queue.node import Node


class AnimalShelter:
    def __init__(self):
        """ initialize AnimalShelter method
        """
        self.front = None
        self.rear = None

    def enqueue(self,animal):
        """ add new animal to the back of the AnimalShelter
        """
        
        
        if animal.type not in ['cat','dog']:
            raise  Exception("only dog and cat can be added")
            return

        new_animal = Node(animal)
        if self.front:
            self.rear.next = new_animal
        else:
            self.front = new_animal
        self.rear = new_animal

    def dequeue(self,ref):
        """ remove animal from the first match type starting from
         the front of the queue and return it
        """
        if self.is_empty():
            raise Exception("Animal Shelter is empty")
        
        temp = self.front
        if temp.value.type == ref:
            self.front = self.front.next
            temp.next = None
            return temp.value
        else:
            previous = temp
            temp = temp.next
            while temp!=None:
                if temp.value.type == ref:
                    previous.next = temp.next
                    temp.next = None
                    return temp.value
                previous = temp
                temp = temp.next
        return None

    def __str__(self):
        """ print queue
        """
        if self.front == None:
            return f"Front --> NULL"
        str_queue = f"Front --> {{{self.front}}}"
        temp = self.front
        while temp.next:
            str_queue+= f" --> {{{temp.next.value}}}"
            temp = temp.next
        str_queue+= f" --> NULL"
        return str_queue



        



    def is_empty(self):
        """ check if the AnimalShelter is empty
        """
        return self.front == None



class Animal:
    def __init__(self):
        self.name = "animal"
        self.type = "any"
    def __str__(self):
        return f"Animal({self.name})"

class Cat(Animal):
    def __init__(self,name):
        self.name = name
        self.type = 'cat'

    def __str__(self):
        return f"Cat({self.name})"

class Dog(Animal):
    def __init__(self,name):
        self.name = name
        self.type = 'dog'

    def __str__(self):
        return f"Dog({self.name})"


if __name__ == "__main__":
    cat1 = Cat("cat-1")
    dog1 = Dog("dog-1")
    cat2 = Cat("cat-2")
    dog2 = Dog("dog-2")
    cat3 = Cat("cat-3")
    dog3 = Dog("dog-3")

    animal_shelter = AnimalShelter()
    animal = Animal()
  
    animal_shelter.enqueue(cat1)
    animal_shelter.enqueue(dog1)
    animal_shelter.enqueue(cat2)
    animal_shelter.enqueue(dog2)
    animal_shelter.enqueue(cat3)
    animal_shelter.enqueue(dog3)
    print(animal_shelter)

    animal_shelter.dequeue('cat')
    animal_shelter.dequeue('dog')
    animal_shelter.dequeue('dog')
    animal_shelter.dequeue('dog')

    animal_shelter.dequeue('cat')
    animal_shelter.dequeue('cat')
    # animal_shelter.dequeue('g')
    print(animal_shelter)
    animal_shelter.enqueue(animal)
    animal_shelter.enqueue(animal)
    print(animal_shelter)


