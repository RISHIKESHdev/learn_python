import xml.etree.ElementTree as ET
import urllib.request, urllib.parse, urllib.error
d=list()
url=input('Enter location:')
uh = urllib.request.urlopen(url).read()
print('Retriving: ',url)
print('Retrieving ',len(uh),' characters')
stuff = ET.fromstring(uh)
lst =stuff.findall('comments/comment')
print('Count: ',len(lst))
for e in lst:
 d.append(int(e.find('count').text))
print('sum: ',sum(d))
