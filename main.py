from model import Article
from model import SemanticNetwork

if __name__ == '__main__':
    a = Article(r'test.txt', filter_stop_words=True)
    a.tokenize()
    a.lemmatize()
    a.tag()

    network = SemanticNetwork(a.words, di=True, link_threshold=0)
    network.draw()

    print(network.page_rank())
