"""
--------------------------------------------------------------------------------------------
character permutation - itertools.permutations vs. loop method vs. recursion
--------------------------------------------------------------------------------------------
"""


def loop_method(n):
    result = []
    final_list = []
    list_temp = []

    alphabets = []
    for letter in n:
        alphabets.append(letter)

    distinct_alphabets = set(alphabets)
    final_single_alphabets = list(distinct_alphabets)
    final_single_alphabets.sort()

    # adding 1 letter word
    for x in final_single_alphabets:
        final_list.append(x)

    if len(n) > 1:
        # adding 2 letters words
        for i in range(0, len(final_single_alphabets)):
            temp_list = list(final_single_alphabets)
            item = temp_list.pop(i)
            for j in temp_list:
                value = item + j
                final_list.append(value)
                list_temp.append(value)

        if len(n) > 2:
            i = 2
            while i < len(final_single_alphabets):
                l1 = list(final_single_alphabets)
                for a in l1:
                    for b in list_temp:
                        if len(b) == i:
                            if a not in b:
                                element = a + b
                                final_list.append(element)
                        else:
                            continue
                list_temp = final_list
                i += 1
            '''for final in final_list:
                print(final)'''
            [result.append(r) for r in final_list]
        else:
            '''for final in final_list:
                print(final)'''
            [result.append(r) for r in final_list]
    else:
        '''for final in final_list:
            print(final)'''
        [result.append(r) for r in final_list]

    return result

def recursive_method(inp: list):
    if len(inp) == 2:
        return [inp[0], (inp[0] + inp[1]), inp[1], (inp[1] + inp[0])]

    res = []
    for c1 in inp:
        r1 = recursive_method([c2 for c2 in inp if c2 != c1])
        res = res + [c1] + [c1+c3 for c3 in r1]

    return sorted(list(set(res)))

''' -------------------------------------------------------------------------------------------- '''
if __name__ == '__main__':
    import itertools
    import time

    test_str = 'abcdefghi'
    char_list = sorted(list(set(test_str)))

    t0 = time.time()
    expected_result = []
    for r in range(1,len(char_list)+1):
        perms = [''.join(t) for t in list(itertools.permutations(char_list, r=r))]
        [expected_result.append(p) for p in perms]
    expected_result = sorted(list(set(expected_result)))
    '''print('expected_result:', expected_result)'''
    print('python.itertools: time taken:', round(time.time() - t0, 2))

    t0 = time.time()
    loop_result = sorted(list(set(loop_method(char_list))))
    print('\nperm_loop_method: Test passed') if expected_result == loop_result \
        else 'perm_loop_method: Test Failed'
    print('time taken:', round(time.time() - t0, 2))

    t0 = time.time()
    rec_result = sorted(list(set(recursive_method(char_list))))
    print('\nperm_recursive_method: Test passed') if expected_result == rec_result \
        else 'perm_recursive_method: Test Failed'
    print('time taken:', round(time.time() - t0, 2))




