# Introductory Programming Assignments

## Polygons Exercises

### Draw a horizontal line
Given a number n, print n asterisks on one line. Example when n=8:
```
********
```

### Draw a vertical line
Given a number n, print n lines, each with one asterisk. Example when n=3:
```
*
*
*
```

### Draw a right triangle
Given a number n, print n lines, each with one more asterisk than the last (i.e. one on the first line, two on the second,etc.). Example when n=3:
```
*
**
***
```

### Isosceles Triangle
Given a number n, print a centered triangle. Example for n=3:
```
  *
 ***
*****
```

### Diamond
Given a number n, print a centered diamond. Example for n=3:
```
  *
 ***
*****
 ***
  *
```

### Diamond with Name
Given a number n, print a centered diamond with your name in place of the middle line. Example for n=3:
```
  *
 ***
Tulio
 ***
  *
```

### Draw a square
Given a number n, print a square with side n. In order to give your square a nicer aspect ratio, intercalate the horizontal lines with asterisks and whitespaces. Example when n=4:
```
* * * *
*     *
*     *
* * * *
```

### Draw a diagonal
Given a number n, print a diagonal of lenght n. Example when n=5:

```
*
 *
  *
   *
    *
```

### Draw a reverse diagonal
Given a number n, print a reverse diagonal of lenght n. Example when n=5:

```
    *
   *
  *
 *
*
```

### X marks the spot
Given a number n, print an X of size n. Assume n is odd. Example when n=5:
```
*   *
 * *
  *
 * *
*   *
```

## FizzBuzz Exercise
FizzBuzz is a simple number game where you count, but say "Fizz" and/or "Buzz" instead of numbers adhering to certain rules.

Create a `fizz_buzz()` method that prints out the numbers 1 through 100.
- Instead of numbers divisible by three print "Fizz".
- Instead of numbers divisible by five print "Buzz".
- Instead of numbers divisible by three and five print "FizzBuzz".

Sample Output:
```
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
```

## Prime Factors Exercise
Write a method `generate(n)` that given an integer N will return a list of integers such that the numbers are the factors of N and are arranged in increasing numerical order.

For example, `generate(1)` should return an empty list and `generate(30)` should return the numbers: `2,3,5`.
