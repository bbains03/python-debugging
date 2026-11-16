# Problem 6: Shopping Cart Calculator — Assignment vs. Accumulation

## 1. Original Bug

The shopping cart calculator was supposed to add all item prices together, but it only returned the last item's price.

**Original buggy code:**

```python
def calculate_total(prices):
    total = 0

    for price in prices:
        total = price

    return total
```

**Input:** `[20, 35, 15]`

**Incorrect output:** `Cart total: $15`

**Expected output:** `Cart total: $70`

## 2. Why the Error Occurred

The problem was this line:

```python
total = price
```

The assignment operator (`=`) replaces the previous value of `total` with the current value of `price`.

During the loop:

- First iteration: `total = 20`
- Second iteration: `total = 35`
- Third iteration: `total = 15`

Because each iteration overwrote the previous value, the function returned only the last price.

This was a **logic error**, not a syntax error. Python executed the code successfully, but the result was incorrect.

## 3. How I Fixed It

I changed:

```python
total = price
```

To:

```python
total += price
```

The `+=` operator adds the current price to the existing total.

It is equivalent to:

```python
total = total + price
```

The corrected loop accumulates the prices:

- First iteration: `0 + 20 = 20`
- Second iteration: `20 + 35 = 55`
- Third iteration: `55 + 15 = 70`

**Correct output:** `Cart total: $70`

## 4. Testing

| Input | Expected result |
|---|---|
| `[20, 35, 15]` | `$70` |
| `[10, 20, 30]` | `$60` |
| `[100]` | `$100` |
| `[]` | `$0` |

The original input was tested successfully after the correction. The other inputs are additional test cases to verify.

## 5. What I Learned

- `=` assigns a value to a variable, replacing its previous value.
- `==` compares two values and evaluates to `True` or `False`.
- `+=` adds a value to the existing variable and stores the result.
- A `for` loop processes each element in a list individually.
- Assignment does not automatically select the larger number.
- Assigning one variable to another does not permanently link their values.
- Logic errors can produce incorrect outputs without raising exceptions.

## 6. Key Takeaway

When calculating a running total, use an accumulation operation rather than repeatedly overwriting the variable.

Understanding how values change during each loop iteration makes it easier to identify and fix logic errors.