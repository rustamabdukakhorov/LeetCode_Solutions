# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 22:55:01 2022

@author: R.U.S.T.E.A.M
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
            num_lst = list(range(len(nums)))
    
            for indx, num in enumerate(num_lst):
                for num_other in num_lst[indx+1:]:
                    if nums[num] + nums[num_other] == target:
                        return [num, num_other]
                    else: 
                        continue
            return None