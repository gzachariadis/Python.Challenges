# Python

### Rock-Paper-Scissors Game

Let's play! You have to return which player won! In case of a draw return Draw!.

```
def rps(p1, p2):
    outcomes = {
        "scissors" : "paper",
        "rock" : "scissors",
        "paper": "rock"
    }

    if outcomes[p1] == p2:
        return "Player 1 won"
    elif outcomes[p2] == p1:
        return "Player 2 won"
    return "Draw"
```

### Turn Hours,Minutes and Seconds to Milliseconds

Your task is to write a function that takes H - Hours, M - Minutes, S - Seconds and return it in Milliseconds

```
def past(h, m, s):
    return (3600 * h + 60 * m + s) * 1000
```

### Array Sum

Write a function that takes an array of numbers and returns the sum of the numbers. The numbers can be negative or non-integer. If the array does not contain any numbers then you should return 0.

```
def sum_array($1):
    return sum([i for i in $2])
```

### Return Negative

You are given a number and have to make it negative. But maybe the number is already negative?

```
def make_negative(number):
    return -abs(number)
```

### Convert boolean values to strings 'Yes' or 'No'.

Complete the method that takes a boolean value and return a "Yes" string for true, or a "No" string for false.

```
def bool_to_word(bool):
    return ['No', 'Yes'][bool]
```

### Count by X

Create a function with two arguments that will return an array of the first n multiples of x.
Assume both the given number and the number of times to count will be positive numbers greater than 0.

```
def count_by(x, n):
    return [i * x for i in range(1, n + 1)]
```

