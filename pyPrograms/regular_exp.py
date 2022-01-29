import re
file=input('Enter a file name:')
fh=open(file)
x=list()
y=list()
z=0
for line in fh:
 if re.search('[0-9]+',line):
  y=re.findall('[0-9]+',line)
  for item in y:
   x.append(item)
for i in x:
    z=z+int(i)
print(z)
