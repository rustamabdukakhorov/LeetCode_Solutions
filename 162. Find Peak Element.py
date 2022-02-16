# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 17:37:45 2022

@author: R.U.S.T.E.A.M
"""

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        peak = len(nums)-1
        for i in range(len(nums)-1):
            if nums[i+1] < nums[i]:
                return i
        return peak