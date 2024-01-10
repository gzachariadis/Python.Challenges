### [Reverse Words](https://www.codewars.com/kata/5259b20d6021e9e14c0010d4/python) ✅ - Codewars

##### Objective

- Write a Function that, given a string parameter, reverses each word in the string and returns the string with every word reversed.

##### Constraints

- All spaces in the given string should be retained.
  
##### Optimal Solution 

```
def reverse_words(sentence):
    return ' '.join(word[::-1] for word in sentence.split(' '))
```

### [Rock-Paper-Scissors Game](https://www.codewars.com/kata/5672a98bdbdd995fad00000f/python)

##### Objective 

- Write a Function that, plays Rock-Paper-Scissors, given two players' choices as String Values.

##### Constraints

- Scissors beats Paper
- Rock beats Scissors
- Paper beats Rock
- Return which Player won, or in case of a draw return "Draw!"
  
##### Optimal Solution

```
def rps(p1, p2):
    hand = {'rock':0, 'paper':1, 'scissors':2}
    results = ['Draw!', 'Player 1 won!', 'Player 2 won!']
    return results[hand[p1] - hand[p2]]
```

### [Turn Hours, Minutes and Seconds to Milliseconds](https://www.codewars.com/kata/55f9bca8ecaa9eac7100004a/python)

##### Objective

- Write a Function that, given "H" for Hours, "M" for Minutes and "S" for Seconds, returns the sum of all in Milliseconds.

##### Constraints

- H must be between 0 and 23
- M must be between 0 and 59
- S must be between 0 and 59

##### Optimal Solution

```
def past(h, m, s):
    return (3600 * h + 60 * m + s) * 1000
```

### [Get the Sum of all Numbers in Array](https://www.codewars.com/kata/53dc54212259ed3d4f00071c/python)

##### Objective

- Write a Function that, given an array of numbers returns the sum of the numbers in the array.

##### Constraints

- The numbers can be negative or non-integer.
- If the array does not contain any numbers then you should return 0.
- Negatives must subtract from the sum, while positivies add to it.

##### Optimal Solution

```
def sum_array(x):
    return sum([i for i in x])
```

### [Turn Number to Negative](https://www.codewars.com/kata/55685cd7ad70877c23000102/python)

##### Objective

- Write a Function that, given a number, transforms it to negative. 

##### Constraints

- The number can be negative already, in which case no change is required.
- Zero (0) is not checked for any specific sign. 

##### Optimal Solution

```
def make_negative(number):
    return -abs(number)
```

### [Convert boolean values to strings 'Yes' or 'No'](https://www.codewars.com/kata/53369039d7ab3ac506000467/python)

##### Objective

- Write a Function that, given a boolean value, returns "Yes" for True, or "No" for False.

##### Constraints

- Output must be of String type.

##### Optimal Solution

```
def bool_to_word(bool):
    return ['No', 'Yes'][bool]
```

### [Count by X](https://www.codewars.com/kata/5513795bd3fafb56c200049e/python)

##### Objective

- Write a Function that, given two arguments "N" and "X", returns an array of the first "N" multiples of "X".

##### Constraints 

- Assume both the given number and the number of times to count will be positive numbers greater than 0.

##### Optimal Solution 1  

```
def count_by(x, n):
    return [i * x for i in range(1, n + 1)]
```

##### Optimal Solution 2 

```
def count_by(x, n):
    return list(range(x, n * x + 1, x))
```

### [Categorize each item in List](https://www.codewars.com/kata/5502c9e7b3216ec63c0001aa/solutions/python)

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

### [Does String end with?](https://www.codewars.com/kata/51f2d1cafc9c0f745c00037d/python)

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

### [Double Each Element in Array](https://www.codewars.com/kata/57f781872e3d8ca2a000007e/python)

##### Objective

- Write a Function that, given an array of integers, returns a new array with each integer's value doubled.

##### Constraints

- The output must be a new List.

##### Optimal Solution

```
def maps(a):
    return [2 * x for x in a]
```

### [Check if Element in List](https://www.codewars.com/kata/57cc975ed542d3148f00015b/python)

##### Objective

- Write a Function that, given an array "Sequence" and a value "X", check whether the provided array contains the value and returns return "True" if the array contains the value or "False" if not.

##### Constraints

- Return type must be of type Boolean.

```
def check(seq, elem):
    return elem in seq
```

### [Sum of Only Positives in List](https://www.codewars.com/kata/5715eaedb436cf5606000381/python)

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

### [Convert Number to String](https://www.codewars.com/kata/5265326f5fda8eb1160004c8/python)

##### Objective 

- Write a Function that, can transform a number (integer) into a string.

##### Constaints

- Output must be of type String.

##### Optimal Solution

```
def number_to_string(num):
    return f"{num}"
```

### [Get Middle Character(s) based on even or odd Length](https://www.codewars.com/kata/56747fd5cb988479af000028/python)

##### Objective 

- Write a Function that, given a word returns the middle character of the word.

##### Constraints

- If the word's length is odd, return the middle character.
- If the word's length is even, return the middle 2 characters.

##### Optimal Solution

```
def get_middle(s):
    index, odd = divmod(len(s), 2)
    return s[index] if odd else s[index - 1:index + 1]
```
### [PascalCase](https://www.codewars.com/kata/5390bac347d09b7da40006f6/python)

##### Objective

- Write a Function that, performs Pascal-Case (capitalize every word's first letter) on a given string. 

##### Constraints

- None.
  
##### Optimal Solution

```
def pascal_case(string):
    return ' '.join(word.capitalize() for word in string.split())
```

### [Number of People in the Bus](https://www.codewars.com/kata/5648b12ce68d9daa6b000099/python)

##### Objectives

- Write a Function that, given a list (or array) of integer pairs, representing the number of people that get on the bus (the first item) and the number of people that get off the bus (the second item) at a bus stop, returns the number of people who are still on the bus after the last bus stop (after the last array). 

##### Constraints

- The test cases ensure that the number of people in the bus is always >= 0. So the returned integer can't be negative.
- The second value in the first pair in the array is 0, since the bus is empty in the first bus stop.

##### Optimal Solution

```
def number(bus_stops):
    return sum(on - off for on, off in bus_stops)
```

### [Remove First and Last Character from String](https://www.codewars.com/kata/56bc28ad5bdaeb48760009b0/python)

##### Objective

- Write a Function that, removes the first and last characters of a string.

##### Constraints

- You don't have to worry with strings with less than two characters.

##### Optimal Solution

```
def remove_char(s):
    return s[1 : -1]
```
