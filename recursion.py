"""
--------------------------------------------------------------------------------------------
Recursion Examples
--------------------------------------------------------------------------------------------
"""
import math

def recursive_factorial(num):
    return 1 if num == 1 else num * recursive_factorial(num - 1)

def sum_of_list(inp: list):
    return inp[0] + inp[1] if len(inp) == 2 else inp[0] + sum_of_list(inp[1:])

def fibonacci(inp: int):
    return 0 if inp == 0 \
        else 1 if (inp == 1 or inp == 2) \
        else (fibonacci(inp-1) + fibonacci(inp-2))

''' find max from a list of numbers'''
def my_max(inp: list):
    if len(inp) == 1:
        return inp[0]
    if len(inp) == 2:
        if inp[0] > inp[1]:
            return inp[0]
        else:
            return inp[1]
    l2 = my_max(inp[1:])
    if inp[0] > l2:
        return inp[0]
    else:
        return l2

''' convert a base-10 number to any base'''
def base10_to_any_base(n,base):
    base_chars = "0123456789ABCDEF"
    return base_chars[n] if n < base else base10_to_any_base(n//base, base) + base_chars[n % base]

''' -------------------------------------------------------------------------------------------- '''
if __name__ == '__main__':
    test_num = 10
    print('Math factorial:', math.factorial(test_num))
    print('recursive_factorial:', recursive_factorial(test_num))

    print('Add list usual:', sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    print('sum_of_list:', sum_of_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

    print('fibonacci:', [fibonacci(i) for i in range(0,11)])

    print('my_max:', my_max([4, 3, 0, -1, 10]))
    print('my_max:', my_max([4]))
    print('my_max:', my_max([3, 4]))
    print('my_max:', my_max([1, 0, 4, 3, 7, 6, 9, 14, 2, 4]))

    print('decimal_to_any_base:')
    print('2835, 16:', base10_to_any_base(2835, 16))
    print('34, 2:', base10_to_any_base(34, 2))