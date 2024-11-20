## Data Structures & Control Flow
### Indentation
Python indentation is a way of telling a Python interpreter that the group of statements belongs to a particular block of code.
A block is a combination of all these statements. Block can be regarded as the grouping of statements for a specific purpose.

### Control Flow Statements
#### if, if...else... and if...elif...else.. statements
```[02_statements_and_expressions.md](02_statements_and_expressions.md)
if expression:
    statement(s)
elif expression:
    statement(s)
elif expression:
    statement(s)
...
else:
    statement(s)
```
#### for loop

In Python, we use a for loop to iterate over sequences such as lists, strings, dictionaries, etc.

```commandline
languages = ['Swift', 'Alto', 'Baleno']

# access elements of the list one by one
for lang in languages:
    print(lang)
```

In programming, the break and continue statements are used to alter the flow of loops:

* break exits the loop entirely  
* continue skips the current iteration and proceeds to the next one

```commandline
for i in range(5):
    if i == 3:
        break
    print(i)
```

```commandline
for i in range(5):
    if i == 3:
        continue
    print(i)
```

1. Write a function to calculate the sum of elements in a list that are greater than a given number.

2. Write a function to check if a given number is prime or not.

A prime number is only divisible by 1 and itself. For example, 13.
Return True if the number is prime, otherwise return False.
