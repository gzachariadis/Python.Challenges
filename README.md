# Challenges

A repository covering my answers to Codewars Python Challenges.

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

## Easy (7 & 8 kyu)

### [Reverse Words](https://www.codewars.com/kata/5259b20d6021e9e14c0010d4/python)

Complete the function that accepts a string parameter. Reverses each word in the string.

Return the string with every word reversed. All spaces in the string should be retained.

```
def reverse_words(sentence):
    return ' '.join(word[::-1] for word in sentence.split(' '))
```

### [Rock-Paper-Scissors Game](https://www.codewars.com/kata/5672a98bdbdd995fad00000f/python)

Let's play! You have to return which player won! In case of a draw return Draw!.

```
def rps(p1, p2):
    hand = {'rock':0, 'paper':1, 'scissors':2}
    results = ['Draw!', 'Player 1 won!', 'Player 2 won!']
    return results[hand[p1] - hand[p2]]
```

### [Turn Hours, Minutes and Seconds to Milliseconds](https://www.codewars.com/kata/55f9bca8ecaa9eac7100004a/python)

Your task is to write a function that takes H - Hours, M - Minutes, S - Seconds and return it in Milliseconds.

```
def past(h, m, s):
    return (3600 * h + 60 * m + s) * 1000
```

### [Get the Sum of all Numbers in Array](https://www.codewars.com/kata/53dc54212259ed3d4f00071c/python)

Write a function that takes an array of numbers and returns the sum of the numbers.

The numbers can be negative or non-integer.

If the array does not contain any numbers then you should return 0.

```
def sum_array(x):
    return sum([i for i in x])
```

### [Turn Number to Negative](https://www.codewars.com/kata/55685cd7ad70877c23000102/python)

You are given a number and have to make it negative. But maybe the number is already negative?

```
def make_negative(number):
    return -abs(number)
```

### [Convert boolean values to strings 'Yes' or 'No'](https://www.codewars.com/kata/53369039d7ab3ac506000467/python)

Complete the method that takes a boolean value and return a "Yes" string for true, or a "No" string for false.

```
def bool_to_word(bool):
    return ['No', 'Yes'][bool]
```

### [Count by X](https://www.codewars.com/kata/5513795bd3fafb56c200049e/python)

Create a function with two arguments that will return an array of the first n multiples of x.

Assume both the given number and the number of times to count will be positive numbers greater than 0.

#### Solution 1 

```
def count_by(x, n):
    return [i * x for i in range(1, n + 1)]
```

#### Solution 2 

```
def count_by(x, n):
    return list(range(x, n * x + 1, x))
```

### [Categorize each item in List](https://www.codewars.com/kata/5502c9e7b3216ec63c0001aa/solutions/python)

The Western Suburbs Croquet Club has two categories of membership, Senior and Open.

To be a senior, a member must be at least 55 years old and have a handicap greater than 7.

Input will consist of a list of pairs.

```
def openOrSenior(data):
  return ["Senior" if age >= 55 and handicap >= 8 else "Open" for (age, handicap) in data]
```

### [Does String end with?](https://www.codewars.com/kata/51f2d1cafc9c0f745c00037d/python)

Complete the solution so that it must return True if a string ends with 2nd argument (also a string).

#### Solution 1

```
def solution(string, ending):
    return ending in string[-len(ending):]

```

#### Solution 2 

```
def solution(string, ending):
    return string.endswith(ending)

```

### [Double Each Element in Array](https://www.codewars.com/kata/57f781872e3d8ca2a000007e/python)

Given an array of integers, return a new array with each value doubled.

```
def maps(a):
    return [2 * x for x in a]
```

### [Check if Element in List](https://www.codewars.com/kata/57cc975ed542d3148f00015b/python)

You will be given an array a and a value x.

All you need to do is check whether the provided array contains the value.

Return true if the array contains the value, false if not.

```
def check(seq, elem):
    return elem in seq
```

### [Sum of Only Positives in List](https://www.codewars.com/kata/5715eaedb436cf5606000381/python)

You get an array of numbers, return the sum of all of the positives ones.

#### Solution 1

```
def positive_sum(arr):
    return sum(x for x in arr if x > 0)
```

#### Solution 2

```
def positive_sum(arr):
    if arr:
        return sum([i for i in arr if i >= 0])
    return 0
```

### [Convert Number to String](https://www.codewars.com/kata/5265326f5fda8eb1160004c8/python)

We need a function that can transform a number (integer) into a string.

```
def number_to_string(num):
    return f"{num}"
```

### [Get Middle Character(s) based on even or odd Length](https://www.codewars.com/kata/56747fd5cb988479af000028/python)

You are going to be given a word.

Your job is to return the middle character of the word.

If the word's length is odd, return the middle character.

If the word's length is even, return the middle 2 characters.

```
def get_middle(s):
    index, odd = divmod(len(s), 2)
    return s[index] if odd else s[index - 1:index + 1]
```

### [PascalCase](https://www.codewars.com/kata/5390bac347d09b7da40006f6/python)

Perform Pascal Case on a given String.\
PascalCase stands for capitalize every word's first letter.

```
def pascal_case(string):
    return ' '.join(word.capitalize() for word in string.split())
```

### [Number of People in the Bus](https://www.codewars.com/kata/5648b12ce68d9daa6b000099/python)

There is a bus moving in the city which takes and drops some people at each bus stop.

You are provided with a list (or array) of integer pairs. 

Elements of each pair represent the number of people that get on the bus (the first item) and the number of people that get off the bus (the second item) at a bus stop.

Your task is to return the number of people who are still on the bus after the last bus stop (after the last array). 

```
def number(bus_stops):
    return sum(on - off for on, off in bus_stops)
```

### [Remove First and Last Character from String](https://www.codewars.com/kata/56bc28ad5bdaeb48760009b0/python)

Your goal is to create a function that removes the first and last characters of a string.

```
def remove_char(s):
    return s[1 : -1]
```

## Medium (5-6 kyu)

### [Move Zeroes to the End of List](https://www.codewars.com/kata/52597aa56021e91c93000cb0/python)

Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

```
def move_zeros(array):
    return [x for x in array if x!=0] + [0] * array.count(0)
```

### [Sum of Multiples inside Number](https://www.codewars.com/kata/514b92a657cdc65150000006/python)

List all natural numbers below the given parameter (not including the parameter)
List the numbers which are multiple of 3 or 5. Then sum those multiples.

```
def solution(number):
    return sum(n for n in range(number) if n % 3 == 0 or n % 5 == 0)
```

### [Create Character Pairs from String](https://www.codewars.com/kata/515de9ae9dcfc28eb6000001/python)

Complete the solution so that it splits the string into pairs of two characters.

If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').

#### Solution 1

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

#### Solution 2

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

Given a floating-point number, return it as floating-point number type with only the first two decimal points. 

##### Constraints 

1. No need to check whether the input is a valid number.
2. Don't [Round](https://www.w3schools.com/python/ref_func_round.asp) the numbers. 

##### Optimal Solution 

```
def two_decimal_places(number):
  return int (number * 100) / 100.0
```

##### My Solution

```
def two_decimal_places(number):
    number = str(number)
    return float(number[:number.index('.') + 3])
```

### [Calculate Items' cost plus Tax](https://www.codewars.com/kata/585d7b4685151614190001fd/python)

##### Objective

Given a catalog of items accompanied by prices in a form of a dictionary, and an array specifying the items bought by a particular customer, calculate the total cost of the items plus a given tax.

##### Constraints

1. In case an item does not exist in the catalog dictionary, it should be ignored.
2. Output should be rounded to two decimal places.

##### Optimal Solution

```
def get_total(costs, items, tax):
    return round(sum(costs.get(item, 0) for item in items) * (1 + tax), 2)
```

#### My Solution

```
def get_total(costs, items, tax):
    total_cost = sum([costs[x] for x in items if x in costs.keys()])
    return round(total_cost + (total_cost * tax),2)
```

### [Can't Beat 'em, Join'em!](https://www.codewars.com/kata/5d37899a3b34c6002df273ee/python)

##### Objective

You are given a list of nested lists. 
Join the lists together by descending total list value (sum).
Ending up with one final list.

##### Constraints

1. In the case of more than one list sharing the same sum, place them in the same order as they were provided.

##### Optimal Solution

```
from itertools import chain

def cant_beat_so_join(lsts):
    return list(chain.from_iterable(sorted(lsts, key=sum, reverse=True)))
```

##### My Solution

```
from itertools import chain

def cant_beat_so_join(numbers):
    return list(chain(*sorted(numbers, key=sum,reverse=True)))
```
