#10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

#Creating File Handler
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

#Adding number of messages sent in each hour into dictionary 'hourCount'
hourCount = dict()
for line in handle:
    lineList = line.split()
    if (len(lineList) < 7 or lineList[0] != 'From'):
        continue
    hour = lineList[5].split(':')[0]
    hourCount[hour] = hourCount.get(hour, 0) + 1

#Creates list of tuples from data in 'hourCount' and sort by hour
hourList = sorted(hourCount.items())

#Printing the data from 'hourList'
for hour, numMsgs in hourList:
    print(hour, numMsgs)