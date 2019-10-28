from exp import Val,Add,Mul

def parse(s: str):
    if s.find('+') > 0:
        pos = s.find('+')
        s1=int(s[:pos])
        s2=s[pos+1:]
    else:
        num=int(s)
        return Val(num)
    return Add(Val(s1),parse(s2))

e=parse("1")
assert e.eval()==1

r=parse("1+2")
assert r.eval()==3

w=parse("1+2+3")
assert w.eval()==6

'''
s="123+456"
pos=s.find('+')
print('pos',pos)

s1=s[0:pos]
s2=s[pos+1:]
print(s,s1,s2)
'''