from exp import Val,Add,Mul

def parse(s: str):
    num=int(s)
    return Val(num)

e=parse("1")
assert e.eval()==1