""""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

"""

"""Brute force approach"""
def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    a+b+c = 0  => -a = b+c
    """
    nums = sorted(nums, key=int)
    ans = [] # return ans
    arr = [] # append arr to ans for possible triplets
    nums = sorted(nums, key=int)
    lookup = {}
    for i in range(len(nums)):
        a = nums[i]
        target = -a
        for j in range(i+1, len(nums)):
            b = nums[j]
            if (target-b) in lookup:
                arr.append(a)
                arr.append(nums[lookup[target-b]])
                arr.append(b)
                ans.append(arr)
                arr = []
            lookup[b] = j
        lookup = {}
    res = []
    for i in ans:
        if i not in res:
            res.append(i)

    return res




nums = [-1, 0, 1, 2, -1, -4]
answer = threeSum(nums)
print(answer)

