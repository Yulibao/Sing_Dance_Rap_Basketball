from nltk.tokenize import word_tokenize
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import wordnet
from nltk import pos_tag
from nltk import data

import networkx

data.path.append('.\\Data')

class Article:
    text = ''
    words = []

    def __init__(self, file_name):
        #with open(file_name,'r') as f:
            #self.text = f.read().lower()
        self.text = file_name.lower()

    def tokenize(self):
        self.words = word_tokenize(self.text)

    def lemmatize(self):
        lemmatizer = WordNetLemmatizer().lemmatize
        self.words = [lemmatizer(word) for word in self.words]
        self.words = [lemmatizer(word,'v') for word in self.words]

    def tag(self):
        self.words = pos_tag(self.words)

class SemanticNetwork:
    word_type = ['VB', 'NN']
    node_word_map = []
    g = networkx.DiGraph()

    link_threshold = 0.1

    def __init__(self, taged_words, link_threshold):
        self.link_threshold = link_threshold

        i = 0
        for word in range(len(taged_words)):
            if word[1] in self.word_type:
                self.node_word_map.append((word[0],i))
                i += 1

        for

    def 