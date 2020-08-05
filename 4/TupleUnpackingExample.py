# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 22:39:39 2020

@author: Angshuman
"""

examScore = [("AD", 500), ("KR", 600), ("SM", 7000), ("DS", 800)];

def find_highest_scsorer(examScore):
    highestScorerName ='';
    currentMax=0;
    for name,score in examScore:
        if score>currentMax:
            currentMax= score;
            highestScorerName = name;
        else:
            pass;
    
    return (highestScorerName,currentMax);

item = find_highest_scsorer(examScore);

print(item);

name,score = find_highest_scsorer(examScore);

print(f"{name} is the highest scorer with {score} marks");
