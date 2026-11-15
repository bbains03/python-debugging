# Problem 5: Average Calculator — ZeroDivisionError

## 1. Original Bug
The program attempted to calculate the average of an empty list.

```python
scores = []
```

**Error:** `ZeroDivisionError: division by zero`

## 2. Why the Error Occurred
The function calculated the average using:

```python
average = total / len(numbers)
```

Since the list was empty, `len(numbers)` returned `0`. Python cannot divide a number by zero.

## 3. How I Fixed It
I added a conditional statement at the beginning of the function:

```python
if len(numbers) == 0:
    return 
```

This checks whether the list is empty before attempting the calculation. If it is empty, the function returns `None` and stops executing.

## 4. Testing
- `scores = []` → `None`
- `scores = [80, 90, 70]` → `80.0`
- `scores = [100]` → `100.0` (expected)
- `scores = [50, 100]` → `75.0` (expected)

## 5. What I Learned
- `len()` counts the number of elements in a list.
- Function parameters receive values when a function is called.
- Defining a function does not execute its body.
- `return` immediately exits a function.
- `None` represents the absence of a value, whereas `0` is an actual numerical value.
- Conditional statements can prevent errors by checking for invalid inputs before performing calculations.
- A `for` loop can accumulate values using `+=`.

## 6. Key Takeaway
Before performing a calculation, check whether the input is valid. Handling edge cases such as empty lists prevents programs from crashing.