# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 22:59:53 2022

@author: R.U.S.T.E.A.M
"""

class Solution:
    def romanToInt(self, s: str) -> int:
       double = {
        'CM' : 900,
        'CD' : 400,
        'XC' : 90,
        'XL' : 40,
        'IX' : 9,
        'IV' : 4
        }
       singles = {
            'M' : 1000,
            'D' : 500,
            'C' : 100,
            'L' : 50,
            'X' : 10,
            'V' : 5,
            'I' : 1
            }
       i = 0
       n = 0
       while i < len(s):
           if i < len(s) - 1 and s[i:i+2] in double:
               n += double[s[i:i+2]]
               i += 2
           else:
               n += singles[s[i]]
               i += 1
       return n