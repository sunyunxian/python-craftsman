from typing import Union


def incr_by_one(value: Union[int, str]) -> Union[int, None]:  # type: ignore

    if isinstance(value, int):
        return value + 1

    elif isinstance(value, str) and value.isdigit():
        return int(value) + 1
    else:
        print(f'Unable to perform incr for value: {value}')
        return None


def incr_by_one_v2(value: Union[int, str]) -> Union[int, None]:

    try:
        return int(value) + 1
    except (TypeError, ValueError) as e:
        print(f'Unable to perform incr for value: {value}, error: {e}')
        return None


if __name__ == '__main__':
    incr_by_one(10)
    incr_by_one('10')
    incr_by_one('foo')

    incr_by_one_v2(10)
    incr_by_one_v2('10')
    incr_by_one_v2('foo')

    # spend_time = timeit(
    #     setup='from __main__ import incr_by_one', stmt="incr_by_one(1)\nincr_by_one('1')\nincr_by_one('foo')"
    # )
    # print(spend_time)
    # spend_time = timeit(
    #     setup='from __main__ import incr_by_one_v2',
    #     stmt="incr_by_one_v2(1)\nincr_by_one_v2('1')\nincr_by_one_v2('foo')",
    # )
    # print(spend_time)
