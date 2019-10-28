from exp import Val,Add,Mul

def parse(s: str):
    if s.find('+') > 0:
        pos = s.find('+')
        s1=s[:pos]
        s2=s[pos+1:]
        return Add(parse(s1),parse(s2))

    elif s.find('*') > 0:
        mos = s.find('*')
        s1=s[:mos]
        s2=s[mos+1:]
        return Mul(parse(s1),parse(s2))

    else:
        num=int(s)
        return Val(num)
    

e=parse("1*2+3")
print(e,e.eval())
assert e.eval()==5

r=parse("1+2*3")
print(r,r.eval())
assert r.eval()==7

'''
s="123+456"
pos=s.find('+')
print('pos',pos)

s1=s[0:pos]
s2=s[pos+1:]
print(s,s1,s2)
'''