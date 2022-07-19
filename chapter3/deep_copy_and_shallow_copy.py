import copy

nums = [1, 2, 3, 4]
nums_copy = nums
nums[2] = 30
print(nums, nums_copy)

nums = [1, 2, 3, 4]
nums_copy = copy.copy(nums)
nums[2] = 30
print(nums, nums_copy)

# shallow copy
nums = [1, [1, 2, 3], 3, 4]  # type: ignore
nums_copy = copy.copy(nums)
nums[1].append(4)  # type: ignore
print(nums, nums_copy)

# deep copy

nums = [1, [1, 2, 3], 3, 4]  # type: ignore
nums_copy = copy.deepcopy(nums)
nums[1].append(4)  # type: ignore
print(nums, nums_copy)
