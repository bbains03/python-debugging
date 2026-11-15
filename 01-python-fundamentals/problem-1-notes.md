Problem 1: Weekly Earnings Calculator

1. Problem Description

The program calculates an employee’s weekly earnings by multiplying the number of hours worked by their hourly pay rate.

2. Expected Output

Weekly earnings: $1000

3. Original Bug

hours_worked = "40"
pay_rate = 25

The number of hours worked was stored as a string instead of an integer.

4. Root Cause

Python interprets "40" as a string rather than a numerical value.

Multiplying a string by an integer repeats the string instead of performing mathematical multiplication.

For example:

print("40" * 3)

Output:

404040

As a result, the program produced an incorrect earnings calculation.

5. Solution

Changed the hours worked from a string to an integer:

hours = 40
hourly_rate = 25

This allowed Python to perform numerical multiplication.

6. Corrected Output

Weekly earnings: $1000

7. Key Takeaways

* Strings and integers are different Python data types.
* Quotation marks determine whether a value is interpreted as a string.
* Multiplying a string by an integer causes string repetition.
* Understanding data types is essential when debugging arithmetic operations.
* Git commits can preserve both the original buggy code and the corrected solution.