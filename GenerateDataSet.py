import random


def convert_to_base_ten(number: list):
    total = 0
    place = 1
    for val in reversed(number):
        total += place * val
        place *= 2

    return total


def get_data_set(bits: int):
    first = [random.randint(0, 1) for x in range(bits)]
    second = [random.randint(0, 1) for x in range(bits)]
    addition = add_binary_numbers(first, second)

    if convert_to_base_ten(addition) != convert_to_base_ten(first) + convert_to_base_ten(second):
        raise ValueError("there was a mistake in addition")

    return [first, second, addition]


def add_binary_numbers(first: list, second: list):
    addition = []
    carry = 0
    for fir, sec in zip(reversed(first), reversed(second)):
        val = fir + sec + carry
        if val == 0:
            addition.append(0)
            carry = 0
        elif val == 1:
            addition.append(1)
            carry = 0
        elif val == 2:
            addition.append(0)
            carry = 1
        else:
            addition.append(1)
            carry = 1

    addition.append(carry)
    addition.reverse()
    return addition
