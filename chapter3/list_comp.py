'''
结论

1. list comprehension 是比传统的 for loop 性能要好的
2. 不复杂的一层循环判断，且数据量不大的话，使用列表推导
3. 如果数据量大，使用列表生成式
'''
from timeit import timeit
from typing import Iterable, List


def remove_odd_mul_100(numbers: Iterable) -> List:
    result = []
    for number in numbers:
        if number % 2 == 1:
            continue
        result.append(number * 100)
    return result


def remove_odd_mul_100_v2(numbers: Iterable) -> List:
    return [number * 100 for number in numbers if number % 2 == 0]


def remove_odd_mul_100_v3(numbers: Iterable) -> Iterable:
    return (number * 100 for number in numbers if number % 2 == 0)


if __name__ == '__main__':
    numbers = [i for i in range(10000)]

    spend_time = timeit(
        setup='from __main__ import remove_odd_mul_100',
        stmt=f'remove_odd_mul_100({numbers})',
        number=10000,
    )
    print(spend_time)

    spend_time = timeit(
        setup='from __main__ import remove_odd_mul_100_v2',
        stmt=f'remove_odd_mul_100_v2({numbers})',
        number=10000,
    )
    print(spend_time)
    spend_time = timeit(
        setup='from __main__ import remove_odd_mul_100_v3',
        stmt=f'remove_odd_mul_100_v3({numbers})',
        number=10000,
    )
    print(spend_time)
