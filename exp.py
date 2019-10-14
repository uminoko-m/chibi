class Expr:
    def eval(self):pass

def expr(e):
    if not isinstance(e,Expr):
        e=Val(e)
    return e

class Binary(Expr):
    __slots__=['left','right']
    def __init__(self,left,right):
        self.left=expr(left)
        self.right=expr(right)
    def __repr__(self):
        classname = self.__class__.__name__
        return f'{classname}({self.left},{self.right})'

class Val(Expr):              
    __slots__=['value']
    def __init__(self,value=0):
        self.value = value
    def __repr__(self):
        return f'Val({self.value})'
    def eval(self):
        return self.value

class Add(Binary):
    def eval(self):
        return self.left.eval() + self.right.eval()

class Mul(Binary):
    def eval(self):
        return self.left.eval() * self.right.eval()

class Sub(Binary):
    def eval(self):
        return self.left.eval() - self.right.eval()

class Div(Binary):
    def eval(self):
        return self.left.eval() // self.right.eval()
    
e=Mul(Add(1,2),3)
g=Div(2,7)
assert e.eval()==9
assert g.eval()==3