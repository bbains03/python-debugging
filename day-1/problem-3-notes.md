# Problem 3: Grade Calculator

## 1. Problem Description

The program determines a student's letter grade based on their numerical exam score using conditional statements.

## 2. Expected Output

```text
Student grade: B
```

## 3. Original Output

```text
Student grade: D
```

## 4. Original Bug

```python
if score >= 60:
    return "D"
elif score >= 70:
    return "C"
elif score >= 80:
    return "B"
elif score >= 90:
    return "A"
else:
    return "F"
```

## 5. Root Cause

The conditions were arranged in the wrong order.

Python evaluates an `if`/`elif` chain from top to bottom and executes the first condition that evaluates to `True`.

When the student's score was 85, the first condition (`score >= 60`) was already satisfied. Therefore, Python returned `"D"` without evaluating the remaining conditions.

This was a logic error rather than a syntax or runtime error.

## 6. Solution

Reordered the conditions to evaluate the highest grade thresholds first.

```python
if score >= 90:
    return "A"
elif score >= 80:
    return "B"
elif score >= 70:
    return "C"
elif score >= 60:
    return "D"
else:
    return "F"
```

## 7. Corrected Output

```text
Student grade: B
```

## 8. Key Takeaways

- Python evaluates `if`/`elif` conditions sequentially.
- Only the first matching branch executes.
- The order of conditions can affect program behavior.
- Logic errors can produce incorrect results without generating Python exceptions.
- Logical operators such as `and` can be used to define more specific conditions.
- Testing expected outputs is essential for identifying logic errors.