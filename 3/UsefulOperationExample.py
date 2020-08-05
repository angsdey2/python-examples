# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 00:08:02 2020

@author: Angshuman
"""
from random import shuffle;
from random import randint;

#Range function

for num in range(23,101,10):
    print(num);
    

#enumerate function
numList = [1,2,3,4,5,6,7,8,9,10];
for (index,val) in enumerate(numList):
    print(f"index: {index} - Value: {val}");
    
dictVar = {1: "One", 2:"Two", 3:"Three", 4:"Four", 5:"Five"};


for (index,(key,val)) in enumerate(dictVar.items()):
    print(f"index: {index} - key: {key} - val: {val}");
    

#zip function
    
list1 =[1,2,3,4];
list2 =['One', 'Two', 'Three'];

for index,(key,val) in enumerate(list(zip(list1,list2))):
    print(f"index: {index} - key: {key} - val: {val}");
    
#in function
if('One' in list2):
    print("Item present");

if 1 in dictVar.keys():
    print("Key present");
    

# min/max function
print(max(numList));
print(min(numList));

#random library function
shuffle(numList);
print(numList);

print(randint(1,100));

result = input("What is your name?\n");
print("Hello " + result);