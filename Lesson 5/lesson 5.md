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

aside::before {
    content: "Speaker notes:";
    font-weight: bold;
}

aside {
    width: 850px;
    border: 1px black solid;
    padding: 5px 5px 5px 5px;
    font-size: 12px;
    line-height: 15px;
    background-color: #EFEFEF;
    display: none;
    position: absolute;
    bottom: 15px;
}

</style>

# Lesson 5

**Function**
Functions are used when you are repeating something multiple times. Hence it is a block of code that can be called multiple times. It can also be used to make your code more readable.

```python
def function_name():
    # code

function_name()
```

---

**Function with argument**

```python
def function_name(arg 1, arg 2, ...):
    # code

function_name(arg 1, arg 2, ...)
```

---

**Function with return value**

```python
def function_name(arg 1, arg 2, ...):
    # code
    return value
x = function_name(arg 1, arg 2, ...)
```

---

Libraries:
Libraries are a collection of functions that can be used by importing them. For example, the math library has a lot of mathematical functions that can be used.

```python

import math
x = math.pow(2, 3)
print(x)

```
