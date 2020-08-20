import urllib.request as ur
import xml.etree.ElementTree as ET

url=input("enter file name:")
total=0
sum=0
print('retrieved' ,url)
xml=ur.urlopen(url).read()
print('retrieved',len(xml) , 'characters')

tree= ET.fromstring(xml)
counts=tree.findall('.//count')
for i in counts:
    sum=sum+int(i.text)
    total+=1
print('count:',total)
print('sum:',sum)