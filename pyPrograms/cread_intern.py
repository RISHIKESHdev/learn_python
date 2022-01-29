class social_network(object):
    def __init__(self):
        self.d=dict()
        self.a=0
        self.b=0
        self.l=dict()
    def group(self,list):
        for i in list:
            self.d[self.a]=i
            self.a+=1
        for k,v in sorted(self.d.items()):
            self.l[v]=[k] if v not in self.l.keys() else self.l[v]+[k]
        print(self.d)
        print(self.l)
        for i in self.l:
            for j in range(0,len(self.l[i]),i):
                b=0
                while(b<i):
                    print(self.l[i][j+b],end=" ")
                    b+=1
                print("") 
p=social_network()
a=int(input())
list=[]
for i in range(a):
    list.append(int(input()))
p.group(list)
