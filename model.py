from nltk.tokenize import word_tokenize
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import wordnet
from nltk.corpus import stopwords
from nltk import pos_tag
from nltk import data

import networkx
import matplotlib.pyplot as plt

from page_rank import pagerank

data.path.append('.\\Data')


class Article:
    text = ''
    words = []
    filter_button = {"stop_words": False, "repeat": False}

    def __init__(self, file_name, filter_stop_words=False, filter_repeate=False):
        with open(file_name, 'r') as f:
            self.text = f.read().lower()

        self.filter_button = {"stop_words": filter_stop_words, "repeat": filter_repeate}

    def tokenize(self):
        self.words = word_tokenize(self.text)

        # filter
        if self.filter_button["stop_words"]:
            self.words = [w for w in self.words if w not in stopwords.words("english")]

    def lemmatize(self):
        lemmatizer = WordNetLemmatizer().lemmatize
        self.words = [lemmatizer(word) for word in self.words]
        self.words = [lemmatizer(word, 'v') for word in self.words]

        # filter
        if self.filter_button["repeat"]:
            self.words = list(set(self.words))

    def tag(self):
        self.words = pos_tag(self.words, tagset='universal')


class SemanticNetwork:
    word_type = ['NOUN', 'VERB']
    node_word_map = []
    g = networkx.DiGraph()

    link_threshold = 0

    def __init__(self, taged_words, di=False, link_threshold=0):
        self.link_threshold = link_threshold

        i = 0
        n = len(taged_words)
        # filter and map
        for word in taged_words:
            if word[1] in self.word_type:
                self.node_word_map.append((word[0], i))
                i += 1

        n = len(self.node_word_map)
        for i in range(n - 1):
            for j in range(i + 1, n):
                link = SemanticNetwork.get_semantic_link(self.node_word_map[i][0], self.node_word_map[j][0])

                if link > self.link_threshold:
                    if di:
                        self.g.add_edges_from([(i, j, {'weight': link})])
                    else:
                        self.g.add_edges_from([(i, j, {'weight': link}), (j, i, {'weight': link})])

    def draw(self):
        plt.figure(1)
        layout = networkx.spring_layout(self.g)
        networkx.draw(self.g, pos=layout, node_color='g', with_labels=True)
        plt.show()

    @staticmethod
    def get_semantic_link(word1, word2):
        synsets1 = wordnet.synsets(word1)
        synsets2 = wordnet.synsets(word2)

        max_similarity = -1

        for synset1 in synsets1:
            for synset2 in synsets2:
                temp = synset1.wup_similarity(synset2)
                if temp is not None and temp > max_similarity:
                    max_similarity = temp

        return max_similarity

    def page_rank(self, draw=False):
        pr = pagerank(self.g, alpha=0.85)
        average = sum(pr.values()) / len(pr)

        if draw:
            plt.figure(2)
            layout = networkx.spring_layout(self.g)
            networkx.draw(self.g, pos=layout, node_size=[250 + (x - average) * 15000 for x in pr.values()],
                          node_color='m',
                          with_labels=True)
            plt.show()

        pr_sorted_tup = sorted(pr.items(), key=lambda x: x[1], reverse=True)
        top_ten_tup = pr_sorted_tup[0:10]
        top = top_ten_tup[0][1]
        last = top_ten_tup[9][1]
        diff = top - last

        plt.figure(3)
        plt.barh(range(10), [record[1] for record in top_ten_tup], height=0.7, color='steelblue', alpha=0.8)
        plt.yticks(range(10), [self.node_word_map[record[0]][0] for record in top_ten_tup])
        plt.xlim(top + diff * 0.1, last - diff * 0.1)
        plt.xlabel("PageRank Value")
        plt.title("KeyWords")
        plt.show()

        return dict([(self.node_word_map[record[0]][0], record[1]) for record in top_ten_tup])
