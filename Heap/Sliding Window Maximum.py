# coding: utf-8

'''
Given an array nums, there is a sliding window of size k
which is moving
from the very left of the array to the very right.
You can only see the k numbers in the window.
Each time the sliding window moves right by one position.

For example,
Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Therefore, return the max sliding window as [3,3,5,5,6,7].

Note:
You may assume k is always valid,
ie: 1 ≤ k ≤ input array's size for non-empty array.
'''
from collections import deque

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        q = deque()
        result = []
        if len(nums) < k or k == 0:
            return []

        n = len(nums)
        for i in range(n):
            while len(q) and nums[q[-1]] < nums[i]:
                q.pop()
            q.append(i)
            if i < k - 1:
                continue
            while len(q) and q[0] <= i - k:
                q.popleft()
            result.append(nums[q[0]])

        return result

nums = [1,3,-1,-3,5,3,6,7]
solution = Solution()
print solution.maxSlidingWindow(nums, 3)
