from exp import Val,Add,Mul,Sub,Div

def parse(s: str):
    if s.rfind('+') > 0:     #足し算
        pos = s.rfind('+')
        s1=s[:pos]
        s2=s[pos+1:]
        return Add(parse(s1),parse(s2))

    elif s.rfind('-') > 0:    #引き算
        pos = s.rfind('-')
        s1=s[:pos]
        s2=s[pos+1:]
        return Sub(parse(s1),parse(s2))

    elif s.rfind('*') > 0:   #かけ算
        pos = s.rfind('*')
        s1=s[:pos]
        s2=s[pos+1:]
        return Mul(parse(s1),parse(s2))

    elif s.rfind('/') > 0:   #割り算
        pos = s.rfind('/')
        s1=s[:pos]
        s2=s[pos+1:]
        return Div(parse(s1),parse(s2))

    else:
        num=int(s)
        return Val(num)
    

e=parse("4/2+24/12*2-6")
print(e,e.eval())
assert e.eval()==0

r=parse("1+2*3-9+8-2*4")
print(r,r.eval())
assert r.eval()==-2


'''
s="123+456"
pos=s.find('+')
print('pos',pos)

s1=s[0:pos]
s2=s[pos+1:]
print(s,s1,s2)
'''