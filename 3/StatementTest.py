# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 19:59:44 2020

@author: Angshuman
"""

#Use for, .split(), and if to create a Statement that will print out words that start with 's':
st = 'Print only the words that start with s in this sentence'

words = st.split(" ");

for word in words:
    if(word.startswith('s')):
        print(word);
        

#Use range() to print all the even numbers from 0 to 10.

#Code Here
for num in range(1,11):
    if num%2==0:
        print(num);


#Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.

 
#Code in this cell
result = [x for x in range(1,51) if x%3 ==0 ]
print(result);

#Go through the string below and if the length of a word is even print "even!"

#Go through the string below and if the length of a word is even print "even!"

st = 'Print every word in this sentence that has an even number of letters'
#Code in this cell
evenWords = ['even!' if len(x)%2 == 0 else x for x in st.split(" ")];
print(evenWords);


#Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".;
#Code in this cell
for x in range(1,101):
    if x%3==0 and x%5==0:
        print("FizzBuzz");
    elif x%3==0:
        print("Fizz");
    elif(x%5)==0:
        print("Buzz");
    else:
        print(x);
        
#Use List Comprehension to create a list of the first letters of every word in the string below:

st = 'Create a list of the first letters of every word in this string'
#Code in this cell
firstLetterList = [x[0] for x in st.split(" ")];
print(firstLetterList);