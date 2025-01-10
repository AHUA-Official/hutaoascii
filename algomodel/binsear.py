#二分查找实现
def  binsearch(arr ,tgt):
    low =0
    high = len(arr)-1
    if len(arr)<1:
        return False
    while low <= high:
        mid = (low+high)//2
        if arr[mid] == tgt:
            print("命中   index在%s "%mid)
            return mid
        if arr[mid] < tgt:
            low = mid+1
            print("中间值小于目标 在右边查询")
        if arr[mid] > tgt:
            high = mid-1
            print("中间值比目标值大   网左边查询")
    print("没有命中")
    return -1
# 示例数组和目标值
arr = [1, 3, 5, 7, 9]
target = 9

# 执行二分查找
index = binsearch(arr, target)
if index != -1:
    print("Element found at index", index)
else:
    print("Element not found")

def is_palindrome_string(s: str) -> bool:
    return s == s[::-1]

# 测试
print(is_palindrome_string("abcba"))  # 输出: True
print(is_palindrome_string("abc"))    # 输出: False
