class Q(object):
    def __init__(self,a,b=1):       #初期値を書くと省略可能
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

q1=Q(1,2)
q2=Q(1,3)
print(q1 + q2)