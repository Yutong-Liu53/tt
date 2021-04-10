#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 13:01:39 2021

@author: apple
"""

# PPHA 30535
# Spring 2021
# Homework 1

# YOUR CANVAS NAME Yutong Liu (yutongl)
# YOUR GITHUB USER NAME Yutong-Liu53

# Due date: Sunday April 11th before midnight
# Write your answers in the space between the questions, and commit/push only this file to your repo.
# Note that there can be a difference between giving a "minimally" right answer, and a really good
# answer, so it can pay to put thought into your work.

#############

# Question 1: Using a for loop, write code that takes in any list of objects, then prints out:
# "The value at position __ is __" for every element in the loop, where the first blank is the
# index location and the second blank the object at that index location
my_list = [5, 9, 3, 8, 7]
for i in range(len(my_list)):
    print("The value at position", end = " ")
    print(i, end = " is ")
    print(my_list[i])

# Question 2: A palindrome is a word or phrase that is the same both forwards and backwards. Write
# code that takes a variable of any string, then tests to see whether it qualifies as a palindrome.
# Make sure it counts the word "radar" and the phrase "A man, a plan, a canal, Panama!", while
# rejecting the word "Apple" and the phrase "This isn't a palindrome". Print the results.
def isPalindrome(s):
    return s == s[::-1]
    return s == s.strip()
    return s == s.lower()
   
s = 'radar'
ans = isPalindrome(s)
 
if ans:
    print(s, "is a palindrome")
else:
    print(s, "isn't a palidrome")
    
s =  'A man, a plan, a canal, Panama!' 
ans = isPalindrome(s)
 
if ans:
    print(s, "is a palindrome")
else:
    print(s, "isn't a palidrome")

s = 'apple'
ans = isPalindrome(s)
 
if ans:
    print(s, "is a palindrome")
else:
    print(s, "isn't a palidrome")
    
s = "This isn't a palindrome"
ans = isPalindrome(s)
 
if ans:
    print(s, "is a palindrome")
else:
    print(s, "isn't a palidrome")


# Question 3: The code below pauses to wait for user input, before assigning the user input to the
# variable.  Beginning with the given code, check to see if the answer given is an available
# vegetable.  If it is, print that the user can have the vegetable and end the bit of code.  If
# they input something unrecognized by our list, tell the user they made an invalid choice and make
# them pick again.  Repeat until they pick a valid vegetable.


# Question 4: Write a list comprehension that starts with any list of strings, and returns a new
# list that contains each string in all lower-case letters, but only if the string begins with the
# letter "a" or "b".
new_list = ['cDEF', 'aCDe', 'bcDE']
for string in new_list:
    if string.startswith('a'):
        print(string.lower())
    elif string.startswith('b'):
        print(string.lower())
    else:
        print(string)##list

# Question 5: Beginning with the list below, write a single list comprehension that turns it into
# the following list: [26, 22, 18, 14, 10, 6]
start_list = [3, 5, 7, 9, 11, 13]
start_list[0] = start_list[0] + 23##
start_list[1] = start_list[1] + 17
start_list[2] = start_list[2] + 11
start_list[3] = start_list[3] + 5
start_list[4] = start_list[4] - 1
start_list[5] = start_list[5] - 7 
print(start_list)

# Question 6: Beginning with the two lists below, write a single dictionary comprehension that
# turns them into the following dictionary: {'IL':'Illinois', 'IN':'Indiana', 'MI':'Michigan', 'OH':'Ohio'}
short_names = ['IL', 'IN', 'MI', 'OH']
long_names  = ['Illinois', 'Indiana', 'Michigan', 'Ohio']
res = {short_names[i]:long_names[i] for i in range(len(short_names))}
print(str(res))