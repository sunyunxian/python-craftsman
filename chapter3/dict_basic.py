from collections import OrderedDict

movies = {'name': 'Burning', 'type': 'movie', 'year': 2018}

print(movies['year'])

movies['rating'] = 10
print(movies)

movies['rating'] = 9
print(movies)

for key in movies:
    print(key)

for key, value in movies.items():
    print(key, value)

# 总是需要判断一个 dict 是否存在某个 key

if 'rating' in movies:
    rating = movies['rating']
else:
    rating = 0
print(rating)

del movies['rating']
try:
    rating = movies['rating']
except KeyError:
    rating = 0
print(rating)

# 更好的 api

rating = movies.get('rating', 0)
print(rating)

# 任何时候都需要先判断一下 key 是否存在，这是一个非常 fuck 的事情
#   先判断 key 是否存在
#   存在，直接添加
#   不存在，先初始化一个 key，并添加
#   而使用 setdefault 可以减少一个判断的步骤，这样子就可以了
d = {'title': 'foobar'}
try:
    d['item'].append('foo')  # type: ignore
except KeyError:
    d['item'] = 'foo'
print(d)

d = {'title': 'foobar'}

d.setdefault('item', []).append('foo')  # type: ignore
print(d)

d.setdefault('item', []).append('bar')  # type: ignore
print(d)

# 删除键
# 还是想要判断 key 是否存在，直接使用 pop 可以免除这个问题
try:
    del d['key']
except KeyError:
    print('Key is not exist')

print(d.pop('key', None))

# 字典推导式

d = {'foo': '1', 'bar': '2'}

d = {key: value for key, value in d.items() if key == 'foo'}
print(d)

li = ['foo', 'bar']
li_d = {i: v for i, v in enumerate(li)}
print(li_d)

d1 = OrderedDict()
d1['First key'] = 1
d1['Second key'] = 2
print(d1)
for key in d1:
    print(key)

d2 = {}
d2['First key'] = 1
d2['Second key'] = 2
print(d2)
for key in d2:
    print(key)

# 如果顺序不相等
d3 = OrderedDict()
d3['Second key'] = 2
d3['First key'] = 1
print(d3)

d4 = {}
d4['Second key'] = 2
d4['First key'] = 1
print(d4)

print(d1 == d2)
print(d1 == d3)
print(d1 == d4)

# 结论
# OrderedDict 和 OrderedDict 对比的时候才会进行位置的对比
# 而 OrderedDict 和 dict 对比的时候不会进行位置对比，只要是 key value 相等，永远是相等的
