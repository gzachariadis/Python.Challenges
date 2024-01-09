# Python Challenges

![GitHub commit activity](https://img.shields.io/github/commit-activity/m/gzachariadis/Python.Challenges)
![GitHub last commit (by committer)](https://img.shields.io/github/last-commit/gzachariadis/Python.Challenges)

![LeetCode](https://img.shields.io/badge/LeetCode-000000?style=for-the-badge&logo=LeetCode&logoColor=#d16c06)

![Hackerrank](https://img.shields.io/badge/-Hackerrank-2EC866?style=for-the-badge&logo=HackerRank&logoColor=white)

![Codewars](https://img.shields.io/badge/Codewars-B1361E?style=for-the-badge&logo=codewars&logoColor=grey)

![Exercism](https://img.shields.io/badge/Exercism-009CAB?style=for-the-badge&logo=exercism&logoColor=white)

![Codewars](https://github.r2v.ch/codewars?user=gzachariadis&stroke=green)


A repository covering all the Python Challenges I have currently completed.

A "✅" next to a Challenge Title indicates I achieved the Optimal Solution (as voted by the Platform's Users) on my first attempt.

Completed - 31

- [Challenges](#challenges)
  - [Easy (7 \& 8 kyu)](#easy-7--8-kyu)
    - [Reverse Words](#reverse-words)
    - [Rock-Paper-Scissors Game](#rock-paper-scissors-game)
    - [Turn Hours, Minutes and Seconds to Milliseconds](#turn-hours-minutes-and-seconds-to-milliseconds)
    - [Get the Sum of all Numbers in Array](#get-the-sum-of-all-numbers-in-array)
    - [Turn Number to Negative](#turn-number-to-negative)
    - [Convert boolean values to strings 'Yes' or 'No'](#convert-boolean-values-to-strings-yes-or-no)
    - [Count by X](#count-by-x)
    - [Categorize each item in List](#categorize-each-item-in-list)
    - [Does String end with?](#does-string-end-with)
    - [Double Each Element in Array](#double-each-element-in-array)
    - [Check if Element in List](#check-if-element-in-list)
    - [Sum of Only Positives in List](#sum-of-only-positives-in-list)
    - [Convert Number to String](#convert-number-to-string)
    - [Get Middle Character(s) based on even or odd Length](#get-middle-characters-based-on-even-or-odd-length)
  - [Medium (5-6 kyu)](#medium-5-6-kyu)
    - [Move Zeroes to the End of List](#move-zeroes-to-the-end-of-list)
    - [Sum of Multiples inside Number](#sum-of-multiples-inside-number)

## Easy (7 & 8 kyu) - Codewars

### [Reverse Words](https://www.codewars.com/kata/5259b20d6021e9e14c0010d4/python) ✅

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

## Hard (4-2 kyu) - Codewars

<br>

## Expert (1 kyu) - Codewars
