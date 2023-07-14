---
marp: true
author: Vivek Jayachandran
size: 4:3
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

# Lesson 2

- IDE setup
- Problem solving

---

# Lesson 2

- IDE
  - What are IDE?
  - How to use them?
  - What are popular IDEs.

---

# Lesson 2

- Python
  - Guido van Rossum
  - Interpreted language
  - Why is it not compiled language?

---

# Lesson 2

- Showcase spiral 1
- Showcase spiral 2

---

# Lesson 2

- first program
- Jupyter notebook
  - What is it?
  - Why is it used?

---

# Lesson 2

- Problem solving
  - Left brain (Puzzle solving)
  - Right brain (Creative writing)
  - Limitation
- Mental exercise
  - Puzzles

---

# Lesson 2

## Problem 1

- A farmer, a wolf, a goat and a cabbage problem,
  - Cross the rive by boat,
  - Farmer + 1 item
  - Wolf will eat goat,
  - Goat will eat cabbage,

<!-- A farmer with a wolf, a goat, and a cabbage must cross a river by boat. The boat can carry only the farmer and a single item. If left unattended together, the wolf would eat the goat, or the goat would eat the cabbage. How can they cross the river without anything being eaten? -->

---

# Lesson 2

## Problem 1 answer

- Take the goat over
- Return empty-handed
- Take the wolf or cabbage over
- Return with the goat
- Take whichever wasn't taken in step 3 over
- Return empty-handed
- Take the goat over
<!--Key: On return journey you can return things back.-->
---

# Lesson 2

## Problem 2

- Three identical brother problem,
  - William, John and James,
  - John owes you money,
  - One question to determine which brother?

<!-- There are three brothers John, James and William. John and James always lies, whereas William always tells the truth. A while back you lent John a considerable sum of money and he has yet to pay you back. One day, while walking down the street, you run into one of the brothers. If it is John, you are keen to confront him about getting your money back, but you aren't able to tell whether it is John, James or William. What question would you ask to determine whether or not he is John? -->

---

# Lesson 2

## Problem 2 solution

|  |John(lies)  |James(lies)  |William  |
|---------|---------|---------|---------|
|Are you John?     |    No     |     Yes    |    No     |
|Are you James?     |    Yes     |    No     |     No    |
|Are you William?     |    Yes     |    Yes     |    Yes     |
