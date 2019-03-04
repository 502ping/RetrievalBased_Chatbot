import jieba
from gensim import corpora,models,similarities
import codecs



#读取训练词库
Train_test = 'tencent_corpus/data.txt'
Traintest = codecs.open(Train_test,'rb').readlines()
Traintest = [w.strip() for w in Traintest]
# 分词完毕得到结果
Traintest_word = []
for word in Traintest:

    words_list = [words for words in jieba.cut(word)]
    Traintest_word.append(words_list)


#测试用词

#TestResult = [] 
#TestResult1 = []
#for word in doc_test_list:
#    if  word not in stopwords:
#        TestResult = TestResult1.append(word)
#用dictionary方法获取词袋
dictionary = corpora.Dictionary(Traintest_word)
#词袋中用数字对所有词进行了编号
dictionary.keys()
#使用doc2bow制作语料库，利用词袋模型中的字典将其映射到向量空间
corpus = [dictionary.doc2bow(doc) for doc in Traintest_word]
#对测试文档也进行制作语料库，利用词袋模型中的字典将其映射到向量空间

tfidf_moel = models.TfidfModel(corpus)
tfidf_moel.save('tfidf.model')
#使用TF-IDF模型对语料库建模

print("***************Model has been successfully built!*******************")

print("***************Begin Testing*******************")

while 1:


    keyword = input("ask:")

    input_str = keyword

    doc_test = input_str
    doc_test_list = [word for word in jieba.cut(doc_test)]

    doc_test_vec = dictionary.doc2bow(doc_test_list)


    #获文档中，每个词的TF-IDF值 tfidf[corpus]
    #对每个目标文档，分析测试文档的相似度
    index = similarities.SparseMatrixSimilarity(tfidf_moel[corpus], num_features=len(dictionary.keys()))
    sim = index[tfidf_moel[doc_test_vec]]
    #根据相似度排序是一个列表  表中每一项是一个元组   元组中前面是原句索引  后面是相似度
    SimilaritiesList = sorted(enumerate(sim), key=lambda item: -item[1])

    num = 0
    while (num <= 1):
        Result_tutple = SimilaritiesList[num]  # 获取元组   索引  相似度
        Result_index = Result_tutple[0]  # 获取索引
        num = num + 1

        response_list = Traintest_word[Result_index]

        Result_score = Result_tutple[1]  # 获取索引

        print("该回答相似度为"+str(Result_score))


        if response_list.index('\t')!=-1:

            newlist =  response_list[response_list.index('\t'):]

            response=''
            for res in newlist:
                response+=res
            print("answer:"+response)






