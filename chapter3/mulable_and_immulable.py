from typing import List


def add_str(in_func_obj: str) -> None:
    print(f'In add [before]: in_func_obj={in_func_obj}')
    in_func_obj += ' suffix'
    print(f'In add [after]: in_func_obj={in_func_obj}')


def add_list(in_func_obj: List) -> None:
    print(f'In add [before]: in_func_obj={in_func_obj}')
    in_func_obj += ['abc']
    print(f'In add [after]: in_func_obj={in_func_obj}')


if __name__ == '__main__':
    orig_str = 'foo'
    print(f'Outside [before]: origin_obj={orig_str}')
    add_str(orig_str)
    print(f'Outside [after]: origin_obj={orig_str}')

    print('-' * 20, '\n')

    orig_list = ['foo', 'bar']
    print(f'Outside [before]: origin_obj={orig_list}')
    add_list(orig_list)
    print(f'Outside [after]: origin_obj={orig_list}')
