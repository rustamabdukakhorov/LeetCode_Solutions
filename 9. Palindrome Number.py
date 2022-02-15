# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 22:56:48 2022

@author: R.U.S.T.E.A.M
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        if s == s[::-1]:
            return True
        else:
            return False