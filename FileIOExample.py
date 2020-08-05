# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 12:22:54 2020

@author: Angshuman
"""

file1= open('filetest.txt');
print(file1.readlines());
print(file1.readlines());
file1.seek(0);
print(file1.readlines());
file1.close();

with open('filetest.txt',mode='r') as f:
    print(f.read());

with open('filetest.txt', mode='a') as f:
    f.write("\nThis is 4th line");

with open('filetest.txt', mode='r') as f:
    print(f.read());
    
with open('newfiletest.txt', mode='w') as f:
    f.write("Created this new file using python");
    
with open('newfiletest.txt', mode='r') as f:
    print(f.read());