# coding: UTF-8

import os
import jieba
import jieba.analyse
import gensim
import pandas as pd

model = gensim.models.KeyedVectors.load_word2vec_format("/Users/yuhaomao/Desktop/AES-CN/word2vec/news_12g_baidubaike_20g_novel_90g_embedding_64.bin", binary=True)
print(pd.Series(model.most_similar(u'微信')))