#25年1月 minimax的   一来就是做题  但是 花了20分钟写好之后就不文化了
#描述   竖式打印乘法计算的流程
def print_vertical_multiplication(a, b):
    # 将两个数转换为字符串
    a_str = str(a)
    b_str = str(b)
    max_length = len(str(a*b))
    # 打印乘数
    print(f"  {a_str.rjust(max_length - 1)}")
    print(f"× {b_str.rjust(max_length - 1)}")
    print("-"*max_length)
    calme=[]
    for i in range(len(b_str)):
        calme.append(int(b_str[i]))
        calme.reverse()
    for j in range(len(b_str)):
        temp=a*calme[j]
        pp= str(temp).rjust(max_length-j)
        print(pp)



    # 打印加法线
    print("-"*max_length)

    final_result=a*b
    print(f"{final_result}")


# 示例
print_vertical_multiplication(11, 1111)