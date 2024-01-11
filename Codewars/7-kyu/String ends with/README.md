### [String ends with?](https://www.codewars.com/kata/51f2d1cafc9c0f745c00037d/python)

##### Objective

- Write a Function that, given two String Values "X" and "Y", returns "True" if a string "X" ends with "Y" argument.

##### Constraints

##### Optional Solution 1 (Without)

```
def solution(string, ending):
    return ending in string[-len(ending):]

```

##### Optional Solution 2 (With)

```
def solution(string, ending):
    return string.endswith(ending)

```