def solution(A):
    mydict ={}
    for i in A:
        if i in mydict:
            mydict[i]+=1
        else :
            mydict[i]=1
    my_count = list(mydict.values())
    counts = sorted(my_count)
    to_remove=0
    unique_counts=set()
    print(mydict)

    for c in counts:
        c -= 1
        to_remove += 1
        unique_counts.add(c)
    if len(set(counts))==1:
      return len(counts)-1

    return to_remove


A1 = [1, 1, 1, 2, 2, 2]
print(solution(A1))  # 应该输出 1

A2 = [5, 3, 3, 2, 5, 2, 3, 2]
print(solution(A2))  # 应该输出 2

A3 = [127, 15, 3, 8, 10]
print(solution(A3))  # 应该输出 4

A4 = [10000000, 10000000, 5, 5, 5, 2, 2, 2, 0, 0]
print(solution(A4))  # 应该输出 4

