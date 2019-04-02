#coding=utf-8
import jieba
import re
from collections import Counter


#导入打开要处理的文本傲慢与偏见中文版小说
txt = open("傲慢与偏见.txt", "r", encoding="gb18030").read()

#加入要去除的标点符号
excludes = {"，", "。", "\n", "-", "“", "”", "：", "；", "？", "（", "）", "！", "…"}

#利用jieba分词
words = jieba.lcut(txt)

#设置初始计数数组
counts = {}

#开始遍历计数
for word in words:
    counts[word] = counts.get(word,0)+1

#去除标点符号
for word in excludes:
    del counts[word]

#返回遍历得分所有键与值
items = list(counts.items())

print(len(items))

#根据词出现次序进行排序
items.sort(key=lambda x: x[1], reverse=True)

#将数据写入ｔｘｔ文本便于导入Matlab画图
file = open('data.txt', mode='w')

#输出词语与词频
for i in range(10963):
    word, count = items[i]
    print("{0:<10}{1:>5}".format(word,count))

    #写入ｔｘｔ文件
    new_context = word + "   " + str(count) + '\n'
    file.write(new_context)

file.close()



result = open('正则.txt', mode='w')
#存正则匹配的数组
things = []

#正则匹配：人物说的内容
for i in re.finditer("[说｜道]：“(.+)\？”", txt):
    message = i.group(1)
    things.append(message)

#计数和展示
c = Counter(things)
for k, v in c.most_common(51):
    print(k, v)
    context = k + "   " + str(v) + '\n'
    result.write(context)

result.close()
