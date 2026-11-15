# Problem 4 — Inventory Calculator

## Original Bug
The original code used:

```python
for i in range(len(items) - 1):
```

## Root Cause
This is an **off-by-one error**. Subtracting 1 from the list length causes the loop to skip the final element.

For example, a list containing 5 items has indices 0–4, but `range(4)` only generates 0–3.

## Solution
Remove `-1`:

```python
for i in range(len(items)):
```

This allows the loop to process every item in the list.

## Expected Output
For `[12, 8, 15, 6, 9]`:

```text
Total inventory: 50
```

## What I Learned
- `len()` counts the elements in a list.
- `range()` generates numbers up to, but not including, its stopping value.
- List indexing starts at 0.
- `+=` adds to the existing value of a variable.
- Functions can be defined once and called multiple times with different arguments.
- `return` sends a value back to the caller, while `print()` displays a value.
- Indentation determines whether statements execute inside or outside a loop.