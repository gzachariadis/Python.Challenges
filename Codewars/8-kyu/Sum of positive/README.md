### [Sum of positive](https://www.codewars.com/kata/5715eaedb436cf5606000381/python)

##### Objective

- Write a Function that, given an array of numbers, returns the sum of all the positives numbers in the array.

##### Constraints

- Default sum (in case all negative) should be Zero (0).

##### Optimal Solution 1

```
def positive_sum(arr):
    return sum(x for x in arr if x > 0)
```

##### Optimal Solution 2

```
def positive_sum(arr):
    if arr:
        return sum([i for i in arr if i >= 0])
    return 0
```
