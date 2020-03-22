# 题目：写一个函数，倒序取出一句话中每个单词的第一个字母
#1 用split分割，但是只能分割空格，标点符号不能
# class Sortstr(object):
#     def __init__(self):
#         self.run()

#     def run(self):
#         with open('word.txt',encoding='utf-8') as f:
#             content = f.read()
#             ls = content.split()
#             for i in ls:
#                 print(i)

# if __name__ == "__main__":
#     so = Sortstr()

#2 使用正则表达式 
import re
with open('word.txt',encoding='utf-8') as f:
    content = f.read()
# 首先生成一个正则表达式对象。使用compile函数
# 然后pattern这个正则表达式对象去文本匹配（search，match，findall等方法）
# b代表单词 中括号里任选，其中转义了一个上标，匹配i'm这种
pattern = re.compile(r'\b[a-zA-Z\']+\b')
# findall方法返回列表
ls = pattern.findall(content)
#列表倒序排列。从-1开始，后面-1表示倒序,中间不能写0.否则不包含 ls2[0]
ls2 = ls[-1::-1]
for i in ls2:
    # 每一个字符串也可以进行切片操作
    print(i[-1])