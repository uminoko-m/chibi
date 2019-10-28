from exp import Val,Add,Mul

def parse(s: str):
    if s.find('+') > 0:
        pos = s.find('+')
        s1=int(s[:pos])
        s2=int(s[pos+1:])
        return Add(Val(s1),Val(s2))
    else:
        num=int(s)
        return Val(num)

e=parse("1+2")
assert e.eval()==3


#s="123+456"
#pos=s.find('+')
#print('pos',pos)

#s1=s[0:pos]
#s2=s[pos+1:]
#print(s,s1,s2)
