# -*- coding: utf-8 -*-
"""Functions1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/19aABiPrCmU0wPWlURNN5fR5Iwrh-lx47
"""

def binary_search(arr, target, low, high):
    if low > high:
        return -1  # Element not found
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, high)
    else:
        return binary_search(arr, target, low, mid - 1)

array = [1, 3, 5, 7, 9, 11, 13]
target_value = 7
print(binary_search(array, target_value, 0, len(array) - 1))  # Output: 3

def binary_search(arr, target, low, high):
    if low > high:
        return -1  # Element not found
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, high)
    else:
        return binary_search(arr, target, low, mid - 1)

The function takes four arguments:

arr: The sorted array in which to perform the search.
target: The value you want to find within the array.
low: The current lower bound of the search range.
high: The current upper bound of the search range.
The function starts with an if condition:

If low is greater than high, it means the search range is invalid and the target element is not found in the array. In this case, the function returns -1 to indicate that the element is not found.
If the search range is valid, the function calculates the middle index (mid) of the current range using integer division //. This index will be used to compare the value at that position with the target.

The function then checks whether the value at the middle index (arr[mid]) is equal to the target:

If they are equal, it means the target has been found, and the function returns the mid index as the position of the target in the array.
If arr[mid] is less than the target, the function makes a recursive call to binary_search with an updated low bound (mid + 1) and the same high bound.
If arr[mid] is greater than the target, the function makes a recursive call to binary_search with an updated high bound (mid - 1) and the same low bound.
The recursion continues until the base case is reached, where the search range becomes invalid (low > high) or the target is found (arr[mid] == target).



array = [1, 3, 5, 7, 9, 11, 13]
target_value = 7
print(binary_search(array, target_value, 0, len(array) - 1))  # Output: 3



Basic Arithmetic:
python
Copy code
add = lambda x, y: x + y
print(add(5, 3))  # Output: 8
Square Function:
python
Copy code
square = lambda x: x ** 2
print(square(4))  # Output: 16
Even or Odd Check:
python
Copy code
is_even = lambda x: x % 2 == 0
print(is_even(6))  # Output: True
String Length Sorting:
python
Copy code
words = ['apple', 'banana', 'cherry']
words.sort(key=lambda word: len(word))
print(words)  # Output: ['apple', 'cherry', 'banana']
List Comprehension:
python
Copy code
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]
Filtering with Lambda:
python
Copy code
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4, 6, 8, 10]
Dictionary Sorting by Values:
python
Copy code
data = {'apple': 3, 'banana': 1, 'cherry': 2}
sorted_data = dict(sorted(data.items(), key=lambda item: item[1]))
print(sorted_data)  # Output: {'banana': 1, 'cherry': 2, 'apple': 3}
Using Lambda in Higher-Order Functions:
python
Copy code
def apply_operation(x, y, operation):
    return operation(x, y)

result = apply_operation(10, 5, lambda a, b: a * b)
print(result)  # Output: 50
Finding Maximum of a List:
python
Copy code
numbers = [12, 45, 9, 27, 6]
max_value = max(numbers, key=lambda x: x)
print(max_value)  # Output: 45
Custom Sorting:
python
Copy code
data = [('apple', 3), ('banana', 1), ('cherry', 2)]
data.sort(key=lambda item: item[1])
print(data)  # Output: [('banana', 1), ('cherry', 2), ('apple', 3)]
These examples showcase different ways you can use lambda expressions in Python for various tasks, including arithmetic operations, sorting, filtering, and working with higher-order functions.

. Squaring Numbers:

python
Copy code
numbers = [1, 2, 3, 4, 5]
squared = map(lambda x: x ** 2, numbers)
squared_list = list(squared)
print(squared_list)  # Output: [1, 4, 9, 16, 25]
2. Converting to Upper Case:

python
Copy code
words = ["apple", "banana", "cherry"]
uppercased = map(str.upper, words)
uppercased_list = list(uppercased)
print(uppercased_list)  # Output: ['APPLE', 'BANANA', 'CHERRY']
3. Calculating Length of Strings:

python
Copy code
words = ["apple", "banana", "cherry"]
lengths = map(len, words)
lengths_list = list(lengths)
print(lengths_list)  # Output: [5, 6, 6]
4. Doubling Numbers:

python
Copy code
numbers = [1, 2, 3, 4, 5]
doubled = map(lambda x: x * 2, numbers)
doubled_list = list(doubled)
print(doubled_list)  # Output: [2, 4, 6, 8, 10]
5. String Reversal:

python
Copy code
words = ["hello", "world", "python"]
reversed_words = map(lambda x: x[::-1], words)
reversed_list = list(reversed_words)
print(reversed_list)  # Output: ['olleh', 'dlrow', 'nohtyp']
6. Rounding Numbers:

python
Copy code
numbers = [3.14159, 2.71828, 1.41421]
rounded = map(round, numbers)
rounded_list = list(rounded)
print(rounded_list)  # Output: [3, 3, 1]
7. Negating Numbers:

python
Copy code
numbers = [1, -2, 3, -4, 5]
negated = map(lambda x: -x, numbers)
negated_list = list(negated)
print(negated_list)  # Output: [-1, 2, -3, 4, -5]
8. Checking for Even Numbers:

python
Copy code
numbers = [1, 2, 3, 4, 5]
is_even = map(lambda x: x % 2 == 0, numbers)
is_even_list = list(is_even)
print(is_even_list)  # Output: [False, True, False, True, False]
9. Adding Two Lists Element-wise:

python
Copy code
numbers1 = [1, 2, 3]
numbers2 = [10, 20, 30]
sums = map(lambda x, y: x + y, numbers1, numbers2)
sums_list = list(sums)
print(sums_list)  # Output: [11, 22, 33]
10. Converting to Strings:

python
Copy code
numbers = [1, 2, 3, 4, 5]
number_strings = map(str, numbers)
number_strings_list = list(number_strings)
print(number_strings_list)  # Output: ['1', '2', '3'



ertainly! Here are 5 examples of using the reduce() function in Python:

Note: Starting from Python 3.9, the reduce() function has been moved to the functools module. You need to import it before using it.

python
Copy code
from functools import reduce
1. Summing Numbers:

python
Copy code
numbers = [1, 2, 3, 4, 5]
sum_result = reduce(lambda x, y: x + y, numbers)
print(sum_result)  # Output: 15
2. Finding the Maximum Number:

python
Copy code
numbers = [3, 8, 2, 10, 5]
max_result = reduce(lambda x, y: x if x > y else y, numbers)
print(max_result)  # Output: 10
3. Concatenating Strings:

python
Copy code
strings = ["Hello", " ", "world", "!"]
concatenated = reduce(lambda x, y: x + y, strings)
print(concatenated)  # Output: "Hello world!"
4. Factorial Calculation:

python
Copy code
import math

n = 5
factorial = reduce(lambda x, y: x * y, range(1, n + 1))
print(factorial)  # Output: 120
5. Custom Aggregation:

python
Copy code
data = [2, 4, 6, 8, 10]
aggregated_result = reduce(lambda x, y: (x[0] + y, x[1] * y), data, (0, 1))
print(aggregated_result)  # Output: (30, 3840)
In these examples, the reduce() function is used to iteratively apply a given function to the elements of an iterable (like a list) in a cumulative manner. This gradually reduces the iterable to a single value or result. The examples cover various scenarios, such as basic arithmetic operations, string concatenation, and more complex custom aggregations.

