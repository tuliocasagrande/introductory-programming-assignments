
# coding: utf-8

# # Introductory Programming Assignments
# 
# 
# ## Polygons Exercises
# 
# 
# ### Draw a horizontal line
# Given a number n, print n asterisks on one line. Example when n=8:
# ```
# ********
# ```

# In[1]:


def print_hline(n):
    print('*' * n)

print_hline(8)


# ### Draw a vertical line
# Given a number n, print n lines, each with one asterisk. Example when n=3:
# ```
# *
# *
# *
# ```

# In[2]:


def print_vline(n):
    print('*\n' * n, end='')

print_vline(3)


# ### Draw a right triangle
# Given a number n, print n lines, each with one more asterisk than the last (i.e. one on the first line, two on the second,etc.). Example when n=3:
# ```
# *
# **
# ***
# ```

# In[3]:


def print_right_triangle(n):
    for i in range(1, n + 1):
        print_hline(i)

print_right_triangle(3)


# ### Isosceles Triangle
# Given a number n, print a centered triangle. Example for n=3:
# ```
#   *
#  ***
# *****
# ```

# In[4]:


def print_iso_triangle(n):
    for i in range(1, n + 1):
        spaces = ' ' * (n - i)
        asterisks = '*' * (2 * i - 1)
        print(spaces + asterisks)

print_iso_triangle(3)


# ### Diamond
# Given a number n, print a centered diamond. Example for n=3:
# ```
#   *
#  ***
# *****
#  ***
#   *
# ```

# In[5]:


def print_diamond(n):
    for i in range(1, n + 1):
        spaces = ' ' * (n - i)
        asterisks = '*' * (2 * i - 1)
        print(spaces + asterisks)

    for i in range(n - 1, 0, -1):
        spaces = ' ' * (n - i)
        asterisks = '*' * (2 * i - 1)
        print(spaces + asterisks)

print_diamond(3)


# ### Diamond with Name
# Given a number n, print a centered diamond with your name in place of the middle line. Example for n=3:
# ```
#   *
#  ***
# Bill
#  ***
#   *
# ```

# In[6]:


def print_diamond_with_name(n, name):
    for i in range(1, n):
        spaces = ' ' * (n - i)
        asterisks = '*' * (2 * i - 1)
        print(spaces + asterisks)

    print(name)

    for i in range(n - 1, 0, -1):
        spaces = ' ' * (n - i)
        asterisks = '*' * (2 * i - 1)
        print(spaces + asterisks)

print_diamond_with_name(3, 'Tulio')


# ### Draw a square
# Given a number n, print a square with side n. In order to give your square a nicer aspect ratio, intercalate the horizontal lines with asterisks and whitespaces. Example when n=4:
# ```
# * * * *
# *     *
# *     *
# * * * *
# ```

# In[7]:


def square(n):
    for i in range(1, n + 1):
        if i == 1 or i == n:
            print('* ' * n)
        else:
            print('*' + ' ' * (2 * n - 3) + '*')

square(4)


# ### Draw a diagonal
# Given a number n, print a diagonal of lenght n. Example when n=5:
# 
# ```
# *
#  *
#   *
#    *
#     *
# ```

# In[8]:


def diagonal(n):
    for i in range(n):
        print(' ' * i + '*')

diagonal(5)


# ### Draw an reverse diagonal
# Given a number n, print an reverse diagonal of lenght n. Example when n=5:
# 
# ```
#     *
#    *
#   *
#  *
# *
# ```

# In[9]:


def reverse_diagonal(n):
    for i in range(n - 1, -1, -1):
        print(' ' * i + '*')

reverse_diagonal(5)


# ### X marks the spot
# Given a number n, print an X of size n. Assume n is odd. Example when n=5:
# ```
# *   *
#  * *
#   *
#  * *
# *   *
# ```

# In[10]:


def x_marks_the_spot(n):
    h = n // 2
    for i in range(0, h):
        middle_spaces = ' ' * (n - 2 - i * 2)
        print(' ' * i + '*' + middle_spaces + '*')

    print(' ' * h + '*')

    for i in range(h - 1, -1, -1):
        middle_spaces = ' ' * (n - 2 - i * 2)
        print(' ' * i + '*' + middle_spaces + '*')

x_marks_the_spot(5)


# ## FizzBuzz Exercise
# FizzBuzz is a simple number game where you count, but say "Fizz" and/or "Buzz" instead of numbers adhering to certain rules.
# 
# Create a `fizz_buzz()` method that prints out the numbers 1 through 100.
# - Instead of numbers divisible by three print "Fizz".
# - Instead of numbers divisible by five print "Buzz".
# - Instead of numbers divisible by three and five print "FizzBuzz".
# 
# Sample Output:
# ```
# 1
# 2
# Fizz
# 4
# Buzz
# Fizz
# 7
# 8
# Fizz
# Buzz
# 11
# Fizz
# 13
# 14
# FizzBuzz
# ```

# In[11]:


def fizz_buzz(n):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)

fizz_buzz(15)


# ## Prime Factors Exercise
# Write a method `generate(n)` that given an integer N will return a list of integers such that the numbers are the factors of N and are arranged in increasing numerical order.
# 
# For example, `generate(1)` should return an empty list and `generate(30)` should return the numbers: `2,3,5`.

# In[12]:


def generate(n):
    factors = []
    i = 2
    while i <= n:
        while n % i == 0:
            factors.append(i)
            n //= i
        i += 1

    return factors

print(generate(1))
print(generate(5))
print(generate(30))
print(generate(50))
print(generate(80))

