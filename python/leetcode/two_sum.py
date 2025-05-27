def two_sum(nums, target):
    m = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in m:
            return [m[diff], i]
        m[num] = i
    return []
