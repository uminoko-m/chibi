def calc(s):
    count=0
    if len(s)==1:
        b=int(s)
        count+=b
    else:
        for i in range(len(s)):
            if s[i]=="+":
                pass
            else:
                a=int(s[i])
                count+=a
    return int(count)

print(calc("1"))
print(calc("1+2"))
print(calc("1+2+3"))
