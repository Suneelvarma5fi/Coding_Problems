#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 19:18:04 2020

@author: suneelvarma
"""

''' LONGEST COMMON SUBSTRING '''


def substring(mat,i,j,subs):
    if i == 0 or j == 0:
        return subs[::-1]
    
    x = mat[i][j]
    j -= 1
    while x == mat[i][j]:
        j -= 1
    else:
        subs += s1[j]
        return substring(mat,i-1,j,subs)

def LCS(s1,s2):
    len1,len2 = len(s1),len(s2)

    mat = [[0 for _ in range(len1+1)] for _ in range(len2+1)]
    for i in range(1,len2+1):
        for j in range(1,len1+1):
        
            if s2[i-1] != s1[j-1]:
                mat[i][j] = max(mat[i-1][j],mat[i][j-1])
            else:
                mat[i][j] = mat[i-1][j-1]+1
                
    return substring(mat,len2,len1,'')
        
if __name__ == '__main__':
    s1 = input()
    s2 = input()
    print(LCS(s1,s2))