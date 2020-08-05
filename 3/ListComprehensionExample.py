# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 19:30:34 2020

@author: Angshuman
"""

celciusList =[10,20,30,40,50,60,70,80,90,100]
farhenhietList = [((9/5)*celc + 32) for celc in celciusList]
celFarList = list(zip(celciusList,farhenhietList));
print(celciusList);
print(farhenhietList);
print(celFarList);


results = ['EVEN' if x%2==0 else 'ODD' for x in range(1,11)];
print(results);


# nested loops using list comprehension

myList = [x*y for x in [2,4,6] for y in [1,10,100,1000]];
print(myList);