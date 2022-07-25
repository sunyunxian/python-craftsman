li = ['foo', 'bar']

iter_l = iter(li)

try:
    while True:
        print(next(iter_l))
except StopIteration as e:
    print(f'Has error: StopIteration{e}')
