def twoSum(nums, target):
    hashMap = {}
    for i in range(len(nums)):
        complement = target - nums[i]

        if complement in hashMap:
            return  print([i, hashMap[complement]])
        hashMap[nums[i]] = i

    return print("false")


nums = [2, 9, 11, 15]
target = 9


twoSum(nums, target)