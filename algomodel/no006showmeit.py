# 数组中只有一个数字出现1次，其他数字都出现了2次，问这个数字是多少   这个怎么做呀
def find_single_number(nums):
    result = 0
    for num in nums:
        result ^= num
        print(result)
    return result

# 示例
nums = [2, 3, 2, 3]
print(find_single_number(nums))  # 输出应该是 4