# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 23:00:43 2022

@author: R.U.S.T.E.A.M
"""

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target in nums and nums:
            return [nums.index(target), len(nums) - nums[::-1].index(target) -1]
        else:
            return [-1, -1]