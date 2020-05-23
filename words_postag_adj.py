# -*- coding: utf-8 -*-
import pynlpir
import csv
import re


result = []
pynlpir.open(encoding='utf-8')

my_file = open("postag_adj1.csv", "a+", encoding="gbk", newline="")

consent_text = open("gejiurenminyiyuan.txt","r",encoding="utf-8").read()

# 只保留中文文本
cleaned_text1 = "".join(re.findall(r'[\u4e00-\u9fa5]+', consent_text))

my_segment = pynlpir.segment(cleaned_text1, pos_tagging=True, pos_names='child', pos_english=False)

word_list = [i for i, x in my_segment if x == "形容词"]
# print(word_list)

pynlpir.close()

word_set = set(word_list)

for word in word_set:
    if len(word) > 1:
        freq = word_list.count(word)
        result.append((word, freq))

new_result = sorted(result, key=lambda k: k[1], reverse=True)

writer = csv.writer(my_file)
writer.writerow(('words', 'pos_tag'))

for i in new_result:
    writer.writerow(i)

my_file.close()
