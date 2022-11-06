"""
--------------------------------------------------------------------------------------------
Math methods
--------------------------------------------------------------------------------------------
"""

def decimal2binary(number):
    """
    :param number: integer base10 number to convert. Current restriction: must be >= 0
    :return: binary value in string format preceded by '0b'
    """

    bin_value = ''
    while number > 0:
        next_digit = number % 2
        number = (number - next_digit)/2
        bin_value = '%d%s' % (next_digit, bin_value)

    return '0b0' if bin_value == '' else '0b' + bin_value

''' -------------------------------------------------------------------------------------------- '''
if __name__ == '__main__':
    for num in [0, 5, 8, 12, 13, 22, 23, 30, 31]:
        print('bin value of %d is %s' % (num, decimal2binary(num)))

    ''' Proper testing '''
    print()
    n_failed = 0
    for n in range(10000):
        bn = decimal2binary(n)
        if bn != str(bin(n)):
            print('Test for %d failed, expected %s, got %s' % (n, bin(n), bn))
            n_failed += 1

    print('All tests passed') if n_failed == 0 else print('ERROR! %d tests failed' % n_failed)