'''
结论

    python list 尾部插入性能非常好，但是首部插入的性能非常差（数据大一点的，首部插入的时候不建议使用）
    如果非要插入首部，使用 deque，也就是双端队列，使用 appendleft 进行插入，性能和 append 是差不多的
'''
from collections import deque
from timeit import timeit


def list_append():
    li = []
    for i in range(5000):
        li.append(i)


def list_insert():
    li = []
    for i in range(5000):
        li.insert(0, i)


def deque_insert():
    li = deque()
    for i in range(5000):
        li.appendleft(i)


if __name__ == '__main__':
    spend_time = timeit(
        setup='from __main__ import list_append', stmt='list_append()', number=10000
    )
    print(spend_time)

    spend_time = timeit(
        setup='from __main__ import deque_insert', stmt='deque_insert()', number=10000
    )
    print(spend_time)

    spend_time = timeit(
        setup='from __main__ import list_insert', stmt='list_insert()', number=10000
    )
    print(spend_time)
