#This application will read the mailbox data (mbox.txt) and count the number of email messages per organization (i.e. domain name of the email address) using a database with the following schema to maintain the counts.

#=================================================#
#                                                 #
#  CREATE TABLE Counts (org TEXT, count INTEGER)  #
#                                                 #
#=================================================#

import sqlite3

#initializing the table Counts in 'emaildb.sqlite'
conn = sqlite3.connect('emaildb.sqlite')
handle = conn.cursor()
handle.execute("DROP TABLE IF EXISTS Counts")
handle.execute("CREATE TABLE Counts (org TEXT, count INTEGER)")

#Getting the file mbox.txt
fname = input("Enter the file name: ")
if (len(fname) < 1):
    fname = 'mbox.txt'
file = open(fname)

for line in file:
    if (not line.startswith('From: ')): continue
    domain = line.split()[1].split('@')[1]
    handle.execute('SELECT count FROM Counts WHERE org = ?', (domain,))
    row = handle.fetchone()
    if (row is None):
        handle.execute('INSERT INTO Counts (org, count) VALUES (?, 1)', (domain,))
    else:
        handle.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (domain,))
    conn.commit()
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in handle.execute(sqlstr):
    print(row[0], row[1])
handle.close()
    