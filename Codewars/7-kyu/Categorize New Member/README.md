### [Categorize New Member](https://www.codewars.com/kata/5502c9e7b3216ec63c0001aa/solutions/python)

##### Objective 

- Write a Function that, given a list of pairs, each pair consists of an integer for the person's age and an integer for the person's handicap, returns a list of string values stating whether the respective member is to be placed in the "Senior" or "Open" category, based on the constraints.

##### Constraints

- The Western Suburbs Croquet Club has two categories of membership, Senior and Open. 
- To be a senior, a member must be at least 55 years old and have a handicap greater than 7.
- Input will consist of a list of pairs.

##### Optimal Solution

```
def openOrSenior(data):
  return ["Senior" if age >= 55 and handicap >= 8 else "Open" for (age, handicap) in data]
```