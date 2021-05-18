import os

import gensim
import numpy as np
import tensorflow as tf
from gensim.models.word2vec import Word2Vec
from gensim.corpora.dictionary import Dictionary
from gensim import models
import pandas as pd
import jieba
import logging
from keras import Sequential
from keras.preprocessing.sequence import pad_sequences
from keras.layers import Bidirectional,LSTM,Dense,Embedding,Dropout,Activation,Softmax
from sklearn.model_selection import train_test_split
from keras.utils import np_utils

# 封装模型和方法
class Sentiment:
    def __init__(self, w2id, embedding_weights, Embedding_dim, maxlen, labels_category):
        self.Embedding_dim = Embedding_dim
        self.embedding_weights = embedding_weights
        self.vocab = w2id
        self.labels_category = labels_category
        self.maxlen = maxlen
        self.model = self.build_model()

    def build_model(self):
        model = Sequential()
        # input dim(140,100)
        model.add(Embedding(output_dim=self.Embedding_dim,
                            input_dim=len(self.vocab) + 1,
                            weights=[self.embedding_weights],
                            input_length=self.maxlen))
        model.add(Bidirectional(LSTM(50), merge_mode='concat'))
        model.add(Dropout(0.5))
        model.add(Dense(self.labels_category))
        model.add(Activation('softmax'))
        model.compile(loss='categorical_crossentropy',
                      optimizer='adam',
                      metrics=['accuracy'])
        model.summary()
        return model

    def train(self, X_train, y_train, X_test, y_test, n_epoch=5):
        self.model.fit(X_train, y_train, batch_size=32, epochs=n_epoch,
                       validation_data=(X_test, y_test))
        self.model.save('sentiment.h5')

    def predict(self, model_path, new_sen):
        model = self.model
        model.load_weights(model_path)
        new_sen_list = jieba.lcut(new_sen)
        sen2id = [self.vocab.get(word, 0) for word in new_sen_list]
        sen_input = pad_sequences([sen2id], maxlen=self.maxlen)
        res = model.predict(sen_input)[0]
        return np.argmax(res)

    def load_model(self,modelPath):
        self.model.load_weights(modelPath)