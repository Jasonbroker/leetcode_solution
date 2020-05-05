#
# @lc app=leetcode id=220 lang=python3
#
# [220] Contains Duplicate III
#
# https://leetcode.com/problems/contains-duplicate-iii/description/
#
# algorithms
# Medium (20.62%)
# Likes:    956
# Dislikes: 996
# Total Accepted:    117.1K
# Total Submissions: 566.8K
# Testcase Example:  '[1,2,3,1]\n3\n0'
#
# Given an array of integers, find out whether there are two distinct indices i
# and j in the array such that the absolute difference between nums[i] and
# nums[j] is at most t and the absolute difference between i and j is at most
# k.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,2,3,1], k = 3, t = 0
# Output: true
# 
# 
# 
# Example 2:
# 
# 
# Input: nums = [1,0,1,1], k = 1, t = 2
# Output: true
# 
# 
# 
# Example 3:
# 
# 
# Input: nums = [1,5,9,1,5,9], k = 2, t = 3
# Output: false
# 
# 
# 
# 
#
# [1,5,9,1,5,9]\n2\n3
# @lc code=start
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        # 简单的方法，和II一样，查找表+ 区间
        if k < 1 or t < 0: return False
        dic = collections.OrderedDict()
        for n in nums:
            key = n if not t else n // t
            print(key)
            for m in (dic.get(key - 1), dic.get(key), dic.get(key + 1)):
                if m is not None and abs(n - m) <= t:
                    return True
                if len(dic) == k:
                    dic.popitem(False)
            dic[key] = n
        return False
        # 桶排序
        
        
# @lc code=end

