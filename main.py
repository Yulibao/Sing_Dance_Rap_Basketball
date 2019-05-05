from model import Article
from model import SemanticNetwork

if __name__ == '__main__':
    a = Article(r'test.txt')
    a.tokenize()
    a.lemmatize()
    a.tag()

    network = SemanticNetwork(a.words,link_threshold=0)
    network.draw()
    network.page_rank()