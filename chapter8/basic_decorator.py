import time


def timer(func):
    def decorated(*args, **kwargs):
        st = time.perf_counter()
        ret = func(*args, **kwargs)
        print('time cost {}'.format(time.perf_counter() - st))
        return ret

    return decorated


# timer(spend_func)
@timer
def spend_func():
    print('spend func')
    time.sleep(1)


if __name__ == '__main__':
    spend_func()
