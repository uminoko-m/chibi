import math

class Q(object):
    def __init__(self,a,b=1):       #初期値を書くと省略可能
        #gcd = math.gcd(a,b)
        self.a=a
        self.b=b

    def __repr__(self):
        if self.b==1:
            return str(self.a)
        else:
            return f'{self.a}/{self.b}'

    def __add__(self,q):                #分数の足し算　　受け取るのはq,返すのはQ
        a=self.a                    #自分自身がself
        b=self.b
        c=q.a                       #引数で受け取ったほうがq
        d=q.b
        #print(a,b,c,d)
        a=a*d + b*c
        b=b*d
        return Q(a,b)

    def __sub__(self,q):
        a=self.a
        b=self.b
        c=q.a
        d=q.b
        a=a*d-b*c
        b=b*d
        return Q(a,b)

    def __mul__(self,q):
        a=self.a
        b=self.b
        c=q.a
        d=q.b
        a=a*c
        b=b*d
        return Q(a,b)

    def __truediv__(self,q):
        a=self.a
        b=self.b
        c=q.a
        d=q.b
        a=a*d
        b=b*c
        return Q(a,b)

q1=Q(1,2)
q2=Q(1,3)
q3=Q(4,6)
print(q1 + q2)
print(q1 - q2)
print(q1 * q2)
print(q1 / q2)