from model import Article
from model import SemanticNetwork

if __name__ == '__main__':
    a = Article(r'test.txt', filter_stop_words=True)
    a.tokenize()
    a.lemmatize()
    a.tag()

    network_un = SemanticNetwork(a.words, di=False, link_threshold=0)
    network_di = SemanticNetwork(a.words, di=True, link_threshold=0)

    # network_un.draw()
    # network_di.draw()

    network_un.page_rank(title="Undirected graph", fig=(2, 3))
    network_di.page_rank(title="Directed graph", fig=(4, 5))
