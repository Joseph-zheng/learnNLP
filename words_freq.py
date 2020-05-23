# -*- coding: utf-8 -*-
import jieba
import csv
import re

my_file = open("words_freq_all1.csv", "a+", encoding="gbk", newline="")

result = []
# 读取数据
consent_text = open("gejiurenminyiyuan.txt","r",encoding="utf-8").read()

# 只保留中文文本
cleaned_text1 = "".join(re.findall(r'[\u4e00-\u9fa5]+', consent_text))

# load stopwords
stop_words = open('stop_words.txt', 'r', encoding='utf-8').read()
# add stop words 用 stopwords.add()设置屏蔽显示的词语,可以添加多个
# stopwords = set(STOPWORDS)
# stopwords.add("aaaa")
# stopwords.add("bb")

word_cut = jieba.lcut(cleaned_text1)

# 去除停用词
cleaned_text2 = [w for w in word_cut if w not in stop_words]

# 去重
word_set = set(cleaned_text2)

# 排序
for word in word_set:
    if len(word) >= 1:
        freq = cleaned_text2.count(word)
        result.append((word, freq))

new_result = sorted(result, key=lambda k: k[1], reverse=True)

writer = csv.writer(my_file)

writer.writerow(('words', 'frequency'))

for i in new_result:
    writer.writerow(i)

my_file.close()

