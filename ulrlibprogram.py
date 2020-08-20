
# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter the url to scrape - ')

html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

counts = 0
sum = 0

spans = soup('span')
for i in spans:
    sum = sum+ int(i.contents[0])
    counts += 1

print('Count ', counts)
print('Sum ', sum)
