'''
结论

1. 如果是大量的需要 in 判断的代码，转成 set 性能会非常快
2. 转换的时候需要注意：set() 的开销是非常大的，保证一次转换，多次使用才是正确的使用方式
'''

from random import randint
from timeit import timeit

randint_list = [''.join([str(randint(0, 9)) for i in range(6)]) for i in range(10000)]
randint_set = set([''.join([str(randint(0, 9)) for i in range(6)]) for i in range(10000)])


def list_check(list_data, check_number: str = '1'):
    if check_number in list_data:
        print('In')


def set_check(set_data, check_number: str = '1'):
    if check_number in set_data:
        print('In')


if __name__ == '__main__':
    spend_time = timeit(
        setup='from __main__ import list_check, randint_list',
        stmt='list_check(randint_list)',
        number=10000,
    )
    print(spend_time)

    spend_time = timeit(
        setup='from __main__ import set_check, randint_set',
        stmt='set_check(randint_set)',
        number=10000,
    )
    print(spend_time)
