def unsame(s):
    result = []

    # 遍历字符串，处理相邻重复字符
    for i in range(len(s)):
        # 如果当前字符与前一个字符不同（或这是第一个字符），则添加到结果中
        if i == 0 or s[i] != s[i - 1]:
            result.append(s[i])

    # 将结果列表转换为字符串
    reanswer = "".join(result)
    return reanswer
input_string = "aabccba"
output_string = unsame(input_string)
print(output_string)  # 输出: "abcba"
# def unsame(s):
#     result = []
#     i = 0
#     while i < len(s):
#         if i < len(s) - 1 and s[i] == s[i + 1]:
#             # 如果当前字符与下一个字符相同，跳过这两个字符
#             i += 1
#         else:
#             # 否则，将当前字符添加到结果列表中
#             result.append(s[i])
#             i += 1
#     # 将结果列表转换为字符串并返回
#     return "".join(result)
#
# # 测试用例
# input_string = "aabccba"
# output_string = unsame(input_string)
# print(output_string)  # 输出: "abcba"