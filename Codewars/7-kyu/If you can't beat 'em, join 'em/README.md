### [If you can't beat 'em, join 'em](https://www.codewars.com/kata/5d37899a3b34c6002df273ee/python)

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