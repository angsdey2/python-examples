# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 22:09:02 2020

@author: Angshuman
"""

animals = ['Dog', 'Cat', 'Elephant', 'Horse'];
numList = [1,2,3,4,5,6,7,8,9,10];
numTotal = 0;
stringVar = "Learning python";

print("============== List Iteration Example================");
for animal in animals:
    print("This is {0}".format(animal));
    
print("============== List Iteration Example================");
for num in numList:
    numTotal+= num;

print(f'Sum of numList : {numTotal}');

print("============== String Iteration Example================");
for char in stringVar:
    print(char);
    
print("============== Tuple Iteration Example================");
listOfTuple = [(1,2),(3,4),(5,6),(7,8)]

for (val1, val2) in  listOfTuple:
    print(f'val1: {val1} - val2: {val2}');
    
print("================ Dictionary iteration example ==================");
dictVar = {1: "One", 2:"Two", 3:"Three", 4:"Four", 5:"Five"};

for (key,val) in dictVar.items():
    print(f"key: {key} - val: {val}");
    
print("============== Continue example ================");
for num in numList:
    if num%2==0:
        continue;
    print(f"{num} is odd number");




