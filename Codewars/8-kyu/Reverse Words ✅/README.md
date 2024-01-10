### [Reverse Words](https://www.codewars.com/kata/5259b20d6021e9e14c0010d4/python) - 31/12/2023

##### Objective

- Write a Function that, given a string parameter, reverses each word in the string and returns the string with every word reversed.

##### Constraints

- All spaces in the given string should be retained.
  
##### Optimal Solution 

```
def reverse_words(sentence):
    return ' '.join(word[::-1] for word in sentence.split(' '))
```