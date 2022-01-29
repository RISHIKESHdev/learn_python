from urllib.request import urlopen
from bs4 import BeautifulSoup
url = input('Enter - ')
html = urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")
span = soup('span')
c=list()
for sp in span:
    for i in sp:
        c.append(int(i))
print(sum(c))
