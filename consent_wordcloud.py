# -*- coding:utf-8 -*-
import re
import jieba.analyse
from wordcloud import WordCloud
from imageio import imread


# read files
text = open("sample_informed_consent.txt", "r", encoding="utf-8").read()

stop_words = open("stop_words.txt", "r", encoding="utf-8").read()

text1 = "".join(re.findall(r'[\u4e00-\u9fa5]+', text))

# cut words
cut_text = jieba.lcut(text1)

# remove stop words
clean_text = [w for w in cut_text if w not in stop_words]

# 关键词作为词云
word_list = " ".join(clean_text)

frequencies = jieba.analyse.extract_tags(word_list, topK=50, withWeight=True)

# converts the results to the dictionary
freq_dict = dict(frequencies)

image = imread("coverimage.jpg")  # 读取图片
mask = image

# 自定义字体颜色
# def grey_color_func(word, font_size, position, orientation, random_state=None,**kwargs):
# return 'hsl(0,0%%,%d%%)'% random.randint(50,55)
# word_cloud.recolor(color_func=grey_color_func)

# 词云函数设置
cloud = WordCloud(
    font_path="simhei.ttf",
    background_color="white",
    max_words=100,
    max_font_size=150,
    min_font_size=4,
    mask=image,
)

# generate and save wordcloud
word_cloud = cloud.generate_from_frequencies(freq_dict)
word_cloud.to_file("consent_word_cloud2.jpg")
