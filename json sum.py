import urllib.request, urllib.parse, urllib.error
import json
url=input("enter url here:")
connection=urllib.request.urlopen(url)
read=connection.read().decode()
js=json.loads(read)
info=js["comments"]
print("retreive :",url, "\ncount:",len(read))
sum=0
for i in info:
    sum=sum+int(i['count'])
print(sum)