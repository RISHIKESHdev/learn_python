#import xml.etree.ElementTree as ET
import re
import json
import urllib.request, urllib.parse, urllib.error
lst=list()
x=0
url=input('Enter location:')
uh = urllib.request.urlopen(url).read()
print('Retriving: ',url)
print('Retrieved ',len(uh),' characters')
u=uh.decode()
lst=(re.findall('[0-9]+',u))
for i in lst:
    x=x+int(i)
print('sum: ',x)
#lst=json.load(u)
#print('sum:' ,sum(lst))
