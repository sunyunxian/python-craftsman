from typing import Iterable


def all_number_gt_10(nums: Iterable) -> bool:
    if not nums:
        return False

    for i in nums:
        if i <= 10:
            return False
    return True


def all_number_gt_10_v2(nums: Iterable) -> bool:

    return bool(nums) and all(n > 10 for n in nums)


if __name__ == '__main__':
    nums = [11, 10, 199]
    print(all_number_gt_10(nums))
    print(all_number_gt_10_v2(nums))
