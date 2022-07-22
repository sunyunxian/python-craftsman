from enum import Enum


class PagePerlLevel(str, Enum):
    LT_100 = 'Less than 100 ms'
    LT_300 = 'Between 100 and 300 ms'
    LT_1000 = 'Between 300 ms and 1 s'
    GT_1000 = 'Greater than 1 s'


def analyzer_log(file):
    paths_group = {}

    with open(file) as fp:
        for i in fp:
            path, response_time_str = i.strip().split(' ')

            response_time = int(response_time_str)
            if response_time < 100:
                level = PagePerlLevel.LT_100
            elif response_time < 300:
                level = PagePerlLevel.LT_300
            elif response_time < 1000:
                level = PagePerlLevel.LT_1000
            else:
                level = PagePerlLevel.GT_1000

            if path not in paths_group:
                paths_group[path] = {}

            try:
                paths_group[path][level] += 1
            except KeyError:
                paths_group[path][level] = 1

    for path, result in paths_group.items():
        print(f'==Path: {path}')
        total = sum(result.values())
        print(f'    Total requests: {total}')
        print('    Performance:')

        sorted_items = sorted(result.items(), key=lambda pair: list(PagePerlLevel).index(pair[0]))
        for level_name, count in sorted_items:
            print(f'    - {level_name} : {count}')


if __name__ == '__main__':
    analyzer_log('logs.txt')
