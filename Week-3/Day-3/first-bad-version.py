# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 0
        right = n
        pos = 0
        
        while left <= right:
            mid = left + (right - left) // 2
            if isBadVersion(mid):
                pos = mid;
                right = mid-1;
            else:
                left = mid+1;
                
        return pos