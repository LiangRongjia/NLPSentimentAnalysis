import io
from sklearn.model_selection import train_test_split
from keras_preprocessing.sequence import pad_sequences
from keras.utils import np_utils
import numpy as np
from gensim.corpora import Dictionary
import sys
import json
import os
import time
import gensim
import kashgari
from py.backend import Sentiment
from py.backend import *

sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding='utf8')
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

# 需要的函数


def load_model(word_model):
    # model = Word2Vec(vector_size=100,  # 词向量维度
    #                  min_count=5,  # 词频阈值
    #                  window=5)  # 窗口大小
    model = gensim.models.word2vec.Word2Vec.load(word_model)
    return model


def generate_id2wec(word_model):
    gensim_dict = Dictionary()
    # gensim_dict.doc2bow(model.wv.vocab.keys(), allow_update=True)
    gensim_dict.doc2bow(model.wv.index_to_key, allow_update=True)
    w2id = {v: k + 1 for k, v in gensim_dict.items()}  # 词语的索引，从1开始编号
    # print(w2id.keys())
    # for word in w2id.keys():
    #     print(model.predict_output_word(word))
    # print()
    w2vec = {word: model.wv[word] for word in w2id.keys()}  # 词语的词向量
    # print(w2vec)
    n_vocabs = len(w2id) + 1
    embedding_weights = np.zeros((n_vocabs, 100))
    for w, index in w2id.items():  # 从索引为1的词语开始，用词向量填充矩阵
        embedding_weights[index, :] = w2vec[w]
    return w2id, embedding_weights


# 获得文字和索引
loaded_model = kashgari.utils.load_model(
    'py/REVISED_location_WordEmbedding.h5')


def getWordAndIndex(title):
    # 按字符预测，得到每个字符预测后的标签
    t = loaded_model.predict([[char for char in title]])

    word = []
    wordIndex = []
    count = 0
    tempWord = ""
    tempWordTag = ""
    tempWordLength = 0
    while(count < len(t[0])):
        if t[0][count] == 'O':
            count += 1
            tempWord = ""
            tempWordTag = ""
            tempWordLength = 0
            continue
        if 'B-' in t[0][count]:
            tempWord += title[count]
            tempWordTag = t[0][count][2:]
            tempWordLength += 1
            count += 1
            while(1):
                if 'I-' not in t[0][count]:
                    word.append([tempWord, tempWordTag])
                    wordIndex.append([count - tempWordLength, count])
                    break
                tempWord += title[count]
                tempWordTag = t[0][count][2:]
                tempWordLength += 1
                count += 1

        tempWord = ""
        tempWordTag = ""
        tempWordLength = 0
    return word, wordIndex


# 单条分析


def singleAnalyses(comment, senti):
    # 预测结果映射表
    label_dic = {0: "消极的", 1: "积极的", 2: "中性的"}
    # 预测态度
    pre = senti.predict("py/sentiment.h5", comment)
    # 态度
    theAttitude = label_dic.get(pre)
    # 角度
    word, wordIndex = getWordAndIndex(comment)
    # 构造输出对象
    output_dic = {
        "commentText": comment,
        "attitude": theAttitude,
        "textFeatures": {
            "words": word,
            "wordIndexs": wordIndex
        },
        "reply": "自动回复"
    }
    return output_dic


# 路径设置
path_dataToPy = 'dataToPy.json'
path_dataToNodeJs = 'dataToNodeJs.json'

# 获取词向量矩阵
model = load_model("py/word2vec.model")
w2id, embedding_weights = generate_id2wec(model)

# 导入模型
senti = Sentiment(w2id, embedding_weights, 100, 200, 3)
senti.load_model("py/sentiment.h5")

print('ok')
sys.stdout.flush()

# 输入
while True:
    line = sys.stdin.readline()
    result = singleAnalyses(line, senti)
    jsString = json.dumps(result,  ensure_ascii=False)
    print(jsString)
    sys.stdout.flush()
