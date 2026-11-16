# Problem 7 — Finding the Highest Number

## 1. The Bug
The function initialized `highest = 0`, which caused incorrect results when every number in the list was negative.

**Original input:**
```python
scores = [-10, -5, -20, -3]
```

**Incorrect output:** `0`

**Expected output:** `-3`

## 2. Why the Bug Happened
- Python started with `highest = 0`.
- The `for` loop compared every number against `highest`.
- Since every number was negative, none was greater than `0`.
- The `if` condition was always false, so `highest` never changed.

## 3. How I Fixed It
I changed the initialization to:

```python
highest = numbers[0]
```

This starts with the first element of the input list instead of a hardcoded number.

The loop then compares each number and updates `highest` whenever it finds a larger value.

## 4. What I Learned
- `numbers[0]` accesses the first element of a list because Python indexing starts at zero.
- Hardcoding a value like `-20` is different from selecting a position like `numbers[0]`.
- A `for` loop