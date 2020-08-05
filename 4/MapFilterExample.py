# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 00:55:42 2020

@author: Angshuman
"""

numList = [1,2,3,4,5,6,7,8,9,10];
def square(num):
    return num**2;

def isEven(num):
    return num%2 == 0;

print(list(map(square,numList)));
print(list(filter(isEven,numList)));

## example of lambda expression
print(list(map(lambda num:num**2, numList)));
print(list(filter(lambda num: num%2==0, numList)));
