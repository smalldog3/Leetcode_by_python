# coding: utf-8

'''
Write a program to find the nth super ugly number.

Super ugly numbers are positive numbers whose all prime factors are in the given prime list primes of size k.
For example, [1, 2, 4, 7, 8, 13, 14, 16, 19, 26, 28, 32]
is the sequence of the first 12 super ugly numbers given primes = [2, 7, 13, 19] of size 4.

Note:
(1) 1 is a super ugly number for any given primes.
(2) The given numbers in primes are in ascending order.
(3) 0 < k ≤ 100, 0 < n ≤ 106, 0 < primes[i] < 1000.
'''
import sys
class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        size = len(primes)
        times = [0] * size
        uglys = [0] * n
        uglys[0] = 1
        for i in range(1, n):
            minValue = sys.maxint
            for j in range(0, size):
                minValue = min(minValue, primes[j] * uglys[times[j]])
            uglys[i] = minValue
            for j in range(0, size):
                if uglys[times[j]] * primes[j] == minValue:
                    times[j] += 1
        return uglys[n - 1]

solution = Solution()
print solution.nthSuperUglyNumber(12, [2, 7, 13, 19])
