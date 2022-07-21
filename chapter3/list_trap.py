from typing import List


def remove_even(numbers: List) -> List:
    for number in numbers:
        if number % 2 == 0:
            numbers.remove(number)

    return numbers


def remove_even_v2(numbers: List) -> List:
    result = []
    for number in numbers:
        if number % 2 != 0:
            result.append(number)

    return result


numbers = [1, 2, 7, 4, 8, 11]
print(remove_even(numbers))
numbers = [1, 2, 7, 4, 8, 11]
print(remove_even_v2(numbers))
