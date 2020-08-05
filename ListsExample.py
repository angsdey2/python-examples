# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 17:49:30 2020

@author: Angshuman
"""

numberList = [1,2,3];
mixedList = ['String', 22.44 , 99];

list1 = ['One','Two','Three'];
list2 = ['Four','Five'];

addedList = list1+list2;

print(numberList);
print(mixedList);
print(mixedList[1]);
print(numberList[1:]);
print(addedList);


addedList.append("Six");
print(addedList);

addedList.pop();
print(addedList);

addedList.pop(0);
print(addedList);

addedList.sort();
print(addedList);

addedList.reverse();
print(addedList);