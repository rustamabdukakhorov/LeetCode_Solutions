# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 23:01:29 2022

@author: R.U.S.T.E.A.M
"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in matrix:
            if target in i:
                return True
        return False