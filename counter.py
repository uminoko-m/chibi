class Counter(object):

    #引数は必ずself
    def __init__(self): #コンストラクタ
        self.cnt=0  

    def count(self):    
        self.cnt+=1

    def doublecount(self):  #2回カウントする
        self.cnt+=2

    def reset(self):
        self.cnt=0

    def show(self):     
        print(self.cnt)

    def __repr__(self):     #文字列を返すと表示される
        return str(self.cnt)

c=Counter()         #作成したクラスを呼び出し、オブジェクトを生成
c.show()
c.doublecount()
c.show()

print(type(c))      #オブジェクトが何のクラスか教えてくれる
print(c)