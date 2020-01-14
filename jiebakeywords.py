# -*- coding: utf-8 -*-
"""
    使用 jieba分词，提取关键词
@Date 2019-10-10
"""
import jieba
from jieba.analyse import *
# jieba.load_userdict(r'G:\aa\three.txt') load 自己的词库

# readfiles
data = open('test.txt', 'r',encoding='utf-8').read()

# load stopwords
stop_words = open('stop_words.txt', 'r',encoding='utf-8').read()
# add stop words 用 stopwords.add()设置屏蔽显示的词语,可以添加多个
# stopwords = set(STOPWORDS)
# stopwords.add("aaaa")
# stopwords.add("bb")
# load stopwords

# cut words 你可以用自己的词典 jieba.load_userdict("userdict.txt")
# 也可以往jieba词库添加词jieba.add_word("知情同意")或者jieba.del_word("自定义")
cut_text = jieba.lcut(data)


# remove stop words
clean_text = [w for w in cut_text if w not in stop_words]

# clean wordlist
word_list = ' '.join(clean_text)

# extract keywords iin two ways
# TD-IDF
# TD词频是这词在目前分析材料中的比例，相当于内置函数会计算一个TD值，IDF根据语料库来的，这里用的通用语料库
# 如果有自己的语料库，把这个语句，加在下面语句前面，jieba.analyse.set_idf_path(r"D:\wdic.txt")
# topK是前十个关键词，后面带有权重
for keyword, weight in extract_tags(word_list, topK=10, withWeight=True):
    print('%s %s' % (keyword, weight))

# textrank 提取
# for keyword, weight in textrank(word_list, withWeight=True):
#    print('%s %s' % (keyword, weight))
