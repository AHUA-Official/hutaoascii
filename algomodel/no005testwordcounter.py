from collections import Counter
import re

def count_words(text):
    # 分割单词并统计
    words = text.split()
    print(words)
    word_counts = Counter(words)
    print(word_counts)
    return word_counts


def main():
    # 假设文本内容
    text = "hello world hello everyone"

    # 统计单词
    word_counts = count_words(text)

    # 输出结果
    for word, count in word_counts.items():
        print(f"Word: {word}, Count: {count}")

s = '<html><h1>www.baidu.com</html>'
p = re.compile(r'<html><h1>(.*?)</html>')
result = re.findall(p, s)[0]
print(p)
print(result)