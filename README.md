# Happy Numbers

A Python implementation to determine if a given integer is a "Happy Number".

## Mathematical Definition
A **happy number** is a number defined by the following process:
1. Starting with any positive integer, replace the number by the sum of the squares of its digits.
2. Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
3. Those numbers for which this process ends in 1 are happy numbers.

## Prerequisites
* Python 3.6 or higher

## Usage

You can use the `happy_num` function by importing it into your own Python scripts, or you can run the file directly to execute the built-in tests.

### Example

```python
from happy_numbers import happy_num

# Check if 19 is a happy number
result = happy_num(19)
print(f"Is 19 a happy number? {result}")  # Output: True

# Check if 123 is a happy number
result = happy_num(123)
print(f"Is 123 a happy number? {result}") # Output: False
```

## Running the Tests
The script includes simple `assert` statements at the bottom. To verify the logic is working correctly, simply run the script from your terminal:

```bash
python happy_numbers.py
```

If the script runs without outputting any errors, all tests have passed successfully.
