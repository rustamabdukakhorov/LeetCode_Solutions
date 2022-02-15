# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 23:01:01 2022

@author: R.U.S.T.E.A.M
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            return -1