# Challenge Summary
Write the following methods for the Linked List class:
* append : add new node to the end of the list.
* insert before : insert new node before given node.
* insert after : insert new node after given node.

## Whiteboard Process
![](linked-list-insertions.png)

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
* append:
  walk through the linked list until you reach null then add new node there.
  
  Time O(n)
  space O(1)
* insert before:
    walk through the linked list until you reach the given value then add new node before it.
  

    Time O(n)
    space O(1)
* insert after:
    walk through the linked list until you reach the given value then add new node after it.
    Time O(n)
    space O(1)

## Solution
<!-- Show how to run your code, and examples of it in action -->

````python
def test_append_node_to_the_end():
    ll = LinkedList()
    ll.append(5)
    ll.append(10)
    ll.append(17)
    assert ll.__str__() == "{5} -> {10} -> {17} -> NULL"
```