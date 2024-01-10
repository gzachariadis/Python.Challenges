## Medium (5-6 kyu) - Codewars

### [Move Zeroes to the End of List](https://www.codewars.com/kata/52597aa56021e91c93000cb0/python)

##### Objective

- Write a Function that, given an array, moves all of the zeros to the end.

##### Constraints

- Preserve the order of the other elements as given.

##### Optimal Solution

```
def move_zeros(array):
    return [x for x in array if x!=0] + [0] * array.count(0)
```

### [Sum of Multiples inside Number](https://www.codewars.com/kata/514b92a657cdc65150000006/python)

##### Objective 

- Write a Function that, given a parameter, lists all natural numbers below the given parameter (not including the parameter), which are multiple of 3 or 5, returning the sum of those multiples.

##### Constraints

- If the number is a multiple of both 3 and 5, only count it once.
- Additionally, if the number is negative, return 0.
  
##### Optimal Solution

```
def solution(number):
    return sum(n for n in range(number) if n % 3 == 0 or n % 5 == 0)
```

### [Create Character Pairs from String](https://www.codewars.com/kata/515de9ae9dcfc28eb6000001/python)

##### Objective

- Write a Function that, splits the string into pairs of two characters.

##### Constraints

- If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').

##### Optimal Solution 1

```
def solution(s):
    result = []
    for i in range(0, len(s), 2):
        try:
            result.append("".join([s[i], s[i + 1]]))
        except IndexError:
            result.append("".join([s[-1:], "_"]))
    return result
```

##### Optimal Solution 2

```
def solution(s):
    result = []

    if len(s) % 2:
        s += '_'    
    for i in range(0, len(s), 2):
        result.append(s[i : i + 2])
    return result
```

### [Formatting Decimal Places](https://www.codewars.com/kata/5641c3f809bf31f008000042/python)

##### Objective

- Write a Function that, given a floating-point number, returns a floating-point number type with only the first two decimal points. 

##### Constraints 

- No need to check whether the input is a valid number.
- Don't [Round](https://www.w3schools.com/python/ref_func_round.asp) the numbers. 

##### Optimal Solution 

```
def two_decimal_places(number):
  return int (number * 100) / 100.0
```

### [Calculate Items' cost plus Tax](https://www.codewars.com/kata/585d7b4685151614190001fd/python)

##### Objective

- Write a Function that, given a catalog of items accompanied by prices in a form of a dictionary, and an array specifying the items bought by a particular customer, calculate the total cost of the items plus a given tax.

##### Constraints

- In case an item does not exist in the catalog dictionary, it should be ignored.
- Output should be rounded to two decimal places.

##### Optimal Solution

```
def get_total(costs, items, tax):
    return round(sum(costs.get(item, 0) for item in items) * (1 + tax), 2)
```

### [Can't Beat 'em, Join'em!](https://www.codewars.com/kata/5d37899a3b34c6002df273ee/python)

##### Objectives

- Write a Function that, given a list of nested lists, joins the lists together by descending total list value (sum) and returns one final aggregate list.

##### Constraints

- In the case of more than one list sharing the same sum, place them in the same order as they were provided.

##### Optimal Solution

```
from itertools import chain

def cant_beat_so_join(lsts):
    return list(chain.from_iterable(sorted(lsts, key=sum, reverse=True)))
```