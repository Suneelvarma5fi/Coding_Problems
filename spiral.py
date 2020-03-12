#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 20:18:54 2020

@author: suneelvarma
"""

'''SPIRAL ARRAY'''
arr = list(range(101,165))

row = 8
col = 8
p = 0
i = 0
j = 0
res = [[0 for _ in range(row)] for _ in range(col)]

def display(res):
    for i in res:
        print(i)
    return

def right(res,i,j,p,arr):#i constant
    global row,col
    if res[i][j] != 0 or p > row*col:
        display(res)
        return res
    else:
        while res[i][j+1] == 0:
            res[i][j] = arr[p]
            p += 1
            j += 1
            if j == row-1 and res[i][j] == 0:
                res[i][j] = arr[p]
                down(res,i+1,j,p+1,arr)
                break
        else:
            res[i][j] = arr[p]
            down(res,i+1,j,p+1,arr)
            


def down(res,i,j,p,arr):#j constant
    global row,col
    if res[i][j] != 0 or p > row*col:
        display(res)
        return res
    else:
        while res[i+1][j] == 0:
            res[i][j] = arr[p]
            p += 1
            i += 1
            if i == col-1 and res[i][j] == 0:
                res[i][j] = arr[p]
                left(res,i,j-1,p+1,arr)
                break
        else:
            res[i][j] = arr[p]
            left(res,i,j-1,p+1,arr)
        
def left(res,i,j,p,arr):#i constant
    global row,col
    if res[i][j] != 0 or p > row*col:
        display(res)
        return res
    else:
        while res[i][j-1] == 0:
            res[i][j] = arr[p]
            p += 1
            j -= 1
            if j == 0 and res[i][j] == 0:
                res[i][j] = arr[p]
                up(res,i-1,j,p+1,arr)
                break
        else:
            res[i][j] = arr[p]
            up(res,i-1,j,p+1,arr)
        
def up(res,i,j,p,arr):#j constant
    global row,col
    if res[i][j] != 0 or p > row*col:
        display(res)
        return res
    else:
        while res[i-1][j] == 0:
            res[i][j] = arr[p]
            p += 1
            i -= 1
            if i == 0 and res[i][j] == 0:
                res[i][j] = arr[p]
                right(res,i,j+1,p+1,arr)
                break
        else:
            res[i][j] = arr[p]
            right(res,i,j+1,p+1,arr) 
            