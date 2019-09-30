def calc(s):
    nums=list(map(int,s.split("+")))
    count=0
    for i in range(len(nums)):
        count+=nums[i]
    return count

print(calc("1"))
print(calc("1+2"))
print(calc("1+2+3"))
