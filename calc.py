def calc(s):
  nums=[]
  st=s.split("+")
  #print(st)

  for i in range(len(st)):
    nums.append(st[i].split("*"))
  #print(nums)

  count=0
  for i in range(len(nums)):
    lon=len(nums[i])
    if lon >= 2:
      for j in range(lon-1):
        if j==0:
          a=int(nums[i][j]) * int(nums[i][j+1])
        elif j>=1:
          a=a*int(nums[i][j+1])
      count+=a
    else:
      count+=int(nums[i][0])

  return count

print(calc("1+2*3"))
print(calc("1+2+3"))
print(calc("1*2+3"))
print(calc("1*2*3"))