# -*- coding: utf-8 -*-
import pynlpir
import re
import csv


pynlpir.open(encoding='utf-8')

my_file = open("nlpir_kewords1.csv", "a+", encoding="gbk", newline="")

consent_text = open("huaihuasiyuan.txt","r",encoding="utf-8").read()

# 只保留中文文本
cleaned_text1 = "".join(re.findall(r'[\u4e00-\u9fa5]+', consent_text))

my_keywords = pynlpir.get_key_words(cleaned_text1, max_words=20, weighted=True)

writer = csv.writer(my_file)
writer.writerow(('words', 'weight'))

for i in my_keywords:
    writer.writerow(i)

my_file.close()
pynlpir.close()
