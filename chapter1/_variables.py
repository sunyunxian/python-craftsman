# encoding=utf-8

foo = 'foo'

bar: str = 'bar'

foo, bar = 'foo', 'bar'

foo, bar = 'bar', 'foo'

foo, bar = ['foo', 'bar']

foo, bar = ('foo', 'bar')

foo, bar = {'foo', 'bar'}

foo, *test, bar = ['foo', 'test1', 'test2', 'bar']

foo, _, bar = ['foo', 'test', 'bar']

foo, *_tmp, bar = ['foo', 'test1', 'test2', 'bar']
