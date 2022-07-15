# encoding=utf-8
'''
1. 变量名字变成了可读性的有意义的名字，而不是 i，j，k
2. 增加了有意义的临时变量：current next_ should_swap
3. 增加了类型注释和函数的表述、接口文档，并在交换的时候写了注释，表明了交换的原因
'''
from typing import List


def my_magic_bubble_sort(numbers):
    # 我的第一本能解法
    length = len(numbers)

    for i in range(length):
        length = length - 1
        for i in range(length):
            if numbers[i] > numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]

    return numbers


def my_second_bubble_sort(numbers: List[int]) -> List[int]:
    '''冒泡排序
    :param numbers: 需要排序的列表，函数会直接修改原始列表
    '''
    stop_position = len(numbers) - 1
    while stop_position > 0:
        for i in range(stop_position):
            current, next_ = numbers[i], numbers[i + 1]
            should_swap = False
            # 前面大于后面就进行交换
            if current > next_:
                should_swap = True
            if should_swap:
                numbers[i], numbers[i + 1] = next_, current
        stop_position -= 1
    return numbers


def r_magic_bubble_sort(numbers):
    '''R 的解法
    默认认为偶数比奇数大
    '''
    j = len(numbers) - 1
    while j > 0:
        for i in range(j):
            if numbers[i] % 2 == 0 and numbers[i + 1] % 2 == 1:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                continue
            elif (numbers[i] % 2 == numbers[i + 1] % 2) and numbers[i] > numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                continue
        j -= 1
    return numbers


def magic_bubble_sort(numbers: List[int]) -> List[int]:
    '''有魔力的冒泡排序，默认偶数比奇数大
    :param number: 需要排序的数组，函数会直接修改原有的数组
    '''
    stop_position = len(numbers) - 1
    while stop_position > 0:
        for i in range(stop_position):
            current, next_ = numbers[i], numbers[i + 1]
            current_is_even, next_is_even = numbers[i] % 2 == 0, numbers[i + 1] % 2 == 0
            should_swap = False
            # 交换位置的条件
            # - 前面是偶数，后面是奇数
            # - 前后都是奇数或者偶数，但是前面的比后面的大
            if current_is_even and not next_is_even:
                should_swap = True
            elif current_is_even == next_is_even and current > next_:
                should_swap = True
            if should_swap:
                current, next_ = next_, current
        stop_position -= 1

    return numbers


if __name__ == '__main__':
    numbers = [23, 32, 1, 3, 4, 19, 20, 2, 4]
    magic_bubble_sort(numbers)
    print(r_magic_bubble_sort(numbers))
    print(magic_bubble_sort(numbers))
    print(my_second_bubble_sort(numbers))
