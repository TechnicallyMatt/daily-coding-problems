# Problem 2

# Given an array of integers, return a new array such that each element at index i of the new array is the
# product of all the numbers in the original array except the one at i.

# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24].
# If our input was [3, 2, 1], the expected output would be [2, 3, 6].

# Follow-up: what if you can't use division?

import pytest
from timeit import timeit


def array_product_func(input_array):
    '''
    complexity: O(N)
    '''
    product = 1
    for k in input_array:
        product = k * product
        output_array = []
    for i in input_array:
        output_array.append(product / i)
    return output_array


@pytest.mark.parametrize(
    'input_array, output_array', [([1, 2, 3, 4, 5], [120, 60, 40, 30, 24]), ([1, 2, 3, 4, 5], [120, 60, 40, 30, 24])]
)
def test_array_product_func(input_array, output_array):
    assert array_product_func(input_array) == output_array
