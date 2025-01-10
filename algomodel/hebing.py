#合并有序数组
#假设有两个有序数列，对其进行合并，并按照倒序排列返回；
#如[1，3，4],[2,2,4,5];返回[5,4,4,3,2,2,1]
a = [1,3,4]
b = [2,2,4,5]
m=a+b
m.sort(reverse=True)
print(m)
c=[]
i, j = len(a) - 1, len(b) - 1
while i >= 0 and j >= 0:
    if a[i] > b[j]:
        c.insert(0, a[i])
        i -= 1
    else:
        c.insert(0, b[j])
        j -= 1

# 如果数组a还有剩余元素，添加到结果数组
while i >= 0:
    c.insert(0, a[i])
    i -= 1

# 如果数组b还有剩余元素，添加到结果数组
while j >= 0:
    c.insert(0, b[j])
    j -= 1

print(c)
