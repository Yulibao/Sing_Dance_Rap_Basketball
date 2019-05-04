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
        with open(file_name,'r') as f:
            self.text = f.read().lower()

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

    def __init__(self, taged_words, link_threshold=0):
        self.link_threshold = link_threshold

        i = 0
        n = len(taged_words)
        for word in taged_words:
            if word[1] in self.word_type:
                self.node_word_map.append((word[0],i))
                i += 1

        n = len(self.node_word_map)
        for i in range(n):
            for j in range(i, n):
                link = SemanticNetwork.get_semantic_link(self.node_word_map[i][0],self.node_word_map[j][0])

                if link> self.link_threshold:
                 self.g.add_weighted_edges_from([(i, j, link)])

    @staticmethod
    def get_semantic_link(word1, word2):
        synsets1 = wordnet.synsets(word1)
        synsets2 = wordnet.synsets(word2)

        max_similarity = -1

        for synset1 in synsets1:
            for synset2 in synsets2:
                temp = synset1.path_similarity(synset2)
                if temp is not None and temp > max_similarity:
                    max_similarity = temp

        return max_similarity

    def page_rank(self):
        dic=networkx.pagerank(self.g,alpha=0.5)
        result = sorted(dic.items(), key=lambda x: x[1], reverse=True)
        return result[0:10]