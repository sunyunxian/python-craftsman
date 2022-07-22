fruits = {'apple', 'orange', 'apple', 'pineapple'}
print(fruits)

# 创建
empty_set = set()  # type:ignore
print(empty_set)

# 推导式
nums = [1, 2, 2, 4, 1]
nums_set = {num for num in nums if num < 3}
print(nums_set)

# api
nums_set = {num for num in range(1, 10)}
print(nums_set)
print(nums_set.add(10))  # type: ignore
print(nums_set)
print(nums_set.pop())
print(nums_set)
print(nums_set.remove(2))  # type: ignore
print(nums_set)
print(nums_set.discard(2))  # type: ignore
print(nums_set)
try:
    nums_set.remove(2)
except KeyError:
    print('Not exist 2')

frozen_s = frozenset([1, 2, 3])
print(frozen_s)
