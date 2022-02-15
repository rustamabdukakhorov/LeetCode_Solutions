# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 23:00:33 2022

@author: R.U.S.T.E.A.M
"""

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = []
        c = 0
        i = len(a)-1
        j = len(b)-1
        
        while c or i>=0 or j>=0:
            
            t = c
            if i>=0:
                t += int(a[i])
                i-=1
            if j>=0:
                t += int(b[j])
                j-=1
            result.append(str(t%2))
            c = t//2
        return "".join(result[::-1])