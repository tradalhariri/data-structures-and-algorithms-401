
from stack_and_queue.stack_queue_animal_shelter.stack_queue_animal_shelter import AnimalShelter,Cat,Dog,Animal

import pytest

def test_anima_shelter_can_enqueue():
    animal_shelter = AnimalShelter()
    animal_shelter.enqueue(Cat("cat1"))
    assert f"Front --> {{{'Cat(cat1)'}}} --> NULL" == animal_shelter.__str__()

def test_anima_shelter_can_enqueue_multiple(animal_shelter):
    assert f"Front --> {{{'Cat(cat-1)'}}} --> {{{'Dog(dog-1)'}}} --> NULL" == animal_shelter.__str__()

def test_animal_shelter_can_dequeue_in_order():
    animal_shelter = AnimalShelter()
    animal_shelter.enqueue(Cat("alesa"))
    animal_shelter.enqueue(Dog("jhon"))
    animal_shelter.enqueue(Cat("soso"))
    animal_shelter.enqueue(Dog("fofo"))
    val = animal_shelter.dequeue('dog')
    assert val.name == 'jhon'


def test_animal_shelter_be_empty_after_multiple_dequeue(animal_shelter):
    animal_shelter.dequeue('dog')
    animal_shelter.dequeue('cat')
    # animal_shelter.dequeue('dog')
    assert animal_shelter.is_empty() == True

def test_animal_shelter_instatiate_empty_queue():
    animal_shelter = AnimalShelter()
    assert animal_shelter.is_empty() == True


def test_can_raise_exception_when_dequeue_empty_animal_shelter():
    animal_shelter = AnimalShelter()
    with pytest.raises(Exception):
        animal_shelter.dequeue('cat')

       
@pytest.fixture
def animal_shelter():
    animal_shelter = AnimalShelter()
    animal_shelter.enqueue(Cat("cat-1"))
    animal_shelter.enqueue(Dog("dog-1"))
    return animal_shelter