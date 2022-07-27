class MyError(Exception):
    def __init__(self, exc, *args: object) -> None:
        self.exc = exc
        super().__init__(f'This is my Error {self.exc}', *args)


def use_my_error():

    try:
        with open('use_my_error.txt') as f:
            for i in f:
                print(i)
    except Exception as e:
        raise MyError(exc=e)


class MyErrorTwo(Exception):
    '''my Error two'''


def use_my_error_two():
    try:
        with open('use_my_error_two') as e:
            print(e)
    except Exception as e:
        print(e)
        raise MyErrorTwo


if __name__ == '__main__':
    use_my_error()
    use_my_error_two()
