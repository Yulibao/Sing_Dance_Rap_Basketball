import nltk

download_dir = "..\\Data"

if __name__ == '__main__':
    nltk.download('punkt', download_dir=download_dir)
    nltk.download('averaged_perceptron_tagger', download_dir=download_dir)
    nltk.download('wordnet', download_dir=download_dir)
    """
    使用时导入 先配置数据路径
    from nltk import data
    data.path.append('(项目根目录)\\Data')
    """
