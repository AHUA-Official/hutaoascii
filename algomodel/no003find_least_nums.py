# 给定一个未排序的整数数组nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。
#请你设计并实现时间复杂度为O(n)的算法解决此问题。
# https://leetcode.cn/problems/longest-consecutive-sequence/description/
#128  最长连续序列


from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        cnt = dict()
        for num in nums:
            prev = cnt[num-1] if num-1 in cnt else 0
            suf = cnt[num+1] if num+1 in cnt else 0
            if not num in cnt:
                cnt[num] = prev+suf+1;
                cnt[num-prev] = cnt[num]
                cnt[num+suf] = cnt[num]
        ans = max(cnt.values())
        return ans
    def longestConsecutiveleft(self, numsl: List[int]) -> int:
        if len(numsl) == 0:
            return 0
        cnt = dict()
        nums =set(numsl)
        for num in nums:
            if num-1 in cnt :
                cnt[num] = cnt[num-1]+1
                start= num - cnt[num-1]
                cnt[start] = cnt[num]
            else:
                cnt[num] = 1


        ans = max(cnt.values())
        return ans

    def dp1(self,nums:List[int]) -> int:
        if len(nums) == 0:
            return 0
        maxlenth =0
        st =set(nums)
        for num in nums:
            end =num+1;
            while end in st:
                end =end+1
            maxlenth = max(maxlenth,end-num)
        return maxlenth

    def longestConsecutiveAAA(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        maxlenth = 1
        st = set(nums)
        for num in nums:
            end = num + 1;
            if num - 1 not in st:
                nowlenth = 1
                now = num

                while now + 1 in st:
                    now = now + 1
                    nowlenth += 1
                maxlenth = max(maxlenth, nowlenth)
        return maxlenth
    def dp2(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        maxlenth = 0
        st = set(nums)
        for num in nums:
            y = num - 1;
            while y in st:
                y = y - 1
            maxlenth = max(maxlenth, num - y)
        return maxlenth

solution = Solution()
# 测试用例 1：空数组
nums1 = []
print("Test Case 1:")
print(solution.longestConsecutive(nums1)) # 输出: 0
print(solution.longestConsecutiveleft(nums1))
print(solution.dp1(nums1))  # 输出: 0
print(solution.dp2(nums1))  # 输出: 0

# 测试用例 2：单个元素
nums2 = [5]
print("\nTest Case 2:")
print(solution.longestConsecutive(nums2))  # 输出: 1
print(solution.longestConsecutiveleft(nums2))
print(solution.dp1(nums2))  # 输出: 1
print(solution.dp2(nums2))  # 输出: 1

# 测试用例 3：已排序且无重复的数组
nums3 = [1, 2, 3, 4, 5]
print("\nTest Case 3:")
print(solution.longestConsecutive(nums3))  # 输出: 5
print(solution.longestConsecutiveleft(nums3))
print(solution.dp1(nums3))  # 输出: 5
print(solution.dp2(nums3))  # 输出: 5

# 测试用例 4：未排序且有重复的数组
nums4 = [10, 5, 12, 6, 7, 8, 9, 5, 10]
print("\nTest Case 4:")
print(solution.longestConsecutive(nums4))  # 输出: 5 (5, 6, 7, 8, 9)
print(solution.longestConsecutiveleft(nums4))
print(solution.dp1(nums4))  # 输出: 5 (5, 6, 7, 8, 9)
print(solution.dp2(nums4))  # 输出: 5 (5, 6, 7, 8, 9)

# 测试用例 5：负数和正数混合
nums5 = [-1, 0, 1, 2, -2, -3, -4]
print("\nTest Case 5:")
print(solution.longestConsecutive(nums5))  # 输出: 4 (-4, -3, -2, -1, 0, 1, 2)
print(solution.longestConsecutiveleft(nums5))
print(solution.dp1(nums5))  # 输出: 4 (-4, -3, -2, -1, 0, 1, 2)
print(solution.dp2(nums5))  # 输出: 4 (-4, -3, -2, -1, 0, 1, 2)

# 测试用例 6：完全不连续的数组
nums6 = [1, 10, 100, 1000, 10000]
print("\nTest Case 6:")
print(solution.longestConsecutive(nums6))  # 输出: 1
print(solution.longestConsecutiveleft(nums6))
print(solution.dp1(nums6))  # 输出: 1
print(solution.dp2(nums6))  # 输出: 1

# 测试用例 7：大量重复元素
nums7 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
print("\nTest Case 7:")
print(solution.longestConsecutive(nums7))  # 输出: 1
print(solution.longestConsecutiveleft(nums7))
print(solution.dp1(nums7))  # 输出: 1
print(solution.dp2(nums7))  # 输出: 1

# 测试用例 8：随机顺序的数组
nums8 = [9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6]
print("\nTest Case 8:")
print(solution.longestConsecutive(nums8))  # 输出: 5 (-1, 0, 1, 3, 4, 5, 6, 7, 8, 9)
print(solution.longestConsecutiveleft(nums8))
print(solution.dp1(nums8))  # 输出: 5 (-1, 0, 1, 3, 4, 5, 6, 7, 8, 9)
print(solution.dp2(nums8))  # 输出: 5 (-1, 0, 1, 3, 4, 5, 6, 7, 8, 9)