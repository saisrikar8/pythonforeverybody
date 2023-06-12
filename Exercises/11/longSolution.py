#Data Format
#The file contains much of the text from the introduction of the textbook except that random numbers are inserted throughout the text. Here is a sample of the output you might see:

#=========================================================#

#Why should you learn to write programs? 7746
#12 1929 8827
#Writing programs (or programming) is a very creative 
#7 and rewarding activity.  You can write programs for 
#many reasons, ranging from making your living to solving
#8837 a difficult data analysis problem to having fun to helping 128
#someone else solve a problem.  This book assumes that 
#everyone needs to know how to program ...

#=========================================================#

#The sum for the sample text above is 27486. The numbers can appear anywhere in the line. There can be any number of numbers in each line (including none).

import re

#Getting the file
fileName = input("Enter file: ")
if (len(fileName) < 1):
    fileName = "regex_sum_42.txt"
file = open(fileName)

#iterating and searching thru each line
lst = list()
for line in file:
    nums = re.findall('[0-9]+', line)
    lst = lst + [int(num) for num in nums]
print(sum(lst))
    