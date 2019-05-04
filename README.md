# ***Sing_Dance_Rap_Basketball***
[![LICENSE](https://img.shields.io/badge/license-Anti%20996-blue.svg?style=flat-square)](https://github.com/Yulibao/Sing_Dance_Rap_Basketball/blob/master/LICENSE)

## ***Data structure algorithm***：
> * Tokenize and lemmatize the text, and annotate  
with pos tags.

> * Add nouns and verbs words in the text as  
nodes in the network, compute the semantic  
similarity of two nodes, and link the two  
nodes if their semantic similarity is higher  
than a threshold.

> * Iterate the weighted Pagerank on the network  
until convergence.

> * Sort the nodes according to their Pagerank  
score and select top N nodes as the keywords  
of the text.

## ***Todos***:
*  分词 判断词性
   * ***直接调库，JieBa分词，挑出来动词和名词***
* 建立一个 Semantic Network
   * ***图中各顶点的PageRanke值随机初始化*** 
   * ***边的权重按照以下算法***  
   ![](https://s2.ax1x.com/2019/05/04/EdiC11.png)  
   * ***~~其中两个不理解的地方:~~***  
     ***~~论文里面的senses是啥玩意？~~***   
     ***~~Wordnet or Hownet具体怎么实现？~~***
     > * Let W1 has n senses S1i (i=1…n) and W2 has m  
       senses S2j (j=1…m). Then semantic similarity between  
       W1 and W2 can be approximately computed  
       by maximum similarity between their senses,  
       which can be measured by Wordnet or Hownet.

    * ***[Wordnet[1]](https://zh.wikipedia.org/wiki/WordNet)***
      ***[Wrodnet[2]](https://zhuanlan.zhihu.com/p/26527203)***
    * ***[Hownet](https://zhuanlan.zhihu.com/p/32688983)***  
    * ***[Wordnet、Hownet的比较](https://www.cnblogs.com/kaituorensheng/p/3569436.html)***

* 在上一步建立的数据结构上PageRank  
  * ***算法如下***  
    ![](https://s2.ax1x.com/2019/05/04/EdC5xx.png)
  * ***循环计算，直至收敛*** *//这里需要一个判定收敛的算法或者库*
