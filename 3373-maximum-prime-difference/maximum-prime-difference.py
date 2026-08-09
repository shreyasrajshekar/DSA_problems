class Solution(object):
    def maximumPrimeDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def isPrime(n):
            if n < 2:
                return False
            
            i = 2
            while i * i <= n:
                if n % i == 0:
                    return False
                i += 1
            
            return True

        first = -1
        last = -1

        for i in range(len(nums)):
            if isPrime(nums[i]):
                if first == -1:
                    first = i
                last = i

        return last - first