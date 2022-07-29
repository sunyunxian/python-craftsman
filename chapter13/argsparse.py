import argparse


def v1():
    parser = argparse.ArgumentParser()
    parser.parse_args()


def v2():
    parser = argparse.ArgumentParser()
    parser.add_argument('echo')
    args = parser.parse_args()
    print(args.echo)


def v3():
    parser = argparse.ArgumentParser()
    parser.add_argument('echo', help='echo the string you use here.')
    args = parser.parse_args()
    print(args.echo)


def v4():
    parser = argparse.ArgumentParser()
    parser.add_argument('square', help='display a square of a given number.', type=int)
    args = parser.parse_args()
    print(args.square**2)


def v5():
    parser = argparse.ArgumentParser()
    parser.add_argument('--verbosity', help='increase output verbosity')
    args = parser.parse_args()
    if args.verbosity:
        print('verbosity turn on')
        print(f'verbosity is {args.verbosity}')


def main():
    # v1()
    # v2()
    # v3()
    # v4()
    v5()


if __name__ == '__main__':
    main()
