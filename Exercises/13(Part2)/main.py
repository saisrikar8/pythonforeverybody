import urllib.request, urllib.parse, urllib.error
import json

url = input("Enter url: ")
if (len(url) < 1):
    url = "http://py4e-data.dr-chuck.net/comments_1715462.json"

JSON = json.load(urllib.request.urlopen(url))['comments']

countSum = 0

for person in JSON:
    countSum += person['count']

print(countSum)