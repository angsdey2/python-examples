# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 22:35:55 2020

@author: Angshuman
"""

num= 0;

while num<10:
    print(f"Current num :{num}");
    num+=1;
else:
    print(f"Current num is not less than 10");
    


print("============== Break example ================");

val=15
while val>10:
    if val == 12:
        break;
    print(f"val is: {val}");
    val-=1;