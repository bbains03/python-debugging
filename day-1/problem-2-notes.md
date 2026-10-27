Problem 2: Tax Calculator

1. Problem Description

The program calculates the total price of a product after applying a 12% tax rate.

2. Expected Output

Total price: $112.0

3. Original Error

TypeError: unsupported operand type(s) for +: 'int' and 'str'

Original buggy code:

def calculate_total(price, tax_rate):
    total = price + (price * tax_rate)
    return total
product_price = 100
tax_rate = "0.12"
final_price = calculate_total(product_price, tax_rate)
print(f"Total price: ${final_price}")

4. Root Cause

The variable tax_rate was assigned "0.12", which Python interprets as a string rather than a numerical value.

When Python evaluates:

total = price + (price * tax_rate)

It first attempts to multiply an integer (100) by a string ("0.12").

Python repeats the string 100 times instead of calculating a numerical tax amount.

The program then attempts to add the integer 100 to the resulting string, producing a TypeError.

5. Solution

Changed the tax rate from a string to a float.

Before:

tax_rate = "0.12"

After:

tax_rate = 0.12

This allows Python to perform numerical multiplication and addition correctly.

6. Corrected Output

Total price: $112.0

7. Key Takeaways

* Strings and floats are different Python data types.
* Quotation marks determine whether a value is treated as a string.
* Multiplying a string by an integer repeats the string.
* A TypeError occurs when an operation is performed on incompatible data types.
* Reading error messages helps identify the cause of a programming issue.
* Testing corrected code verifies that the program produces the expected result.