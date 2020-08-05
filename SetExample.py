# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 00:38:53 2020

@author: Angshuman
"""

# Sets are collection of unordered unique objects
set1 = set();
set1.add(1);
set1.add(2);
print(set1);

list1 = [1,1,1,1,2,2,2,2,3,3,3,4,4,4];
set2= set(list1);
print(set2);

set3 = set([1,1,2,3]);
print(set3);

bool1 =None;
print('None assignment:',bool1);
bool1= False;
print(bool1==True);

