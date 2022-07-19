print(list('foo'))

numbers = [1, 2, 3, 4]
print(numbers[2])
print(numbers[1:])
del numbers[1:]
print(numbers)

names = ['foo', 'bar']
for index, s in enumerate(names):
    print(index, s)
