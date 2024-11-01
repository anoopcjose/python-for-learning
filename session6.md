# Session 6

### History:
1. Fairly old language created by Guido Van Rossum
2. Design began in the late 1980s and was first released in February 1991

### Features:
1. Simple language which is easier to learn
2. Free and open-source
3. Portability
4. Extensible and Embeddable
5. High-level, interpreted language 
6. Large standard libraries to solve common tasks
7. Object-Oriented


## Sample Program & Starting The Interpreter

Add two numbers
```commandline
num1 = 3  
num2 = 5  
sum = num1 + num2  
print(sum)
```  
```commandline
print("Hello, World!")
```

1. Immediate mode
2. Script mode

Integrated Development Environment (IDE)


### Keywords

Rules for writing Identifiers

1. Identifiers can be a combination of letters in lowercase (a to z) or uppercase (A to Z) or digits (0 to 9) or an underscore (_)
2. An identifier cannot start with a digit. 1variable is invalid, but variable1 is perfectly fine
3. Keywords cannot be used as identifiers
4. We cannot use special symbols like !, @, #, $, % etc. in our identifier
5. Identifier can be of any length


### Python Comments, Statement and Indentation 

```commandline
# this is a comment
```
```commandline
a = "this is a statement"
```
```commandline
if True:
  print("Indentation is important in Python")
```

## Python Variables and Data Types

### Variables: 
> Numbers, Strings, List, Tuple, Set, Dictionary

### 1. Python Numbers: 
> Integers, Floating Point & Complex Numbers
```commandline
a = 5
print(a, "is of type", type(a))

a = 2.0
print(a, "is of type", type(a))

a = 1+2j
print(a, "is complex number?", isinstance(1+2j,complex))
```
# -----------------------

### 2. Python Strings
Sequence of Unicode Characters

```commandline
s = 'Hello world!’

# s[4] = 'o’
print("s[4] = ", s[4])

# s[6:11] = 'world
print("s[6:11] = ", s[6:11])
```

Generates error   
Strings are immutable in Python  
> s[5] ='d'
# -----------------------

### 3. Python List
An ordered sequence of items
```commandline
a = [5,10,15,20,25,30,35,40]

# a[2] = 15
print("a[2] = ", a[2])

# a[0:3] = [5, 10, 15]
print("a[0:3] = ", a[0:3])

# a[5:] = [30, 35, 40]
print("a[5:] = ", a[5:])
```
# -----------------------

### 4. Python Tuple
An ordered sequence of items same as list.  
The only difference is that tuples are immutable

```commandline
t = (5,'program', 1+3j)

# t[1] = 'program’
print("t[1] = ", t[1])

# t[0:3] = (5, 'program', (1+3j))
print("t[0:3] = ", t[0:3])
```
Generates error  
Tuples are immutable  
> t[0] = 10
# -----------------------

### 5. Python Set
An unordered collection of Unique Items

Cannot have multiple occurrences of the same element and store unordered values
```commandline
a = {5, 2, 3, 1, 4}

# printing set variable
print("a = ", a)

# data type of variable a
print(type(a))
```
# -----------------------

### Python Dictionary
An unordered collection of Key-Value Pairs

```commandline
d = {1:'value','key':2}
print(type(d))

print("d[1] = ", d[1]);

print("d['key'] = ", d['key']);

# Generates error
print("d[2] = ", d[2]);
```

# -----------------------
### Conversion between Data Types

Type conversion functions: int(), float(), str() etc.
```commandline
float(5) 
5.0 
```

### Python Output, Input & Import

```commandline
print('This sentence is output to the screen')

# Output: This sentence is output to the screen

a = 5
print('The value of a is', a)

# Output: The value of a is 5
```


import math
print(math.pi)

> from math import pi   
> pi  
3.141592653589793

> num = input('Enter a number: ')   
Enter a number: 10   
> num   
'10'


### Type of Operators

1. Arithmetic Operators
2. Comparison(Relational) Operators
3. Logical Operators
4. Bitwise Operators
5. Assignment Operators
6. Special Operators
7. Identity operators: is and is not are the identity operators in Python.
8. Membership operators: in and not in are the membership operators in Python.

## CONTROL STATEMENTS

### Decision-Making Control Statements

```commandline
if x%2 == 0:
	print 'x is even'
else:
	print 'x is odd'a
```

```commandline
if x < y:
	print 'x is less than y'
elif x > y:
	print 'x is greater than y'
else:
	print 'x and y are equal'

elif is an abbreviation of “else if”
```

```commandline
if x == y:
	print 'x and y are equal'
else:
	if x < y:
		print 'x is less than y'
	else:
		print 'x is greater than y'
```