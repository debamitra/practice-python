

---

### **Skill: List Comprehensions**

#### **Duration: 20 minutes**
1. **Quick Review (5 minutes):**
   - Syntax: `[expression for item in iterable if condition]`
   - Example: `[x**2 for x in range(10) if x % 2 == 0]`

2. **Exercises:**
   - Create a list of squares of numbers from 1 to 10.
   - Filter a list of names to include only those that start with "A."
   - Generate a dictionary where keys are numbers 1-5, and values are their cubes.

3. **Reflection:**
   - Write down one use case in a real-world project (e.g., filtering API responses).

---

### **Skill: Generators**

#### **Duration: 25 minutes**
1. **Quick Review (5 minutes):**
   - Syntax: Use `yield` instead of `return` to create a generator.
   - Example:
     ```python
     def countdown(n):
         while n > 0:
             yield n
             n -= 1
     ```

2. **Exercises:**
   - Write a generator for Fibonacci numbers up to `n`.
   - Create a generator that reads a file and yields one line at a time.
   - Design a generator to produce numbers divisible by 3 up to 100.

3. **Reflection:**
   - Compare memory usage between a generator and a list comprehension for large datasets.

---

### **Skill: Decorators**

#### **Duration: 30 minutes**
1. **Quick Review (5 minutes):**
   - Syntax:
     ```python
     def my_decorator(func):
         def wrapper():
             print("Before the function runs")
             func()
             print("After the function runs")
         return wrapper
     ```

2. **Exercises:**
   - Write a decorator to log the execution time of a function.
   - Create a decorator to cache results of a function.
   - Design a decorator that ensures a function only runs if a certain condition is met (e.g., user is logged in).

3. **Reflection:**
   - Think of how decorators can simplify repetitive tasks in larger projects.

---

### **Skill: File Handling**

#### **Duration: 20 minutes**
1. **Quick Review (5 minutes):**
   - Syntax for reading/writing files:
     ```python
     with open('file.txt', 'r') as f:
         data = f.read()
     ```

2. **Exercises:**
   - Write a script to read a CSV file and print rows where the second column is greater than 50.
   - Create a script to merge two text files line by line into a new file.
   - Parse a log file and output all lines containing the word "ERROR."

3. **Reflection:**
   - Identify one project idea where file handling would be critical (e.g., processing log files or managing configuration files).

---

### **Skill: Error Handling**

#### **Duration: 20 minutes**
1. **Quick Review (5 minutes):**
   - Syntax:
     ```python
     try:
         result = 10 / 0
     except ZeroDivisionError:
         print("Cannot divide by zero!")
     finally:
         print("This always runs.")
     ```

2. **Exercises:**
   - Write a function that validates user input as an integer and raises a `ValueError` for invalid input.
   - Create a function that reads a file and handles `FileNotFoundError` gracefully.
   - Implement a program to divide two numbers, handling `ZeroDivisionError` and ensuring cleanup in the `finally` block.

3. **Reflection:**
   - Note how error handling can make your code robust in production environments.

---

### **Wrap-Up (5-10 minutes)**
- **Review & Notes:**
   - Jot down key insights from each skill.
   - List a few real-world scenarios where these skills can be applied.
- **Set a Goal for Next Session:**
   - Example: Implement these skills in a mini-project like a "Log Analyzer" or "File Processor."

---

## Review notes

List comprehension

syntax -> [ expression for item in iterable if condition ]
examples -> [ x ** 2 for x in range(10) if x % 2 ==0 ]

