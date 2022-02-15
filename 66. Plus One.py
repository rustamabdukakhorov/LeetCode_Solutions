# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 22:57:08 2022

@author: R.U.S.T.E.A.M
"""

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ''
        for i in digits:
            s += str(i)

        x = int(s) + 1
        x = str(x)
        return [int(i) for i in x]