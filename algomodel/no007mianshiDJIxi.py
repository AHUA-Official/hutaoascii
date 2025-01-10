# 拖住科技
def is_valid_ip(ip):
    parts = ip.split('.')
    if len(parts) != 4:
        return False
    for part in parts:
        if not part.isdigit() or not 0 <= int(part) < 256 :
            # or (part[0] == '0' and len(part) > 1)
            return False
    return True

# 测试
print(is_valid_ip("192.168.1.1"))  # True
print(is_valid_ip("255.255.255.255"))  # True
print(is_valid_ip("256.100.50.25"))  # False


def binary_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_value = arr[mid]

        if mid_value == target:
            return mid  # 返回目标值的索引
        elif mid_value < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # 如果未找到，返回-1


# 示例数组和目标值
arr = [1, 3, 5, 7, 9]
target = 3

# 执行二分查找
index = binary_search(arr, target)
if index != -1:
    print(f"Element found at index {index}")
else:
    print("Element not found")