# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 17:28:17 2022

@author: R.U.S.T.E.A.M
"""

class Solution:
    def findMin(self, nums: List[int]) -> int:
            minimum = nums[0]
            for i in nums:
                if i <= minimum:
                    minimum = i
            return minimum