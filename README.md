
# Booleans, Operators & Conditionals

Boolean values are generally `True` and `False` in Python. In fact, boolean values are used heavily in programming languages since they all eventually compile to binary code -- like in the matrix.

![matrix](matrix_binary.png)

Binary code is just `0`s and `1`s, On and Off, Yes and No, or *True* and *False*. 

In Python as with many other languages, there are things that are not purely `True` or `False`, but their value can be treated as `True` or `False`. We call these ***Truthy*** and ***Falsy***. So, while the value of the number `1` is not specifically `True`, it is Truthy (as are all other positive and negative intergers). Conversely, while the value of the number `0` is not specifically `False`, it is Falsy. We can test this with the `bool` operator, which returns to us the Boolean value of something (i.e. a truthy element returns True and a Falsy element returns False).

## bool() operator


```python
# testing truthiness and falsiness
print('1.', bool(True)) # True
print('2.', bool(False)) # False
print('3.', bool(1)) # True 
print('4.', bool(0)) # False
```


```python
# less obvious examples
print('1.', bool("hello")) # string 'hello' - True
print('2.', bool([])) # empty list - False
print('3.', bool(-300)) # negative number - True
print('4.', bool("")) # empty string - False
```

Here is a list of all the falsy values in Python:

*for now, the bolded examples are most important*
* **None**
* **False**
* **zero** of any numeric type, for example, **0**, 0L, **0.0**, 0j.
* **any empty sequence**, for example, **'', (), []**.
* **any empty mapping or dictionary**, for example, **{}**.
* instances of user-defined classes, if the class defines a `__nonzero__()` or `__len__()` method, when that method returns the integer zero or bool value False.

A list of all falsy values and more information on Booleans in Python can be found [here]('https://docs.python.org/2/library/stdtypes.html').

## Other things that return Boolean values - Comparison Operators

Comparison operators (or Relational operators) have a return value that is either True or False. In Python, comparison operators are:
```python
== # tests equality between two elements
!= # tests inequality between two elements
<, >, <=, >= # each tests the value between two elements
```
Perhaps the last line's operators are a little more familiar because we've seen these operators in math classes. But the first two might be bit more confusing, so, let's dive into those first.

The double equals operator (==) is testing whether the value of element1 is equal to that of element2.
```python 
False == True # returns False
False == False # returns True
10 == 20 # returns False
10 == 10 # returns True
"hi" == "HI" # returns False
"heLLo" == "heLLo" # returns True
```

The bang equals operator (!=) is testing whether the value of element1 is **not** equal to that of element2.

```python 
True != True # returns False
True != False # returns True
10 != 20 # returns True
10 != 10 # returns False
"hi" != "HI" # returns True
"heLLo" != "heLLo" # returns False
```




```python
print('1.', True != True) # False
print('2.', False == True) # False
print('3.', 10 == 10) # True
print('4.', "hi" == "HI") # False
print('5.', type(0) == int) # True
print('6.', ["hi"] == ["hi"]) # True
```

The greater than (`>`), less than (`<`), greater than or equal to (`>=`) and less than or equal (`<=`) to operators also only return True or False from an operation.


```python
print('1.', True > True) # False
print('2.', True >= True) # True
print('3.', 10 <= 10) # True
print('4.', 7 < 7) # False
print('5.', 10 < 100) # True
print('6.', 100 > 101) # False
# you can even compare strings to see which is alphabetically greater or less than
# a string is greater than if it comes after another string alphabetically (or if its ascii value is greater)
# capital letters have lower ascii values (come earlier in the alphabet) than their lowercase letter counterparts
print('7.', "A" < "a") # True 
print('8.', "aaron" > "alexa") # False
print('9.', "Terrance" > "Teresa") # True
```

## Logical Operators

The next group of operators are logical operators. They compare truthy/falsy values. The operators are:
```python
and 
# Compares two elements. If both elements are truthy, the second element is returned
# If there is a falsy value, the first falsy value is returned

or 
# Compares two elements. The first truthy element is returned. 
# If both elements are falsy, the second element is returned

not 
# returns a boolean value that is opposite of truthy/falsy value of the element
```
Let's see these in action:

*try to guess what the values will be before running the code - write your answers in a comment next to the print statement*


```python
print("1.", 2 and 0) #
print("2.", False and 2) #
print("3.", True and 2) #
print("4.", 2 and 3) #
print("5.", 2 or []) #
print("6.", 0 or []) #
print("7.", not False) #
print("8.", not True) #
print("9.", not []) #
print("10.", not 0) #
print("11.", not 100) #
```

## Identity Operators

The next type of operators are identity operators, `is` and `is not`. They check to see if one element is or is not the other element. This is similar to `!=` and `==`. However there is one key difference. The `!=` and `==` check to see if the value of each element is the same, however, the `is` and `is not` operators check to see if the elements are the same element. 

Let's check it out:

*again, try to find the correct return value for each example and write the answer in a comment next to the print statement*


```python
x = {'name': "example"}
b = x
c = {'name': "example"}
print("1.", {} is {}) #
print("1A.", {} == {}) #
print("2.", [] is []) #
print("3.", "Hi" is "Hi") #
print("4.", ["same"] is ["same"]) #
print("4A.", ["same"] == ["same"]) #
print("5.", 9 is not 10) #
print("6.", x is b) #
print("7.", b is c) #
print("7A.", b == c) #
print("8.", x is not c) #
```

As we can see, the `is` and `is not` operators are checking to see if the objects are exactly the same object in memory. However, the `==` and `!=` operators are simply checking to see if the value of each element is the same. This will become clearer as we learn more about how python stores data. 

All objects are stored in a specific place in memory, we can think of this as an address on the computer. All objects have their own unique address. When we use the `is` or `is not` operator, we are checking to see if the address of the object is the same as another object. When we use the `==` or `!=` operators, we are checking to see if they are basically equal in value, irrespective of whether they are the same or two different objects.

## Ternary Operator

The next operator is the Ternary. It is a bit more of a complicated operator, but it can be very useful when you would like to decide which value to assign to a variable. Ternaries are good for one-line conditions, but anything more complex makes ternary operators quite difficult to read. Let's check it out:


```python
my_condition = True
value = 10 if my_condition else 1000
print(value)
```


```python
# let's say we are receiving two variables with different 
# values and we want to assign the higher value to a new variable
x = 12
y = 20
new_variable = x if x > y else y
# here we are saying, take the value of x if it is greater than the value of y. else take the value of y
# since x > y evaluates to false, the ternary returns the value after the else statement
print(new_variable)
```

## Conditionals

The conditonal operators in python are:
```python
if
elif
else
```
The `if` and `elif` statements check to see if a condition is met. The first part of any conditional is always an `if`. The `elif` and `else` statements aren't always required when writing a conditional statement, but they **do** always require being preceded by an `if`. The block of code that follows an `if` is only executed if the condition is met, the same goes for an `elif` statement. The block of code that follows an `else` is only executed if the preceding conditions for the `if` and `elif` statemtents were not met.


```python
x = True
y = False
if x:
    print("If statement executed")
elif x:
    print("elif statement executed")
else:
    print("else statement executed")
```


```python
x = True
y = False
if y:
    print("If statement executed")
elif x:
    print("elif statement executed")
else:
    print("else statement executed")
```


```python
x = True
y = False
if y:
    print("If statement executed")
elif y:
    print("elif statement executed")
else:
    print("else statement executed")
```


```python
x = True
y = False
if x and y:
    print("If statement executed")
elif "hey" or y:
    print("elif statement executed")
else:
    print("else statement executed")
```


```python
if 0:
    print("If statement executed")
elif [] or "":
    print("elif statement executed")
else:
    print("else statement executed")

```


```python
# We can even NEST our if/elif/else statements!
x = True
y = False
if y:
    print("If statement executed")
elif [] or 100:
    if [] and True:
        print("Oh no... I don't get executed")
    elif "NESTING, OH YEAH":
        print("Woo! I get executed")
else:
    print("else statement executed")
```

# Summary

Boolean values and truthy/falsy values are heavily leveraged to make sure our programs are running properly and it is paramount to understand how to use these tools in order to make our programs as dynamic and clean as possible -- True or False? True!
