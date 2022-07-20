from timeit import timeit
from typing import Dict

d1 = {'name': 'apple'}
d2 = {'price': 10}


def merge_dict(*dicts) -> Dict:
    result = {}
    for d in dicts:
        result.update(d)
    return result


def merge_dict_v2(*dicts) -> Dict:
    r: Dict = {}
    for d in dicts:
        r = r | d
    return r


def merge_dict_v3(d1: Dict, d2: Dict) -> Dict:
    result = d1.copy()
    result.update(d2)
    return result


def merge_dict_v4(d1: Dict, d2: Dict) -> Dict:
    return d1 | d2


if __name__ == '__main__':
    spend_time = timeit(setup='from __main__ import merge_dict, d1, d2', stmt='merge_dict(d1, d2)')
    print(spend_time)

    spend_time = timeit(
        setup='from __main__ import merge_dict_v2, d1, d2', stmt='merge_dict_v2(d1, d2)'
    )
    print(spend_time)

    spend_time = timeit(
        setup='from __main__ import merge_dict_v3, d1, d2', stmt='merge_dict_v3(d1, d2)'
    )
    print(spend_time)

    spend_time = timeit(
        setup='from __main__ import merge_dict_v4, d1, d2', stmt='merge_dict_v4(d1, d2)'
    )
    print(spend_time)

    spend_time = timeit(setup='from __main__ import d1, d2', stmt='{**d1, **d2}')
    print(spend_time)
