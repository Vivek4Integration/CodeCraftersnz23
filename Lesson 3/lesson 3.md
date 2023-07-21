--- 
marp: true
author: Vivek Jayachandran
theme: gaia
---
<style>
:root{
    --color-background: #101010;
    --color-foreground: #FFFFFF;
}
</style>

# Lesson 3

- Variables
- Control structures
  - If
  - Loop
    - While
    - For

---

## `Variables`

What is a Variable?
In Python, a variable is a named location used to store data in memory. It is helpful to think of variables as a container that holds data that can be changed later in the program. For example:

``` python
x=10
```

---

## `Variables`

Naming Variables
In Python, variables can be declared and values can be assigned to it. In Python, variables are not bound to a specific type, so you can assign a string to a variable, and later assign an integer to the same variable.

``` python
x = 10 # integer
y = "Hello, World!" # String
print(x)
print(y)
```

> ***Give descriptive names for variables.***

---

## `Variables`

Problem?

``` python
x=10
y=20
print(x)
print(y)
```

Can you swap their values?

---

### `If`

What is an if statement?
The if statement in Python is a control structure that is used to check conditions. If the condition is true, the block of code under the if statement will be executed. If the condition is false, the block of code under the if statement will be skipped.

Example of if Statement
Here is an example of an if statement:

``` python
x = 10
if x > 0:
    print("x is positive")
```

---

### `If else`

The if-else statement in Python is used to check conditions and execute a specific block of code if the condition is true, and another block of code if the condition is false.

The syntax of the if-else statement is:

```python
if condition:
    # block of code if condition is true
else:
    # block of code if condition is false
```

---

### `If else`

Here is an example of an if-else statement:

```python
x = -10
if x > 0:
    print("x is positive")
else:
    print("x is not positive")
```

---

### `while` Loop

The while loop in Python is used to iterate over a block of code as long as the test expression (condition) is true.

Syntax of while Loop
The syntax of a while loop in Python is:

```python
while condition:
    # block of code
```

Here, condition is a boolean expression that is either True or False. The # block of code is a series of Python statements which will be executed as long as the condition is true.

---

### Example of `while` Loop

In this example, the condition is i <= 5. As long as i is less than or equal to 5, the print statement will be executed and i will be incremented by 1.

```python
i = 1
while i <= 5:
    print(i)
    i += 1
```

---

### for Loop

The for loop in Python is used to iterate over a sequence (like a list, tuple, dictionary, set, or string).

Syntax of for Loop:

``` python
for element in sequence:
    # block of code
```

---

### Example for `for` loop

Here, element is the variable that takes the value of the item inside the sequence on each iteration. The # block of code is a series of Python statements which will be executed for each item in the sequence.

``` python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

```

``` text
apple
banana
cherry

```

---

### Example for `for` loop

``` python
for i in range(5):
    print(i)
```

```text
0
1
2
3
4
```
---

### `break` and `continue` Statements

break and continue statements can alter the flow of a normal loop.

The break statement immediately terminates the loop, and program control proceeds to the lines of code that follow the loop.

The continue statement causes the program to skip the rest of the loop and immediately proceed to the next iteration.