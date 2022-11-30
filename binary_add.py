"""
--------------------------------------------------------------------------------------------
add 2 binary numbers whose digits are represented as a list
--------------------------------------------------------------------------------------------
"""


def add_digit(d1, d2, carry):
    if d1 == 0 and d2 == 0:
        return [0, 0] if carry == 0 else [0, 1]
    elif (d1 == 0 and d2 == 1) or (d1 == 1 and d2 == 0):
        return [0, 1] if carry == 0 else [1, 0]
    else:  # d1 & d2 = 1
        return [1, 0] if carry == 0 else [1, 1]

def add_binary_as_list(n1, n2):
    # firstly: make sure len(n1) == len(n2) by adding 0's to the smaller one
    if len(n1) < len(n2):
        n1 = [0] * (len(n2) - len(n1)) + n1
    elif len(n1) > len(n2):
        n2 = [0] * (len(n1) - len(n2)) + n2

    # add a 0 at the start of each in case last carry is 1
    n1 = [0] + n1
    n2 = [0] + n2

    carry = 0
    resulting_sum = [0] * len(n1)
    for i in reversed(range(0, len(n1))):
        pos_sum = add_digit(n1[i], n2[i], carry)
        resulting_sum[i] = pos_sum[1]
        carry = pos_sum[0]

    # drop most significant digit if it is 0
    return resulting_sum[1:] if resulting_sum[0] == 0 else resulting_sum

''' -------------------------------------------------------------------------------------------- '''
if __name__ == '__main__':
    n1 = [1, 0, 1, 1]  # decimal 11
    n2 = [1, 1, 0, 1]  # decimal 13
    exp_result = [1, 1, 0, 0, 0]
    act_result = add_binary_as_list(n1, n2)
    print('OK') if act_result == exp_result else \
        print('Something went wrong, expected: %s, got: %s'
              % (exp_result, act_result))

    n1 = [1, 0]  # decimal 2
    n2 = [0, 1]  # decimal 3
    exp_result = [1, 1]
    act_result = add_binary_as_list(n1, n2)
    print('OK') if act_result == exp_result else \
        print('Something went wrong, expected: %s, got: %s'
              % (exp_result, act_result))

    n1 = [1, 1, 1]  # decimal 7
    n2 = [1, 1, 1]  # decimal 7
    exp_result = [1, 1, 1, 0]
    act_result = add_binary_as_list(n1, n2)
    print('OK') if act_result == exp_result else \
        print('Something went wrong, expected: %s, got: %s'
              % (exp_result, act_result))

    n1 = [1, 0, 5]  # decimal 5
    n2 = [1, 1, 0, 1]  # decimal 13
    exp_result = [1, 0, 0, 1, 0]
    act_result = add_binary_as_list(n1, n2)
    print('OK') if act_result == exp_result else \
        print('Something went wrong, expected: %s, got: %s'
              % (exp_result, act_result))