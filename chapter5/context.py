from contextlib import contextmanager


@contextmanager
def test_contextmanager():
    print(f"Gen con\n{'-' * 20}")
    # 创建一个假的连接数据
    con = {'User': 'foo', 'Password': 'bar'}
    yield con
    print(f"Del con\n{'-' * 20}")
    del con


if __name__ == '__main__':
    with test_contextmanager() as con:
        for k, v in con.items():
            print(f'{k} is {v}')
