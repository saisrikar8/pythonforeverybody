#9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

name = input("Enter file: ")
if (len(name) < 1):
    name = 'mbox-short.txt'
handle = open(name)
count = dict()

#Finding lines that start with 'From ' in mbox-short.txt and storing used email addresses in dictionary
for line in handle:
    lineList = line.split()
    
    if (len(lineList) < 2):
        continue
        
    if (lineList[0] != 'From'):
        continue
    
    emailAddress = lineList[1]
    count[emailAddress] = count.get(emailAddress, 0) + 1

#Residual Values Stored in these variables
maxNumOfMessages = 0
maxUsedEmailAddress = ''

#Max Loop/Finding max email address in count
for emailAddress, numOfMessages in count.items():
    if (maxNumOfMessages < numOfMessages):
        maxNumOfMessages = numOfMessages
        maxUsedEmailAddress = emailAddress
        
print(maxUsedEmailAddress, maxNumOfMessages)