# -*- coding: utf-8 -*-
import jieba
from jieba.analyse import *
import re
import csv


my_file = open("jieba_kewords1.csv", "a+", encoding="utf-8", newline="")
result = []
# 读取数据
consent_text = open("huaihuasiyuan.txt","r",encoding="utf-8").read()

# 只保留中文文本
cleaned_text1 = "".join(re.findall(r'[\u4e00-\u9fa5]+', consent_text))

# load stopwords
stop_words = open('stop_words.txt', 'r', encoding='utf-8').read()
# add stop words 用 stopwords.add()设置屏蔽显示的词语,可以添加多个
# stopwords = set(STOPWORDS)
# stopwords.add("aaaa")
# stopwords.add("bb")

word_cut = jieba.lcut(cleaned_text1)

cleaned_text2 = [w for w in word_cut if w not in stop_words]

word_list = ' '.join(cleaned_text2)

TD = []

for keyword, weight in extract_tags(word_list, topK=20, withWeight=True):
    TD.append((keyword,weight))

TR = []
for keyword, weight in textrank(word_list, topK=20, withWeight=True):
    TR.append((keyword, weight))

writer = csv.writer(my_file)
writer.writerow(('words', 'weight'))

for i in TD:
    writer.writerow(i)

for i in TR:
    writer.writerow(i)

my_file.close()
