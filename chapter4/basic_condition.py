s = ''

if s == True:  # NOQA
    print('s is True')
else:
    print('s is False')

if s:
    print('s is True')
else:
    print('s is False')

# not 放到表达式中，以及如果本身的表达式能表达意思，尽量少使用


# 三元表达式
class Foo:
    def __init__(self) -> None:
        self.like = 'dynamic'


language = 'Python' if Foo().like == 'dynamic' else 'Golang'
print(language)

# 真值和假值的原因


class FooSecond:
    pass


print(bool(FooSecond))
print(bool(FooSecond()))


class Bar:
    def __init__(self, item=None) -> None:
        if not item:
            self.item = []
        else:
            self.item = item

    def __len__(self):
        return len(self.item)


print(Bar)
print(bool(Bar()))  # 这个默认就是 False
print(bool(Bar(['1'])))
print(bool(Bar()))


class BarSecond:
    def __eq__(self, other: object) -> bool:
        # 只有 0 和 1 才相等
        if other == 0 or other == 1:
            return True
        return False


# 注意，必须先实例化对象
print(BarSecond() == 0)  # True
print(BarSecond() == 1)  # True
print(BarSecond() == 2)  # True
