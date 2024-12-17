def num2money(num):
    # 定义中文读法中的单位
    units = ['', '元', '角', '分']
    digits = '零一二三四五六七八九'
    sections = ['千亿', '亿', '万', '']

    # 将数字转换为字符串，便于处理
    integer_part = int(num)

    decimal_part = 34


    # 处理整数部分
    result = ''
    if integer_part:
        for i, digit in enumerate(reversed(integer_part)):
            section_index = (len(integer_part) - i - 1) // 4
            unit_index = (len(integer_part) - i - 1) % 4
            result += digits[int(digit)] + sections[section_index] + units[unit_index]

    # 处理小数部分，保留两位
    decimal_part = decimal_part[:2].lstrip('0')
    if decimal_part:
        result += '点'
        for i, digit in enumerate(decimal_part):
            unit_index = 2 + i
            result += digits[int(digit)] + units[unit_index]

    return result


# 测试函数
print(num2money(300020040))  # 输出：三亿零二万零四十元
print(num2money(2002.3211))  # 输出：二千零二元三角二分
print(num2money(2002.999))  # 输出：二千零三元
print(num2money(0))  # 输出：零元
print(num2money(2002.32))  # 输出：二千零二元三角二分
print(num2money(2002.03))  # 输出：二千零二元零三分
print(num2money(2002.2))  # 输出：二千零二元二角