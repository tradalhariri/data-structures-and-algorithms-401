# Insert to Middle of an Array
we have an array , we need to insert a given value in the middle of that array
## Whiteboard Process

![Whiteboard](array-insert-shift.png)

## Approach & Efficiency
* first I determined the middle index
* if len of array even then middle = len(array) // 2
* if len of array is odd then middle = len(array) // 2 + 1
* then I saved the value of the middle index inside temp variable
* then set the array at middle with the given value.
* Then iterate over the array from middle (not included) to the end of array.
* in each iteration :
  * save the temp inside another temp variable (let us call it temp1)
  * update the temp variable with the current item in array
  * update the current item with the value of temp1
* after exit the loop append temp to array and return it.

I chosed to insert the value in the middle of the array without needing another helper array because I dont want to make the space complexty O(N). It stil O(1) but the time complexity is O(N)