#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 15:16:13 2020

@author: suneelvarma
"""

def check(l,i,j,checklist,var):
    if (i,j) in checklist:
        return 'yes'
    elif i>=0 and j>=0:
        try:
            x = var if l[i][j]==var else 0
            return x
        except IndexError:
            return 0
    else:
        return 0
 
def fun(arr,i,j,checked,var):
    x = check(arr,i,j,checked,var)
    if x == 'yes':
        return 1
    elif x == var:
        checked.append((i,j))
        fun(arr,i+1,j,checked,var)
        fun(arr,i,j+1,checked,var)
        fun(arr,i-1,j,checked,var)
        fun(arr,i,j-1,checked,var)
        return checked
    elif x == 0:
        return 0
    
if __name__ == '__main__':
    n=int(input())
    arr = []
    for i in range(n):
        arr.append(input())
    m=len(arr[0])
    groups = []
    checked = []
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 'a' and (i,j) not in checked:
                temp = fun(arr,i,j,[],'a')
                groups.append(len(temp))
                checked += temp
            elif arr[i][j] == 'b' and (i,j) not in checked:
                temp = fun(arr,i,j,[],'b')
                groups.append(len(temp))
                checked += temp
            elif arr[i][j] == 'c' and (i,j) not in checked:
                temp = fun(arr,i,j,[],'c')
                groups.append(len(temp))
                checked += temp
                
    print(len(groups))