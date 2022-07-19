'''
结论
使用生成器的速度要远远大于直接生成，差距巨大，内存上也是生成器远远小于直接生成
在调用的时候，速度上差距没有这么大，但是内存还是远远大于的

直接生成存在问题
1. 流程上：初始化容器 - 处理 - 结果放入容器 - 返回容器
2. 每次都要全部处理完成才能调用，这会消耗过多的时间（当然生成器也会消耗类似的事件）
    2.1 但是如果调用方是按需生成，比如需要一部分，这个时候生成了全部完全就是浪费资源
3. 结果过多的时候，存放结果的容器内存占用过大
'''
from timeit import timeit


def gen_even_v1(max_number: int):
    r = []
    for i in range(max_number):
        if i % 2 == 0:
            r.append(i)
    return r


def use_gen_even_v1(max_num: int):
    list(gen_even_v1(max_num))


def gen_even_v2(max_number: int):
    for i in range(max_number):
        if i % 2 == 0:
            yield i


def use_gen_even_v2(max_num: int):
    list(gen_even_v2(max_num))


if __name__ == '__main__':
    max_number = 1000

    spend_time = timeit(
        setup='from __main__ import gen_even_v1', stmt=f'gen_even_v1({max_number})', number=100000
    )
    print(spend_time)
    spend_time = timeit(
        setup='from __main__ import gen_even_v2', stmt=f'gen_even_v2({max_number})', number=100000
    )
    print(spend_time)

    spend_time = timeit(
        setup='from __main__ import use_gen_even_v1',
        stmt=f'use_gen_even_v1({max_number})',
        number=100000,
    )
    print(spend_time)
    spend_time = timeit(
        setup='from __main__ import use_gen_even_v2',
        stmt=f'use_gen_even_v2({max_number})',
        number=100000,
    )
    print(spend_time)
