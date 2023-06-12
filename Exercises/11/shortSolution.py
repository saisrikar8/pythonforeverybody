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

#Optional: Just for Fun
#There are a number of different ways to approach this problem. While we don't recommend trying to write the most compact code possible, it can sometimes be a fun exercise. Here is a a redacted version of two-line version of this program using list comprehension:
import re
print(sum([int(num) for num in re.findall('[0-9]+',open('regex_sum_1715457.txt').read())]))