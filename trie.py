from collections import defaultdict

class Trie:
    def __init__(self):
        self.posi = defaultdict()
        self.neg=defaultdict()
    def insertP(self, word):
        current = self.posi
        for letter in word:
            current = current.setdefault(letter, {})
        current.setdefault("_end")

    def insertN(self,word):
        current=self.neg
        for letter in word:
            current=current.setdefault(letter,{})
        current.setdefault("_end")

    def prints(self):
        print self.posi
        print self.neg

    def search(self,word):
        cur=self.posi
        cur1=self.neg
        str=''
        for letter in word:
            if letter in cur and letter in cur1:
                cur=cur[letter]
                cur1=cur1[letter]
                str+=letter
            else:
                str+=letter
                if "_end" in cur1:
                    return False,-1
                else:
                    return True,str
        return False,-1

t=Trie()
negate=[]
visited=[]
for _ in xrange(input()):
    a=(raw_input().strip()).split()
    if a[0]=='+':
        t.insertP(a[1])
    else:
        t.insertN(a[1])
        negate.append(a[1])
final=[]
tot=0
set=0
negate.sort()
for i in negate:
    val=t.search(i)
    if val[0]==True:
        if val[1] not in final:
            tot+=1
            final.append(val[1])
    else:
        set=1
        print -1
        break
if set==0:
    final.sort()
    print tot
    for i in final:
        print i
