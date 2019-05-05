from model import Article
from model import SemanticNetwork

if __name__ == '__main__':
    a = Article(r'full.txt',filter_stop_words=True)
    a.tokenize()
    a.lemmatize()
    a.tag()

    network = SemanticNetwork(a.words,link_threshold=0)
    network.draw()

    print('keywords:')
    for keyword, value in network.page_rank().items():
        print(keyword,value)