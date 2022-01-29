from urllib.request import urlopen
from bs4 import BeautifulSoup
url = input('Enter url: ')
i=int(input('Enter count:'))
j=int(input('Enter position:'))
z=0
for z in range(i+1):
  a=list()    
  print('Retrieving : ',url)
  html =urlopen(url).read()
  soup = BeautifulSoup(html, "html.parser")
  href= soup('a')
  for hre in href:
   c=hre.get('href',None)
   a.append(c)
  url=(a[j-1])
