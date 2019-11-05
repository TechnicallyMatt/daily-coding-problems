# Problem 1

# Given a list of numbers, return whether any two sums to k. For example, given [10, 15, 3, 7] and k of 17,
# return true since 10 + 7 is 17.
# Bonus: Can you do this in one pass?

import pytest


def pair_sums_to_k(num_list: list, k: int) -> bool:
    '''
    Use a hashset (python set()) which has, on average, constant lookup time.
    Then for each element of the list, we can check to see if the complement of
    k and it has been seen before by checking within the set. If the complement
    has not been seen, add the element itself to the set.

    This scales linearly, i.e. O(N)
    '''
    H = set()
    for n in num_list:
        if (k - n) in H:
            return True
        else:
            H.add(n)
    return False


@pytest.mark.parametrize(
    'num_list, k, answer',
    [
        ([10, 15, 3, 7], 17, True),
        ([10, 15, 3, 7], 6, False),
        ([1, 7, 3, -5, 99], 2, True),
        ([1, 7, 3, -5, 99], 3, False),
        ([5, 4, 3, 6, 7, 8, 5, -1, 99, 101, 1000, -9347], 4, True),
        ([5, 4, 3, 6, 7, 8, 5, -1, 99, 101, 1000, -9347], -347, False),
        ([], 0, False),
        ([], None, False),
    ],
)
def test_pair_sums_to_k(num_list, k, answer):
    assert pair_sums_to_k(num_list, k) == answer


if __name__ == '__main__':
    print('Solution to problem 1:')
