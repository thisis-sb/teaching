"""
--------------------------------------------------------------------------------------------
Recursion Examples
--------------------------------------------------------------------------------------------
"""
import math

def recursive_factorial(num):
    if num == 1:
        return 1
    else:
        return num * recursive_factorial(num - 1)

def sum_of_list(inp: list):
    if len(inp) == 2:
        return inp[0] + inp[1]
    return inp[0] + sum_of_list(inp[1:])

def fibonacci(inp: int):
    if inp == 0:
        return 0
    if inp == 1 or inp == 2:
        return 1
    return fibonacci(inp-1) + fibonacci(inp-2)

''' -------------------------------------------------------------------------------------------- '''
if __name__ == '__main__':
    test_num = 10
    print('Math factorial:', math.factorial(test_num))
    print('recursive_factorial:', recursive_factorial(test_num))

    print('Add list usual:', sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    print('sum_of_list:', sum_of_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

    print('fibonacci:', [fibonacci(i) for i in range(0,11)])