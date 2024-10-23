## Python Fundamentals
### Data Types & Variables
1. String: A sequence of characters enclosed in quotes.
```x = "Hello World"```  

2. Integer: A whole number without a decimal point.  
```x = 50```

3. Float: A number with a decimal point.  
```x = 60.5```

4. Complex: A number with a real and imaginary part.  
```x = 3j```

5. List: An ordered, mutable collection of items.  
         The elements have a defined sequence, starting from index 0. Python lists allow modification after creation, meaning you can change, add, or remove elements from the list without creating a new list.  
```x = ["apple", "banana", "cherry"]```

6. Tuple: An ordered, immutable collection of items.  
          No In-place Modification: Unlike lists, Python tuples do not have methods like append(), remove(), or insert() that modify their contents. The tuple does not allow changes to its memory structure after it is created.  
          No Item Re-assignment: You cannot reassign a value at a specific index in a tuple after it has been created.  
          Fixed Memory Allocation: When a tuple is created, Python allocates a fixed block of memory for it. Since it is immutable, there is no need to allocate additional memory for new elements or modifications. This fixed memory usage contributes to its immutability.  
```x = ("apple", "banana", "cherry")```

7. Range: A sequence of numbers generated within a range.  
```
x = range(10)
print(x)
print(list(x))
```
```commandline
range(0, 10)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

8. Dictionary: A collection of key-value pairs.  
```x = {"name": "Bob", "age": 24}```

9. Set: An unordered collection of unique items.  
```x = {"training", "for", "python"}```

10. Frozenset: An immutable version of a set.  
```x = frozenset({"training", "for", "python"})```

11. Boolean: A binary value representing True or False.  
```x = True```

12. Bytes: An immutable sequence of bytes.  
```x = b"training"```

13. Bytearray: A mutable sequence of bytes.  
```x = bytearray(4)```

14. Memoryview: A memory view object of a bytes-like object.  
```x = memoryview(bytes(6))```

15. NoneType: A special data type representing the absence of a value.  
```x = None```