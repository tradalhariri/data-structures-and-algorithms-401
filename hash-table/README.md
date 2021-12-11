# Hashtables
> Hash Table is a data structure which stores data in an associative manner. In a hash table, data is stored in an array format, where each data value has its own unique index value. Access of data becomes very fast if we know the index of the desired data.


## Challenge

* The challenege is to create a hashtable data structure from scratch, the hash table must add a key value pair in the correct index and solve the collision if two keys has same hash value.

## Approach & Efficiency

* Time comlexity for add method in worst case is O(N)
* Space comlexity for add method is O(1)
* Time comlexity for get method in worst case is O(N)
* Space comlexity for get method is O(1)
## API

> get : Retrieve the  value from hashtable for the given key 

> add: adding a new key value to the hashtable.

> _hash  : Takes a key which is a string and returns an integer which is the index that will be used to store the key/value pair
> 
> contains : Method Indicating if the key exist in the hashtable or not