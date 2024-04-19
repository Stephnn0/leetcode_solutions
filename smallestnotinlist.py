# Given an unsorted integer array nums. Return the smallest positive integer that is not present in nums.
# You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.


def firstMissingPositive(nums) -> int:
        num_set = set(nums)

        print(num_set)
        
        for i in range(1, len(nums)+2):
            print(i, 'current index')
            if i not in num_set:
                return i




# nums = [1, 2, 0]
# nums = [3, 4, -1, 1]
nums = [7,8,9,11,12]
x = firstMissingPositive(nums)

print(x)
